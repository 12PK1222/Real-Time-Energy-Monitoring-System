import os
import struct
import socket
from pymodbus.client import ModbusTcpClient
from pymodbus.transaction import ModbusSocketFramer
from pymodbus.exceptions import ModbusException
from .config import Config

def generate_simulated_data():
    """Generate realistic simulated meter data"""
    return {
        "Voltage Vab": round(415.0 + (10 * (0.5 - (os.getpid() % 100)/100)), 2),
        "Voltage Vbc": round(415.0 + (10 * (0.5 - ((os.getpid()+33) % 100)/100)), 2),
        "Voltage Vca": round(415.0 + (10 * (0.5 - ((os.getpid()+67) % 100)/100)), 2),
        "IR Current": round(50.0 + (20 * (0.5 - (os.getpid() % 100)/100)), 2),
        "IY Current": round(50.0 + (20 * (0.5 - ((os.getpid()+50) % 100)/100)), 2),
        "IB Current": round(50.0 + (20 * (0.5 - ((os.getpid()+25) % 100)/100)), 2),
        "Active Power": round(100.0 + (40 * (0.5 - (os.getpid() % 100)/100)), 2),
        "Apparent Power": round(120.0 + (40 * (0.5 - ((os.getpid()+75) % 100)/100)), 2),
        "Reactive Power": round(80.0 + (30 * (0.5 - ((os.getpid()+15) % 100)/100)), 2),
        "Power Factor": round(0.85 + (0.2 * (0.5 - (os.getpid() % 100)/100)), 2),
        "Frequency": round(50.0 + (1 * (0.5 - ((os.getpid()+60) % 100)/100)), 2)
    }

def check_modbus_connection():
    """Verify if we can reach the Modbus gateway"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        return s.connect_ex((Config.MODBUS_GATEWAY_IP, Config.MODBUS_PORT)) == 0
    finally:
        s.close()

def get_meter_data(slave_id):
    if os.environ.get("SIMULATION_MODE", "false").lower() == "true":
        return generate_simulated_data()
    
    if not check_modbus_connection():
        return {"error": f"Cannot connect to Modbus gateway at {Config.MODBUS_GATEWAY_IP}:{Config.MODBUS_PORT}"}

    client = None
    try:
        client = ModbusTcpClient(
            host=Config.MODBUS_GATEWAY_IP,
            port=Config.MODBUS_PORT,
            framer=ModbusSocketFramer,
            timeout=Config.MODBUS_TIMEOUT,
            retries=Config.MODBUS_RETRIES
        )
        
        # Explicit connection with timeout
        if not client.connect():
            return {"error": "Modbus connection failed"}
        
        data = {}
        for param, address in Config.PARAMETER_MAP.items():
            try:
                # Try input registers first
                response = client.read_input_registers(address, 2, slave=slave_id)
                if response.isError():
                    # Fallback to holding registers
                    response = client.read_holding_registers(address, 2, slave=slave_id)
                    if response.isError():
                        data[param] = None
                        continue
                
                # Convert registers to float
                registers = response.registers
                if len(registers) == 2:
                    packed = struct.pack('>HH', registers[0], registers[1])
                    value = struct.unpack('>f', packed)[0]
                    data[param] = round(value, 2)
                else:
                    data[param] = None
                    
            except ModbusException:
                data[param] = None
        
        return data
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        if client:
            client.close()