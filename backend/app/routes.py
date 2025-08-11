from flask import Blueprint, jsonify, request
from .modbus_client import get_meter_data
from .config import Config
import os

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/substations', methods=['GET'])
def get_substations():
    try:
        return jsonify({
            "status": "success",
            "substations": list(Config.SUBSTATIONS.keys())
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@bp.route('/meters/<substation_name>', methods=['GET'])
def get_meters(substation_name):
    try:
        substation = Config.SUBSTATIONS.get(substation_name)
        if not substation:
            return jsonify({
                "status": "error",
                "message": f"Substation {substation_name} not found"
            }), 404
            
        return jsonify({
            "status": "success",
            "meters": substation
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@bp.route('/meter-data', methods=['GET'])
def get_meter_data_route():
    try:
        slave_id = request.args.get('slave_id')
        meter_name = request.args.get('meter_name', '')
        
        if not slave_id:
            return jsonify({
                "status": "error",
                "message": "slave_id parameter is required"
            }), 400
            
        try:
            slave_id = int(slave_id)
        except ValueError:
            return jsonify({
                "status": "error",
                "message": "slave_id must be a number"
            }), 400
        
        data = get_meter_data(slave_id)
        
        if "error" in data:
            return jsonify({
                "status": "error",
                "message": data["error"],
                "details": f"Failed to read from slave {slave_id}"
            }), 500
            
        return jsonify({
            "status": "success",
            "meter": meter_name,
            "data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@bp.route('/status', methods=['GET'])
def status():
    return jsonify({
        "status": "success",
        "simulation_mode": os.environ.get("SIMULATION_MODE", "false").lower() == "true",
        "modbus_gateway": f"{Config.MODBUS_GATEWAY_IP}:{Config.MODBUS_PORT}",
        "connection_status": "connected" if os.environ.get("SIMULATION_MODE", "false").lower() == "true" 
                          else "disconnected"
    })