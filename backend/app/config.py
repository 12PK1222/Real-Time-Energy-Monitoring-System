class Config:
    MODBUS_GATEWAY_IP = "172.16.51.229"
    MODBUS_PORT = 502
    MODBUS_TIMEOUT = 5
    MODBUS_RETRIES = 2
    
    PARAMETER_MAP = {
        "Voltage Vab": 0,
        "Voltage Vbc": 2, 
        "Voltage Vca": 4,
        "IR Current": 6,
        "IY Current": 8,
        "IB Current": 10,
        "Active Power": 52,
        "Apparent Power": 54,
        "Reactive Power": 60,
        "Power Factor": 62,
        "Frequency": 70
    }
    
    SUBSTATIONS = {
        "MSDS-1 132KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "MSDS-6 132KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "1RP 11KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "7RP 11KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "18RP 11KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "41RP 11KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "MSS": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "RUNNING STATUS": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MSDS-1 11KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "MSDS-6 33KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "1RP1 6.6KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "8RP 11KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "18RP1 6.6KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "41RP1 6.6KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "F-CUT 6.6KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "RTU A88": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MSDS-2 132KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "LF-1 33KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "1RPNEW 11KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "8RP1 11KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "20RP 6.6KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "41RP2 3.3KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "CENTRAL": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "RTU SEMENS": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MSDS-2 11KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "LF-2 33KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "1RPNEW 6.6KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "9RP 11KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "21RP 11KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "41RP3 3.3KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "HSM": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "BPSCL": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MSDS-3 132KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "MSDS-6 11KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "2RP 11KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "10RP 11KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "22RP 11KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "TPP-CPP 132KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "IRON": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "LF-3 33KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MSDS-3 11KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "MSDS-6 3.3KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "3RP 11KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "13RP 11KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "24RP 11KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "TPP 6.6KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "CRM": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MSDS-12 11KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MSDS-4 11KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "MSDS-7 11KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "3RP-NEW 6.6KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "14RP 11KV": [
            {"name": "14RP_Meter1", "slave_id": 10},
            {"name": "14RP_Meter2", "slave_id": 11},
            {"name": "14RP_Meter3", "slave_id": 12},
            {"name": "14RP_Meter4", "slave_id": 13}
        ],
        "15RP 11KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "25RP 11KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "ASS-2 11KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "BF": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MSDS-4NEW 11KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MSDS-9 132KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "MSDS-9 11KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "4RP 11KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "15RP1 6.6KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "26RP 6.6KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "ASS-3 11KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "SMS": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MSDS-4NEW 6.6KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MSDS-9 6.6KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "5RP 11KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "16RP 11KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "02RP-2 11KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "ASS-4 11KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "S.MILL": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "MSDS-5 132KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MSDS-11 132KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "6RP 11KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "17RP 11KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "02RP-4 6.6KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "TOWNSHIP 132KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "WATER SUPPLY": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "MSDS-5 11KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "MSDS-11 33KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "6RP0 6.6KV": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "17RP1 6.6KV": [
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13}
        ],
        "02RP-5 11KV": [
            {"name": "IED:11|C217_12", "slave_id": 12},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11}
        ],
        "TOWNSHIP 11KV": [
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ],
        "MISC": [
            {"name": "IED:110G21_13", "slave_id": 13},
            {"name": "IED:110G2_10", "slave_id": 10},
            {"name": "IED:11|C15_11", "slave_id": 11},
            {"name": "IED:11|C217_12", "slave_id": 12}
        ]
    }
    
    
   