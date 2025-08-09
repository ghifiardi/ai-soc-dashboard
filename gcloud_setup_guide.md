# Using gcloud CLI for BigQuery Authentication

## Perfect! You Have gcloud CLI Already Installed ✅

Since you have gcloud CLI, you can use **Application Default Credentials** - this is actually easier and more secure than JSON keys!

## Step-by-Step Setup (2 minutes)

### Step 1: Configure gcloud for Your Project
Open your terminal and run these commands:

```bash
# Set your project
gcloud config set project chronicle-dev-2be9

# Verify it's set correctly
gcloud config get-value project
```

You should see: `chronicle-dev-2be9`

### Step 2: Authenticate with Application Default Credentials
```bash
# This will open a browser for authentication
gcloud auth application-default login
```

**What happens:**
1. Browser opens automatically
2. Sign in with your Google account (the one with BigQuery access)
3. Grant permissions
4. Terminal shows "Credentials saved"

### Step 3: Verify Your Access
Test that you can access your BigQuery data:

```bash
# Test BigQuery access
bq query --use_legacy_sql=false \
"SELECT COUNT(*) as total_events FROM \`chronicle-dev-2be9.gatra_database.siem_events\` LIMIT 1"
```

If this works, you'll see your event count! 🎉

### Step 4: Configure Your SOC Dashboard

1. **Refresh your SOC dashboard**
2. **Select "BigQuery"** as data source
3. **Enter these settings**:
   ```
   Project ID: chronicle-dev-2be9
   Dataset: gatra_database
   Table: siem_events
   Authentication: Application Default Credentials
   Row Limit: 100
   Hours of Data: 24
   ```
4. **Click "Test BigQuery Connection"**

### Step 5: Success! 🚀

You should see:
- ✅ **"BigQuery connection successful!"**
- 📊 **"Table has X rows"** (your actual data count)
- 🔴 **"BigQuery"** labels on dashboard metrics

## Complete Commands Summary

Copy and paste these commands in your terminal:

```bash
# Configure project
gcloud config set project chronicle-dev-2be9

# Authenticate for application default credentials
gcloud auth application-default login

# Test access (optional)
bq query --use_legacy_sql=false "SELECT COUNT(*) FROM \`chronicle-dev-2be9.gatra_database.siem_events\`"
```

## Dashboard Configuration

```
✅ Data Source: BigQuery
✅ Project ID: chronicle-dev-2be9
✅ Dataset: gatra_database
✅ Table: siem_events
✅ Authentication: Application Default Credentials
✅ No JSON file needed!
```

## Advantages of This Method

- ✅ **No JSON keys to manage** - more secure
- ✅ **Uses your existing Google account** permissions
- ✅ **Easier to set up** - just a few commands
- ✅ **Automatically refreshes** credentials
- ✅ **Works immediately** with your dashboard

## Troubleshooting

### If `gcloud config set project` fails:
```bash
# First authenticate with gcloud
gcloud auth login
# Then set project
gcloud config set project chronicle-dev-2be9
```

### If `gcloud auth application-default login` fails:
- Make sure you're signed in: `gcloud auth list`
- Try: `gcloud auth login` first
- Then retry the application-default command

### If BigQuery test fails:
- Check you have BigQuery permissions in the project
- Verify the table exists: `bq ls chronicle-dev-2be9:gatra_database`

### If dashboard connection fails:
- Make sure you selected "Application Default Credentials"
- Verify gcloud is configured for the right project
- Try refreshing the dashboard page

## What Happens Next

Once connected, your SOC dashboard will:
- 🔴 Show **"BigQuery"** instead of **"Mock"** on all metrics
- 📊 Display **real SIEM events** from your `gatra_database.siem_events` table
- ⚡ **Auto-refresh** with live data every 10 seconds (if enabled)
- 📈 Show **actual security metrics** from your data

This is the **easiest and most secure** way to connect! No JSON files needed. 🎯
