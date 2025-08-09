-- BigQuery Setup for SOC Dashboard
-- Project: chronicle-dev-2be9
-- Run these queries in your BigQuery console

-- Step 1: Create the security_logs dataset
CREATE SCHEMA IF NOT EXISTS `chronicle-dev-2be9.security_logs`
OPTIONS (
  description = "Security Operations Center data for SOC Dashboard",
  location = "US"
);

-- Step 2: Create the security_events table
CREATE TABLE IF NOT EXISTS `chronicle-dev-2be9.security_logs.security_events` (
  timestamp TIMESTAMP NOT NULL,
  event_id STRING NOT NULL,
  severity STRING NOT NULL,
  event_type STRING NOT NULL,
  source_ip STRING,
  destination_ip STRING,
  port INT64,
  protocol STRING,
  status STRING NOT NULL,
  mitre_technique STRING,
  description STRING,
  user_agent STRING,
  country STRING,
  reputation_score INT64,
  asset_name STRING,
  department STRING,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(timestamp)
CLUSTER BY severity, event_type
OPTIONS (
  description = "Security events for SOC monitoring and analysis"
);

-- Step 3: Insert sample security events data
INSERT INTO `chronicle-dev-2be9.security_logs.security_events` 
(timestamp, event_id, severity, event_type, source_ip, destination_ip, port, protocol, status, mitre_technique, description, user_agent, country, reputation_score, asset_name, department) 
VALUES
  -- Critical Events
  (TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 5 MINUTE), 'EVT-001', 'Critical', 'Malware', '185.220.101.45', '192.168.1.100', 443, 'HTTPS', 'Active', 'T1566.001', 'Suspicious file download from known malicious domain', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Russia', 95, 'Web Server', 'IT'),
  
  (TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 15 MINUTE), 'EVT-002', 'Critical', 'Ransomware', '45.142.214.123', '192.168.1.150', 445, 'SMB', 'Contained', 'T1486', 'File encryption activity detected - Lockbit indicators', 'Windows SMB Client', 'Russia', 98, 'File Server', 'Finance'),
  
  (TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 25 MINUTE), 'EVT-003', 'Critical', 'APT Activity', '203.0.113.89', '192.168.1.10', 443, 'HTTPS', 'Investigating', 'T1055', 'Process injection detected - APT29 toolset identified', 'APT29 Custom Tool', 'Unknown', 99, 'Domain Controller', 'IT'),
  
  -- High Priority Events  
  (TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 35 MINUTE), 'EVT-004', 'High', 'Phishing', '203.0.113.45', '192.168.1.50', 80, 'HTTP', 'Blocked', 'T1566.002', 'Malicious email attachment detected by sandbox', 'Outlook/16.0', 'China', 87, 'Mail Server', 'HR'),
  
  (TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 45 MINUTE), 'EVT-005', 'High', 'Data Breach', '192.168.1.200', '10.0.0.10', 1433, 'SQL', 'Monitoring', 'T1041', 'Unauthorized database access attempt - sensitive data queried', 'sqlmap/1.5.2', 'Internal', 0, 'Database Server', 'Finance'),
  
  (TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 55 MINUTE), 'EVT-006', 'High', 'Credential Theft', '192.168.1.80', '192.168.1.5', 389, 'LDAP', 'Blocked', 'T1003', 'LDAP credential dumping attempt detected', 'Mimikatz', 'Internal', 0, 'Domain Controller', 'IT'),
  
  -- Medium Priority Events
  (TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 65 MINUTE), 'EVT-007', 'Medium', 'DDoS', '198.51.100.10', '192.168.1.1', 80, 'HTTP', 'Mitigated', 'T1499', 'High volume requests detected - 10k req/min', 'curl/7.68.0', 'Unknown', 65, 'Firewall', 'Security'),
  
  (TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 75 MINUTE), 'EVT-008', 'Medium', 'Insider Threat', '192.168.1.75', '192.168.1.200', 3389, 'RDP', 'Monitoring', 'T1078', 'Unusual after-hours access from terminated employee account', 'Remote Desktop', 'Internal', 0, 'Workstation', 'Finance'),
  
  (TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 85 MINUTE), 'EVT-009', 'Medium', 'Policy Violation', '192.168.1.120', '8.8.8.8', 53, 'DNS', 'Warned', 'T1071.004', 'DNS tunneling attempt detected', 'dig/9.16.1', 'Internal', 0, 'Workstation', 'Engineering'),
  
  -- Low Priority Events
  (TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 95 MINUTE), 'EVT-010', 'Low', 'Port Scan', '203.0.113.100', '192.168.1.0', 22, 'SSH', 'Logged', 'T1046', 'Network reconnaissance attempt - port scanning detected', 'nmap/7.80', 'USA', 45, 'Network Scanner', 'External'),
  
  (TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 105 MINUTE), 'EVT-011', 'Low', 'Failed Login', '192.168.1.25', '192.168.1.5', 389, 'LDAP', 'Logged', 'T1110', 'Multiple failed login attempts - possible brute force', 'Windows Logon', 'Internal', 0, 'Domain Controller', 'IT'),
  
  (TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 115 MINUTE), 'EVT-012', 'Low', 'Suspicious Traffic', '192.168.1.90', '185.199.108.153', 443, 'HTTPS', 'Allowed', 'T1071.001', 'High frequency HTTPS requests to GitHub - possible data exfiltration', 'git/2.34.1', 'Internal', 0, 'Developer Workstation', 'Engineering');

-- Step 4: Create a view for recent events (last 24 hours)
CREATE VIEW IF NOT EXISTS `chronicle-dev-2be9.security_logs.recent_events` AS
SELECT *
FROM `chronicle-dev-2be9.security_logs.security_events`
WHERE timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 24 HOUR)
ORDER BY timestamp DESC;

-- Step 5: Create a view for critical events
CREATE VIEW IF NOT EXISTS `chronicle-dev-2be9.security_logs.critical_events` AS
SELECT *
FROM `chronicle-dev-2be9.security_logs.security_events`
WHERE severity IN ('Critical', 'High')
  AND timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
ORDER BY timestamp DESC;

-- Step 6: Verify the setup
SELECT 
  'Data Setup Complete' as status,
  COUNT(*) as total_events,
  COUNTIF(severity = 'Critical') as critical_events,
  COUNTIF(severity = 'High') as high_events,
  COUNTIF(severity = 'Medium') as medium_events,
  COUNTIF(severity = 'Low') as low_events,
  COUNT(DISTINCT source_ip) as unique_sources,
  MIN(timestamp) as earliest_event,
  MAX(timestamp) as latest_event
FROM `chronicle-dev-2be9.security_logs.security_events`;
