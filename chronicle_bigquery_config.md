# Chronicle BigQuery Configuration for SOC Dashboard

## Your BigQuery Setup

**Project ID**: `chronicle-dev-2be9`  
**Dataset**: `gatra_database`  
**Table**: `siem_events`

## Quick Setup Steps

### 1. Run the SQL Setup Script

1. In your BigQuery console, click **"SQL query"**
2. Copy and paste the contents of `setup_bigquery_for_soc.sql`
3. Click **"Run"** to execute all queries

This will create:
- ✅ Dataset: `security_logs`
- ✅ Table: `security_events` with proper schema
- ✅ 12 sample security events (Critical, High, Medium, Low)
- ✅ Views for recent and critical events
- ✅ Partitioning and clustering for performance

### 2. Create Service Account

1. Go to [IAM & Admin > Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts?project=chronicle-dev-2be9)
2. Click **"Create Service Account"**
3. Name: `soc-dashboard-reader`
4. Grant roles:
   - `BigQuery Data Viewer`
   - `BigQuery Job User`
5. Create and download JSON key

### 3. Configure Dashboard

In your SOC dashboard sidebar:

```
Data Source: BigQuery
Project ID: chronicle-dev-2be9
Dataset: gatra_database
Table: siem_events
Authentication: Service Account JSON (upload the key file)
```

## Expected Results

Once connected, you'll see:
- **12 security events** from the last 2 hours
- **3 Critical alerts** (Malware, Ransomware, APT)
- **3 High priority** events (Phishing, Data Breach, Credential Theft)
- **Real-time metrics** from your BigQuery data

## Sample Queries for Testing

### Test Connection:
```sql
SELECT COUNT(*) as total_events
FROM `chronicle-dev-2be9.gatra_database.siem_events`
```

### View Recent Events:
```sql
SELECT *
FROM `chronicle-dev-2be9.gatra_database.siem_events`
ORDER BY timestamp DESC
LIMIT 10
```

### Get Metrics (what the dashboard uses):
```sql
SELECT 
    COUNT(*) as total_events,
    COUNT(DISTINCT source_ip) as unique_sources
FROM `chronicle-dev-2be9.gatra_database.siem_events`
WHERE timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 24 HOUR)
```

## Troubleshooting

### If you get "Dataset not found":
- Make sure you ran the SQL setup script completely
- Check that `security_logs` dataset exists in your project

### If you get "Permission denied":
- Verify your service account has `BigQuery Data Viewer` role
- Make sure you're using the correct project ID: `chronicle-dev-2be9`

### If you see "No data":
- Run the sample data insert queries again
- Check the timestamp range (events are created in the last 2 hours)

## Adding More Data

To add more realistic events, you can:

1. **Insert new events**:
```sql
INSERT INTO `chronicle-dev-2be9.security_logs.security_events` 
(timestamp, event_id, severity, event_type, source_ip, destination_ip, status, description)
VALUES 
(CURRENT_TIMESTAMP(), 'EVT-NEW', 'Critical', 'Zero Day', '1.2.3.4', '192.168.1.10', 'Active', 'New threat detected');
```

2. **Import from CSV** using BigQuery's data import feature

3. **Connect real security tools** (Chronicle, Splunk, etc.) to stream data

## Dashboard Configuration Summary

```
✅ Project ID: chronicle-dev-2be9
✅ Dataset: gatra_database  
✅ Table: siem_events
✅ Using your existing SIEM data
✅ Time Range: Configurable (1-168 hours)
✅ Authentication: Service Account JSON required
```

Your BigQuery is now ready for the SOC dashboard! 🚀
