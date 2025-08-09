"""
Real data source connectors for SOC Dashboard
Supports multiple databases, APIs, and log files
"""

import streamlit as st
import pandas as pd
import sqlite3
import requests
import json
import os
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseConnector:
    """Handle database connections and queries"""
    
    def __init__(self):
        self.connection = None
    
    def connect_sqlite(self, db_path: str = "soc_data.db"):
        """Connect to SQLite database"""
        try:
            self.connection = sqlite3.connect(db_path)
            return True
        except Exception as e:
            st.error(f"SQLite connection failed: {e}")
            return False
    
    def connect_postgresql(self, host: str, port: int, database: str, 
                          user: str, password: str):
        """Connect to PostgreSQL database"""
        try:
            import psycopg2
            self.connection = psycopg2.connect(
                host=host, port=port, database=database,
                user=user, password=password
            )
            return True
        except Exception as e:
            st.error(f"PostgreSQL connection failed: {e}")
            return False
    
    def connect_mysql(self, host: str, port: int, database: str,
                     user: str, password: str):
        """Connect to MySQL database"""
        try:
            import mysql.connector
            self.connection = mysql.connector.connect(
                host=host, port=port, database=database,
                user=user, password=password
            )
            return True
        except Exception as e:
            st.error(f"MySQL connection failed: {e}")
            return False
    
    def execute_query(self, query: str) -> pd.DataFrame:
        """Execute SQL query and return DataFrame"""
        if not self.connection:
            st.error("No database connection established")
            return pd.DataFrame()
        
        try:
            return pd.read_sql_query(query, self.connection)
        except Exception as e:
            st.error(f"Query execution failed: {e}")
            return pd.DataFrame()

class SecurityAPIConnector:
    """Connect to security intelligence APIs"""
    
    def __init__(self):
        self.apis = {
            'virustotal': 'https://www.virustotal.com/vtapi/v2/',
            'abuseipdb': 'https://api.abuseipdb.com/api/v2/',
            'otx': 'https://otx.alienvault.com/api/v1/'
        }
    
    def check_ip_reputation(self, ip_address: str, api_key: str, 
                           service: str = 'abuseipdb') -> Dict:
        """Check IP reputation using various services"""
        try:
            if service == 'abuseipdb':
                headers = {
                    'Key': api_key,
                    'Accept': 'application/json'
                }
                params = {
                    'ipAddress': ip_address,
                    'maxAgeInDays': 90,
                    'verbose': ''
                }
                response = requests.get(
                    f"{self.apis['abuseipdb']}check",
                    headers=headers,
                    params=params
                )
                return response.json() if response.status_code == 200 else {}
            
            elif service == 'virustotal':
                params = {
                    'apikey': api_key,
                    'ip': ip_address
                }
                response = requests.get(
                    f"{self.apis['virustotal']}ip-address/report",
                    params=params
                )
                return response.json() if response.status_code == 200 else {}
                
        except Exception as e:
            logger.error(f"API call failed for {service}: {e}")
            return {}
    
    def get_threat_intelligence(self, indicator: str, api_key: str) -> Dict:
        """Get threat intelligence from AlienVault OTX"""
        try:
            headers = {'X-OTX-API-KEY': api_key}
            response = requests.get(
                f"{self.apis['otx']}indicators/IPv4/{indicator}/general",
                headers=headers
            )
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            logger.error(f"OTX API call failed: {e}")
            return {}

class LogFileConnector:
    """Parse and ingest log files"""
    
    def __init__(self):
        self.supported_formats = ['json', 'csv', 'syslog', 'apache', 'nginx']
    
    def parse_json_logs(self, file_path: str) -> pd.DataFrame:
        """Parse JSON log files"""
        try:
            logs = []
            with open(file_path, 'r') as f:
                for line in f:
                    try:
                        log_entry = json.loads(line.strip())
                        logs.append(log_entry)
                    except json.JSONDecodeError:
                        continue
            return pd.DataFrame(logs)
        except Exception as e:
            st.error(f"Failed to parse JSON logs: {e}")
            return pd.DataFrame()
    
    def parse_csv_logs(self, file_path: str) -> pd.DataFrame:
        """Parse CSV log files"""
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            st.error(f"Failed to parse CSV logs: {e}")
            return pd.DataFrame()
    
    def parse_syslog(self, file_path: str) -> pd.DataFrame:
        """Parse syslog format files"""
        try:
            logs = []
            with open(file_path, 'r') as f:
                for line in f:
                    parts = line.strip().split(' ', 5)
                    if len(parts) >= 6:
                        logs.append({
                            'timestamp': f"{parts[0]} {parts[1]} {parts[2]}",
                            'hostname': parts[3],
                            'service': parts[4].rstrip(':'),
                            'message': parts[5] if len(parts) > 5 else ''
                        })
            return pd.DataFrame(logs)
        except Exception as e:
            st.error(f"Failed to parse syslog: {e}")
            return pd.DataFrame()

