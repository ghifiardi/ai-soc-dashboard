# Gatra Database Configuration for SOC Dashboard

## Your Existing BigQuery Setup

**Project ID**: `chronicle-dev-2be9`  
**Dataset**: `gatra_database`  
**Table**: `siem_events`

## Quick Setup Steps

### 1. Check Your Table Schema First

Before configuring the dashboard, run this query in BigQuery to see your table structure:

```sql
SELECT column_name, data_type, is_nullable
FROM `chronicle-dev-2be9.gatra_database.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'siem_events'
ORDER BY ordinal_position;
```

### 2. Create Service Account (if not already done)

1. Go to [IAM & Admin > Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts?project=chronicle-dev-2be9)
2. Click **"Create Service Account"**
3. Name: `soc-dashboard-reader`
4. Grant roles:
   - `BigQuery Data Viewer`
   - `BigQuery Job User`
5. Create and download JSON key

### 3. Configure SOC Dashboard

In your SOC dashboard sidebar:

```
Data Source: BigQuery
Project ID: chronicle-dev-2be9
Dataset: gatra_database
Table: siem_events
Authentication: Service Account JSON (upload the key file)
Row Limit: 100 (adjust as needed)
Hours of Data: 24 (adjust as needed)
```

### 4. Test Connection

Click **"Test BigQuery Connection"** in the dashboard sidebar. This will:
- Verify authentication
- Check table access
- Show row count
- Confirm the connection works

## Expected Results

The dashboard will automatically adapt to your existing `siem_events` table structure. It will:

✅ **Display all your SIEM data** in the events table  
✅ **Show real metrics** based on your actual data  
✅ **Work with any column names** your table has  
✅ **Handle different data types** automatically  

## Flexible Schema Support

The dashboard is designed to work with various SIEM table schemas. It will look for common columns like:

- `timestamp` (or similar time fields)
- `severity`, `priority`, `level` (for event classification)
- `source_ip`, `src_ip` (source addresses)
- `event_type`, `alert_type` (event categories)
- `status` (event status)

If your columns have different names, the dashboard will still display the data in a table format.

## Sample Queries for Your Data

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

### Get Data Range:
```sql
SELECT 
    COUNT(*) as total_events,
    MIN(timestamp) as earliest_event,
    MAX(timestamp) as latest_event,
    COUNT(DISTINCT DATE(timestamp)) as days_of_data
FROM `chronicle-dev-2be9.gatra_database.siem_events`
```

## Troubleshooting

### If you get "Table not found":
- Verify the table name is exactly `siem_events`
- Check that you have access to the `gatra_database` dataset

### If you get "Permission denied":
- Ensure your service account has `BigQuery Data Viewer` role
- Make sure you're using the correct project ID: `chronicle-dev-2be9`

### If you see "No data":
- Check if your table has recent data (last 24 hours)
- Adjust the "Hours of Data" setting in the dashboard
- Verify your table has a timestamp column

## Advanced Configuration

Once connected, you can:

1. **Adjust time ranges** (1-168 hours)
2. **Set row limits** (10-10,000 rows)
3. **Enable auto-refresh** for live updates
4. **View all dashboard sections** with your real data

## Dashboard Configuration Summary

```
✅ Project ID: chronicle-dev-2be9
✅ Dataset: gatra_database
✅ Table: siem_events
✅ Schema: Flexible - adapts to your existing structure
✅ Data: Your real SIEM events
✅ Authentication: Service Account JSON required
```

Your existing SIEM data in BigQuery is now ready for the SOC dashboard! 🚀

## Next Steps

1. **Run the schema check** query to see your table structure
2. **Create the service account** and download the JSON key
3. **Configure the dashboard** with your credentials
4. **Test the connection** and start monitoring your real SIEM data

The dashboard will work with whatever data structure you have in your `siem_events` table!
