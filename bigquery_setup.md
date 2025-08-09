# BigQuery Setup Guide for SOC Dashboard

This guide will help you connect your SOC dashboard to Google BigQuery for real-time security data analysis.

## Prerequisites

1. **Google Cloud Project** with BigQuery enabled
2. **Service Account** with BigQuery permissions
3. **Security data** in BigQuery tables

## Step 1: Create a Service Account

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Navigate to **IAM & Admin > Service Accounts**
3. Click **Create Service Account**
4. Name: `soc-dashboard-reader`
5. Grant these roles:
   - `BigQuery Data Viewer`
   - `BigQuery Job User`
6. Create and download the JSON key file

## Step 2: Prepare Your BigQuery Table

Your security events table should have these columns (flexible schema):

### Required Columns:
```sql
CREATE TABLE `your-project.security_logs.security_events` (
  timestamp TIMESTAMP,
  event_id STRING,
  severity STRING,
  event_type STRING,
  source_ip STRING,
  destination_ip STRING,
  status STRING,
  description STRING
);
```

### Optional Columns (for enhanced features):
```sql
ALTER TABLE `your-project.security_logs.security_events`
ADD COLUMN mitre_technique STRING,
ADD COLUMN user_agent STRING,
ADD COLUMN country STRING,
ADD COLUMN reputation_score INT64;
```

## Step 3: Sample Data Insert

```sql
INSERT INTO `your-project.security_logs.security_events` VALUES
  (CURRENT_TIMESTAMP(), 'EVT-001', 'Critical', 'Malware', '185.220.101.45', '192.168.1.100', 'Active', 'Suspicious file download'),
  (CURRENT_TIMESTAMP(), 'EVT-002', 'High', 'Phishing', '203.0.113.45', '192.168.1.50', 'Blocked', 'Malicious email detected'),
  (CURRENT_TIMESTAMP(), 'EVT-003', 'Medium', 'DDoS', '198.51.100.10', '192.168.1.1', 'Mitigated', 'High volume requests');
```

## Step 4: Configure Dashboard

1. **Select "BigQuery"** in the dashboard sidebar
2. **Enter your details**:
   - Project ID: `your-google-cloud-project`
   - Dataset: `security_logs`
   - Table: `security_events`
3. **Upload Service Account Key**: Upload the JSON file you downloaded
4. **Test Connection**: Click the test button to verify

## Step 5: Advanced Queries

The dashboard uses these BigQuery queries:

### Security Events Query:
```sql
SELECT *
FROM `project.dataset.table`
WHERE timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 24 HOUR)
ORDER BY timestamp DESC
LIMIT 100
```

### Metrics Query:
```sql
SELECT 
    COUNT(*) as total_events,
    COUNTIF(severity = 'Critical') as critical_events,
    COUNTIF(severity = 'High') as high_events,
    COUNT(DISTINCT source_ip) as unique_sources
FROM `project.dataset.table`
WHERE timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 24 HOUR)
```

## Troubleshooting

### Common Issues:

1. **"Permission denied"**
   - Ensure service account has `BigQuery Data Viewer` role
   - Check that the table exists and is accessible

2. **"Table not found"**
   - Verify project ID, dataset, and table names
   - Ensure the table exists in BigQuery

3. **"Authentication failed"**
   - Re-download service account JSON
   - Check JSON file format is valid

4. **"No data returned"**
   - Check if your table has data
   - Adjust the time range (hours of data)

### Performance Tips:

1. **Partition your table** by timestamp for better performance
2. **Use clustering** on frequently queried columns (severity, event_type)
3. **Set appropriate row limits** (100-1000 for dashboards)
4. **Consider materialized views** for complex aggregations

## Example BigQuery Schema

```sql
CREATE TABLE `your-project.security_logs.security_events` (
  timestamp TIMESTAMP NOT NULL,
  event_id STRING NOT NULL,
  severity STRING NOT NULL,
  event_type STRING,
  source_ip STRING,
  destination_ip STRING,
  port INT64,
  protocol STRING,
  status STRING,
  mitre_technique STRING,
  description STRING,
  user_agent STRING,
  country STRING,
  reputation_score INT64,
  asset_name STRING,
  department STRING
)
PARTITION BY DATE(timestamp)
CLUSTER BY severity, event_type;
```

## Cost Optimization

1. **Use partitioning** to reduce query costs
2. **Limit time ranges** (24-48 hours for real-time dashboards)
3. **Set row limits** appropriately
4. **Use BigQuery slots** for predictable pricing
5. **Monitor query costs** in the BigQuery console

## Security Best Practices

1. **Use service accounts** instead of user credentials
2. **Grant minimal permissions** (Data Viewer only)
3. **Rotate service account keys** regularly
4. **Store keys securely** (never commit to git)
5. **Use VPC Service Controls** for additional security

## Next Steps

Once connected, your dashboard will show:
- ✅ Real-time security events from BigQuery
- ✅ Live metrics and counts
- ✅ Automatic data refresh
- ✅ Historical trend analysis

For advanced features, consider:
- Setting up **BigQuery ML** for anomaly detection
- Creating **scheduled queries** for data aggregation
- Implementing **real-time streaming** with Pub/Sub
- Adding **custom threat intelligence** enrichment
