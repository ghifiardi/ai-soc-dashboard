# Using Your Existing Service Account Key

## Great News! You Already Have a Key! ✅

**Service Account**: `gatra-user-bigquery`  
**Key ID**: `a94f1fb2b9808f1fcaaa5541cef77534ca687016`  
**Status**: ✅ **Active**  
**Valid Until**: June 24, 2026

## How to Get the JSON File for Your Existing Key

Since you can't create new keys, you need to get the JSON file for your existing key. Here are your options:

### Option 1: Ask Your Administrator
1. **Contact your Google Cloud administrator**
2. **Show them this key ID**: `a94f1fb2b9808f1fcaaa5541cef77534ca687016`
3. **Ask them to provide the JSON file** for this existing key
4. **They should have the original JSON file** from when the key was created

### Option 2: Use Application Default Credentials (ADC)
If you have `gcloud` CLI access, you can use this method instead:

1. **Install gcloud CLI** (if not already installed)
2. **Authenticate with your user account**:
   ```bash
   gcloud auth login
   gcloud config set project chronicle-dev-2be9
   gcloud auth application-default login
   ```
3. **In your SOC dashboard**, select:
   - Authentication: **"Application Default Credentials"**
   - Project ID: `chronicle-dev-2be9`
   - Dataset: `gatra_database`
   - Table: `siem_events`

### Option 3: Request Key Download Permission
Ask your administrator to temporarily grant you:
- **Service Account Admin** role
- Or **Service Account Key Admin** role

Then you can download the JSON file yourself.

## Dashboard Configuration

### If You Get the JSON File:
```
Data Source: BigQuery
Project ID: chronicle-dev-2be9
Dataset: gatra_database
Table: siem_events
Authentication: Service Account JSON
Upload: [Your JSON file]
```

### If You Use Application Default Credentials:
```
Data Source: BigQuery
Project ID: chronicle-dev-2be9
Dataset: gatra_database
Table: siem_events
Authentication: Application Default Credentials
```

## Verify Your Service Account Permissions

Make sure your service account `gatra-user-bigquery` has these roles:
- ✅ **BigQuery Data Viewer**
- ✅ **BigQuery Job User**

You can check this in **IAM & Admin > IAM** and search for `gatra-user-bigquery`.

## Test Query

Once configured, test with this query in BigQuery:
```sql
SELECT COUNT(*) as total_events
FROM `chronicle-dev-2be9.gatra_database.siem_events`
LIMIT 1
```

## Next Steps

1. **Choose your authentication method** (JSON file or ADC)
2. **Configure your SOC dashboard** with the settings above
3. **Test the BigQuery connection**
4. **Start viewing your real SIEM data!** 🚀

## Troubleshooting

### If you get "Permission denied":
- Verify `gatra-user-bigquery` has BigQuery permissions
- Check that you're using the correct project: `chronicle-dev-2be9`

### If you get "Authentication failed":
- Try the Application Default Credentials method
- Ask your admin for the JSON file for key `a94f1fb2b9808f1fcaaa5541cef77534ca687016`

### If you get "Table not found":
- Confirm `gatra_database.siem_events` exists
- Check table permissions for the service account

Your existing key is perfect for connecting to BigQuery - you just need to get it in the right format! 🎯