class RealDataManager:
    """Main class to manage all real data sources"""
    
    def __init__(self):
        self.db_connector = DatabaseConnector()
        self.api_connector = SecurityAPIConnector()
        self.log_connector = LogFileConnector()
        self.data_cache = {}
        self.last_update = {}
    
    def setup_sample_database(self):
        """Create sample SQLite database with security events"""
        if self.db_connector.connect_sqlite():
            # Create tables
            create_events_table = """
            CREATE TABLE IF NOT EXISTS security_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                event_id TEXT UNIQUE,
                severity TEXT,
                event_type TEXT,
                source_ip TEXT,
                destination_ip TEXT,
                port INTEGER,
                protocol TEXT,
                status TEXT,
                mitre_technique TEXT,
                description TEXT
            )
            """
            
            create_assets_table = """
            CREATE TABLE IF NOT EXISTS assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                asset_name TEXT,
                asset_type TEXT,
                ip_address TEXT,
                risk_score INTEGER,
                last_seen DATETIME,
                vulnerabilities INTEGER
            )
            """
            
            cursor = self.db_connector.connection.cursor()
            cursor.execute(create_events_table)
            cursor.execute(create_assets_table)
            
            # Insert sample data
            sample_events = [
                ('EVT-001', 'Critical', 'Malware', '192.168.1.100', '10.0.0.5', 443, 'HTTPS', 'Active', 'T1566.001', 'Suspicious file download'),
                ('EVT-002', 'High', 'Phishing', '203.0.113.45', '192.168.1.50', 80, 'HTTP', 'Blocked', 'T1566.002', 'Malicious email attachment'),
                ('EVT-003', 'Medium', 'DDoS', '198.51.100.10', '192.168.1.1', 80, 'HTTP', 'Mitigated', 'T1499', 'High volume requests'),
                ('EVT-004', 'Low', 'Port Scan', '203.0.113.100', '192.168.1.0', 22, 'SSH', 'Logged', 'T1046', 'Network reconnaissance'),
                ('EVT-005', 'Critical', 'Data Breach', '192.168.1.200', '10.0.0.10', 1433, 'SQL', 'Investigating', 'T1041', 'Unauthorized data access')
            ]
            
            sample_assets = [
                ('Web Server', 'Server', '192.168.1.10', 85, datetime.now(), 3),
                ('Database', 'Server', '192.168.1.20', 92, datetime.now(), 1),
                ('Firewall', 'Security', '192.168.1.1', 45, datetime.now(), 0),
                ('Workstation-01', 'Endpoint', '192.168.1.100', 67, datetime.now(), 5),
                ('Domain Controller', 'Server', '192.168.1.5', 78, datetime.now(), 2)
            ]
            
            cursor.executemany(
                "INSERT OR IGNORE INTO security_events (event_id, severity, event_type, source_ip, destination_ip, port, protocol, status, mitre_technique, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                sample_events
            )
            
            cursor.executemany(
                "INSERT OR IGNORE INTO assets (asset_name, asset_type, ip_address, risk_score, last_seen, vulnerabilities) VALUES (?, ?, ?, ?, ?, ?)",
                sample_assets
            )
            
            self.db_connector.connection.commit()
            st.success("Sample database created successfully!")
            return True
        return False
    
    def get_security_events(self, limit: int = 50) -> pd.DataFrame:
        """Get security events from database"""
        query = f"""
        SELECT timestamp, event_id, severity, event_type, source_ip, 
               destination_ip, port, protocol, status, mitre_technique, description
        FROM security_events 
        ORDER BY timestamp DESC 
        LIMIT {limit}
        """
        return self.db_connector.execute_query(query)
    
    def get_asset_data(self) -> pd.DataFrame:
        """Get asset information from database"""
        query = """
        SELECT asset_name, asset_type, ip_address, risk_score, 
               last_seen, vulnerabilities
        FROM assets
        ORDER BY risk_score DESC
        """
        return self.db_connector.execute_query(query)
    
    def enrich_with_threat_intel(self, df: pd.DataFrame, api_key: str) -> pd.DataFrame:
        """Enrich events with threat intelligence"""
        if df.empty or not api_key:
            return df
        
        enriched_data = []
        for _, row in df.iterrows():
            row_dict = row.to_dict()
            
            # Check source IP reputation
            if 'source_ip' in row_dict and row_dict['source_ip']:
                reputation = self.api_connector.check_ip_reputation(
                    row_dict['source_ip'], api_key
                )
                if reputation:
                    row_dict['ip_reputation_score'] = reputation.get('abuseConfidencePercentage', 0)
                    row_dict['is_malicious'] = reputation.get('abuseConfidencePercentage', 0) > 75
            
            enriched_data.append(row_dict)
        
        return pd.DataFrame(enriched_data)
    
    def get_real_time_metrics(self) -> Dict:
        """Get real-time metrics from database"""
        metrics = {}
        
        # Total events today
        query = """
        SELECT COUNT(*) as total_events 
        FROM security_events 
        WHERE DATE(timestamp) = DATE('now')
        """
        result = self.db_connector.execute_query(query)
        metrics['total_events'] = result['total_events'].iloc[0] if not result.empty else 0
        
        # Critical events today
        query = """
        SELECT COUNT(*) as critical_events 
        FROM security_events 
        WHERE DATE(timestamp) = DATE('now') AND severity = 'Critical'
        """
        result = self.db_connector.execute_query(query)
        metrics['critical_events'] = result['critical_events'].iloc[0] if not result.empty else 0
        
        # High risk assets
        query = """
        SELECT COUNT(*) as high_risk_assets 
        FROM assets 
        WHERE risk_score > 80
        """
        result = self.db_connector.execute_query(query)
        metrics['high_risk_assets'] = result['high_risk_assets'].iloc[0] if not result.empty else 0
        
        return metrics
