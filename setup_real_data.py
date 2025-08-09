#!/usr/bin/env python3
"""
Setup script for SOC Dashboard real data connections
Run this to initialize your database and test connections
"""

import sqlite3
import requests
import json
from datetime import datetime, timedelta
import random

def create_sample_database():
    """Create a comprehensive sample database with realistic security data"""
    
    print("🗄️ Creating sample SQLite database...")
    
    # Connect to database
    conn = sqlite3.connect('soc_data.db')
    cursor = conn.cursor()
    
    # Create security_events table
    cursor.execute('''
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
            description TEXT,
            user_agent TEXT,
            country TEXT,
            reputation_score INTEGER
        )
    ''')
    
    # Create assets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_name TEXT,
            asset_type TEXT,
            ip_address TEXT,
            risk_score INTEGER,
            last_seen DATETIME,
            vulnerabilities INTEGER,
            os_type TEXT,
            department TEXT,
            criticality TEXT
        )
    ''')
    
    # Create compliance_scores table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS compliance_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            framework TEXT,
            score INTEGER,
            last_updated DATETIME,
            status TEXT,
            findings INTEGER
        )
    ''')
    
    # Create patch_status table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patch_status (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patch_id TEXT,
            asset_name TEXT,
            patch_name TEXT,
            status TEXT,
            deployment_date DATETIME,
            success_rate REAL,
            rollback_required BOOLEAN
        )
    ''')
    
    print("✅ Database schema created!")
    
    # Insert realistic sample data
    print("📊 Inserting sample security events...")
    
    # Sample security events
    sample_events = [
        ('EVT-001', 'Critical', 'Malware', '185.220.101.45', '192.168.1.100', 443, 'HTTPS', 'Active', 'T1566.001', 'Suspicious file download from known malicious domain', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Russia', 95),
        ('EVT-002', 'High', 'Phishing', '203.0.113.45', '192.168.1.50', 80, 'HTTP', 'Blocked', 'T1566.002', 'Malicious email attachment detected', 'Outlook/16.0', 'China', 87),
        ('EVT-003', 'Medium', 'DDoS', '198.51.100.10', '192.168.1.1', 80, 'HTTP', 'Mitigated', 'T1499', 'High volume requests detected', 'curl/7.68.0', 'Unknown', 65),
        ('EVT-004', 'Low', 'Port Scan', '203.0.113.100', '192.168.1.0', 22, 'SSH', 'Logged', 'T1046', 'Network reconnaissance attempt', 'nmap/7.80', 'USA', 45),
        ('EVT-005', 'Critical', 'Data Breach', '192.168.1.200', '10.0.0.10', 1433, 'SQL', 'Investigating', 'T1041', 'Unauthorized database access attempt', 'sqlmap/1.5.2', 'Internal', 0),
        ('EVT-006', 'High', 'Ransomware', '185.220.102.67', '192.168.1.150', 445, 'SMB', 'Contained', 'T1486', 'File encryption activity detected', 'Windows SMB Client', 'Russia', 98),
        ('EVT-007', 'Medium', 'Insider Threat', '192.168.1.75', '192.168.1.200', 3389, 'RDP', 'Monitoring', 'T1078', 'Unusual after-hours access', 'Remote Desktop', 'Internal', 0),
        ('EVT-008', 'Low', 'Policy Violation', '192.168.1.120', '8.8.8.8', 53, 'DNS', 'Warned', 'T1071.004', 'DNS tunneling attempt', 'dig/9.16.1', 'Internal', 0),
        ('EVT-009', 'Critical', 'APT Activity', '45.142.214.123', '192.168.1.10', 443, 'HTTPS', 'Active', 'T1055', 'Process injection detected', 'APT29 Toolset', 'Russia', 99),
        ('EVT-010', 'High', 'Credential Theft', '192.168.1.80', '192.168.1.5', 389, 'LDAP', 'Blocked', 'T1003', 'LDAP credential dumping attempt', 'Mimikatz', 'Internal', 0)
    ]
    
    for event in sample_events:
        cursor.execute('''
            INSERT OR IGNORE INTO security_events 
            (event_id, severity, event_type, source_ip, destination_ip, port, protocol, status, mitre_technique, description, user_agent, country, reputation_score)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', event)
    
    # Sample assets
    sample_assets = [
        ('Web Server', 'Server', '192.168.1.10', 85, datetime.now(), 3, 'Ubuntu 20.04', 'IT', 'High'),
        ('Database Server', 'Server', '192.168.1.20', 92, datetime.now(), 1, 'Windows Server 2019', 'IT', 'Critical'),
        ('Firewall', 'Security', '192.168.1.1', 45, datetime.now(), 0, 'pfSense', 'Security', 'Critical'),
        ('Workstation-01', 'Endpoint', '192.168.1.100', 67, datetime.now(), 5, 'Windows 10', 'Finance', 'Medium'),
        ('Domain Controller', 'Server', '192.168.1.5', 78, datetime.now(), 2, 'Windows Server 2019', 'IT', 'Critical'),
        ('Mail Server', 'Server', '192.168.1.25', 73, datetime.now(), 4, 'Exchange 2019', 'IT', 'High'),
        ('File Server', 'Server', '192.168.1.30', 69, datetime.now(), 3, 'Windows Server 2016', 'IT', 'Medium'),
        ('Print Server', 'Server', '192.168.1.35', 52, datetime.now(), 1, 'Ubuntu 18.04', 'IT', 'Low')
    ]
    
    for asset in sample_assets:
        cursor.execute('''
            INSERT OR IGNORE INTO assets 
            (asset_name, asset_type, ip_address, risk_score, last_seen, vulnerabilities, os_type, department, criticality)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', asset)
    
    # Sample compliance scores
    compliance_data = [
        ('NIST CSF', 94, datetime.now(), 'Compliant', 3),
        ('ISO 27001', 91, datetime.now(), 'Compliant', 5),
        ('SOC 2', 88, datetime.now(), 'Needs Improvement', 8),
        ('PCI DSS', 96, datetime.now(), 'Compliant', 2),
        ('GDPR', 89, datetime.now(), 'Compliant', 4),
        ('HIPAA', 93, datetime.now(), 'Compliant', 3)
    ]
    
    for compliance in compliance_data:
        cursor.execute('''
            INSERT OR IGNORE INTO compliance_scores 
            (framework, score, last_updated, status, findings)
            VALUES (?, ?, ?, ?, ?)
        ''', compliance)
    
    # Sample patch status
    patch_data = [
        ('PATCH-001', 'Web Server', 'Apache Security Update', 'Deployed', datetime.now() - timedelta(days=1), 100.0, False),
        ('PATCH-002', 'Database Server', 'Windows Critical Update', 'In Progress', datetime.now(), 75.0, False),
        ('PATCH-003', 'Workstation-01', 'Chrome Security Update', 'Failed', datetime.now() - timedelta(hours=2), 0.0, True),
        ('PATCH-004', 'Domain Controller', 'AD Security Patch', 'Pending', None, 0.0, False),
        ('PATCH-005', 'Mail Server', 'Exchange Update', 'Deployed', datetime.now() - timedelta(days=3), 100.0, False)
    ]
    
    for patch in patch_data:
        cursor.execute('''
            INSERT OR IGNORE INTO patch_status 
            (patch_id, asset_name, patch_name, status, deployment_date, success_rate, rollback_required)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', patch)
    
    conn.commit()
    conn.close()
    
    print("✅ Sample database created with realistic data!")
    print(f"📍 Database location: soc_data.db")
    print(f"📊 Events: {len(sample_events)}")
    print(f"🖥️  Assets: {len(sample_assets)}")
    print(f"📋 Compliance frameworks: {len(compliance_data)}")
    print(f"🔧 Patch records: {len(patch_data)}")

def test_api_connection(api_key, service='abuseipdb'):
    """Test API connection with a sample request"""
    
    print(f"🔗 Testing {service} API connection...")
    
    if service == 'abuseipdb':
        headers = {
            'Key': api_key,
            'Accept': 'application/json'
        }
        params = {
            'ipAddress': '8.8.8.8',  # Test with Google DNS
            'maxAgeInDays': 90,
            'verbose': ''
        }
        
        try:
            response = requests.get(
                'https://api.abuseipdb.com/api/v2/check',
                headers=headers,
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ {service} API working!")
                print(f"   Test IP: {data.get('ipAddress', 'N/A')}")
                print(f"   Abuse confidence: {data.get('abuseConfidencePercentage', 0)}%")
                return True
            else:
                print(f"❌ {service} API error: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ {service} API connection failed: {e}")
            return False
    
    return False

def create_sample_log_files():
    """Create sample log files for testing"""
    
    print("📄 Creating sample log files...")
    
    # JSON log file
    json_logs = [
        {
            "timestamp": "2024-01-09T10:15:30Z",
            "level": "ALERT",
            "source": "firewall",
            "message": "Blocked connection from 185.220.101.45",
            "src_ip": "185.220.101.45",
            "dst_ip": "192.168.1.100",
            "port": 443,
            "protocol": "TCP"
        },
        {
            "timestamp": "2024-01-09T10:16:45Z",
            "level": "WARNING",
            "source": "ids",
            "message": "Suspicious activity detected",
            "src_ip": "203.0.113.45",
            "dst_ip": "192.168.1.50",
            "port": 80,
            "protocol": "HTTP"
        },
        {
            "timestamp": "2024-01-09T10:17:20Z",
            "level": "INFO",
            "source": "proxy",
            "message": "Connection established",
            "src_ip": "192.168.1.25",
            "dst_ip": "8.8.8.8",
            "port": 53,
            "protocol": "DNS"
        }
    ]
    
    with open('sample_security.json', 'w') as f:
        for log in json_logs:
            f.write(json.dumps(log) + '\n')
    
    # CSV log file
    csv_content = """timestamp,severity,event_type,source_ip,destination_ip,status
2024-01-09 10:15:30,Critical,Malware,185.220.101.45,192.168.1.100,Blocked
2024-01-09 10:16:45,High,Phishing,203.0.113.45,192.168.1.50,Detected
2024-01-09 10:17:20,Medium,Scan,198.51.100.10,192.168.1.1,Logged
2024-01-09 10:18:10,Low,Normal,192.168.1.25,8.8.8.8,Allowed"""
    
    with open('sample_security.csv', 'w') as f:
        f.write(csv_content)
    
    print("✅ Sample log files created!")
    print("   📄 sample_security.json")
    print("   📄 sample_security.csv")

def main():
    """Main setup function"""
    
    print("🛡️ SOC Dashboard Real Data Setup")
    print("=" * 40)
    
    choice = input("\nWhat would you like to set up?\n1. Sample Database\n2. Test API Connection\n3. Create Sample Logs\n4. All of the above\n\nChoice (1-4): ")
    
    if choice in ['1', '4']:
        create_sample_database()
        print()
    
    if choice in ['2', '4']:
        service = input("API Service (abuseipdb/virustotal/otx): ").lower()
        if service in ['abuseipdb', 'virustotal', 'otx']:
            api_key = input(f"Enter your {service} API key: ").strip()
            if api_key:
                test_api_connection(api_key, service)
            else:
                print("❌ No API key provided")
        print()
    
    if choice in ['3', '4']:
        create_sample_log_files()
        print()
    
    print("🎉 Setup complete!")
    print("\nNext steps:")
    print("1. Run: streamlit run streamlit_soc_dashboard.py")
    print("2. Select 'Real Database' in the sidebar")
    print("3. Choose 'SQLite' and your data will load automatically!")

if __name__ == "__main__":
    main()
