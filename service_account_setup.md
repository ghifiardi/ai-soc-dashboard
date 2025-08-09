# Service Account Setup for SOC Dashboard

## Your Service Account

**Service Account ID**: `a94f1fb2b9808f1fcaaa5541cef77534ca687016`  
**Project**: `chronicle-dev-2be9`

## Steps to Get JSON Key File

### 1. Go to Service Account in Google Cloud Console

1. Open [Google Cloud Console](https://console.cloud.google.com)
2. Navigate to **IAM & Admin > Service Accounts**
3. Select project: `chronicle-dev-2be9`
4. Find your service account with ID: `a94f1fb2b9808f1fcaaa5541cef77534ca687016`

### 2. Download JSON Key

1. Click on the service account (the one ending in `...ca687016`)
2. Go to the **"Keys"** tab
3. Click **"Add Key" > "Create new key"**
4. Select **"JSON"** format
5. Click **"Create"**
6. The JSON file will download automatically

### 3. Verify Permissions

Make sure your service account has these roles:
- ✅ **BigQuery Data Viewer**
- ✅ **BigQuery Job User**

If not, add them:
1. Go to **IAM & Admin > IAM**
2. Find your service account
3. Click **Edit** (pencil icon)
4. **Add Role** > Search for "BigQuery Data Viewer"
5. **Add Role** > Search for "BigQuery Job User"
6. Click **Save**

### 4. Configure SOC Dashboard

1. **Refresh your SOC dashboard**
2. **Select "BigQuery"** as data source
3. **Enter your settings**:
   ```
   Project ID: chronicle-dev-2be9
   Dataset: gatra_database
   Table: siem_events
   Authentication: Service Account JSON
   ```
4. **Upload the JSON key file** you just downloaded
5. **Click "Test BigQuery Connection"**

### 5. Expected Success Message

You should see:
- ✅ **"Service account key uploaded"**
- ✅ **"BigQuery connection successful!"**
- 📊 **"Table has X rows"** (showing your data count)

## Troubleshooting

### If you get "Service account not found":
- Double-check the service account ID: `a94f1fb2b9808f1fcaaa5541cef77534ca687016`
- Make sure you're in the correct project: `chronicle-dev-2be9`

### If you get "Permission denied":
- Verify the service account has `BigQuery Data Viewer` role
- Check that `BigQuery Job User` role is also assigned
- Make sure the service account is enabled (not disabled)

### If you get "Table not found":
- Confirm the dataset `gatra_database` exists
- Verify the table `siem_events` is in that dataset
- Check you have read access to the table

### If JSON upload fails:
- Make sure you downloaded the key in **JSON format** (not P12)
- The file should start with `{"type": "service_account"...}`
- Try downloading a new key if the current one doesn't work

## Security Best Practices

1. **Keep the JSON key secure** - don't share it or commit to git
2. **Use minimal permissions** - only BigQuery Data Viewer and Job User
3. **Rotate keys regularly** - create new keys periodically
4. **Monitor usage** - check BigQuery audit logs

## Quick Test Queries

Once connected, you can test with these queries in BigQuery:

```sql
-- Test basic access
SELECT COUNT(*) as total_events
FROM `chronicle-dev-2be9.gatra_database.siem_events`;

-- Check recent data
SELECT *
FROM `chronicle-dev-2be9.gatra_database.siem_events`
ORDER BY timestamp DESC
LIMIT 5;
```

## Dashboard Configuration Summary

```
✅ Project: chronicle-dev-2be9
✅ Dataset: gatra_database
✅ Table: siem_events
✅ Service Account: a94f1fb2b9808f1fcaaa5541cef77534ca687016
✅ Authentication: JSON key file (download required)
✅ Permissions: BigQuery Data Viewer + Job User
```

Once you upload the JSON key, your SOC dashboard will connect to your real SIEM data in BigQuery! 🚀
