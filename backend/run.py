from app import create_app
import os
from dotenv import load_dotenv
from app.modbus_client import check_modbus_connection
from app.config import Config

load_dotenv()

app = create_app()

if __name__ == '__main__':
    # Verify connection before starting
    if os.environ.get("SIMULATION_MODE", "false").lower() != "true":
        print(f"Testing connection to {Config.MODBUS_GATEWAY_IP}:{Config.MODBUS_PORT}...")
        if not check_modbus_connection():
            print("⚠️ Warning: Could not connect to Modbus gateway. Starting in limited mode.")
    
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = os.environ.get('FLASK_ENV', 'development') == 'development'
    
    print(f"\nServer starting on http://{host}:{port}")
    print(f"Modbus gateway: {Config.MODBUS_GATEWAY_IP}:{Config.MODBUS_PORT}")
    print(f"Simulation mode: {os.environ.get('SIMULATION_MODE', 'false')}\n")
    
    app.run(host=host, port=port, debug=debug)