# How to Download JSON Key File - Step by Step

## Your Service Account
**ID**: `a94f1fb2b9808f1fcaaa5541cef77534ca687016`  
**Project**: `chronicle-dev-2be9`

## Step-by-Step Instructions

### Step 1: Go to Google Cloud Console
1. Open your browser
2. Go to: https://console.cloud.google.com
3. Make sure you're in the **chronicle-dev-2be9** project (check top bar)

### Step 2: Navigate to Service Accounts
1. Click the **hamburger menu** (≡) on the top left
2. Go to **IAM & Admin**
3. Click **Service Accounts**

**Direct link**: https://console.cloud.google.com/iam-admin/serviceaccounts?project=chronicle-dev-2be9

### Step 3: Find Your Service Account
Look for the service account that ends with: **...ca687016**
- The full ID is: `a94f1fb2b9808f1fcaaa5541cef77534ca687016`
- It might show a shorter version or email format

### Step 4: Access the Service Account
1. **Click on the service account name** (the one ending in ca687016)
2. This opens the service account details page

### Step 5: Go to Keys Tab
1. You'll see several tabs: **DETAILS**, **PERMISSIONS**, **KEYS**
2. **Click on the "KEYS" tab**

### Step 6: Create New Key
1. Click the **"ADD KEY"** button
2. Select **"Create new key"** from the dropdown

### Step 7: Choose JSON Format
1. A dialog box appears asking for key type
2. **Select "JSON"** (this is very important!)
3. **DO NOT** select P12 - only JSON works with the dashboard

### Step 8: Download
1. Click **"CREATE"**
2. The JSON file will **automatically download** to your computer
3. The file name will look like: `chronicle-dev-2be9-a94f1fb2b9808f1f.json`

### Step 9: Verify the File
Open the downloaded file in a text editor. It should start like this:
```json
{
  "type": "service_account",
  "project_id": "chronicle-dev-2be9",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...",
  "client_email": "...@chronicle-dev-2be9.iam.gserviceaccount.com",
  ...
}
```

## Common Issues & Solutions

### Issue: "I can't find my service account"
**Solution**: 
- Make sure you're in the **chronicle-dev-2be9** project
- Look for the service account ending in **ca687016**
- Check if it's on the next page (if you have many service accounts)

### Issue: "ADD KEY button is grayed out"
**Solution**:
- You need **Service Account Admin** or **Editor** role
- Ask your administrator to give you permissions
- Or ask them to create the key for you

### Issue: "Downloaded file is .p12 format"
**Solution**:
- Delete the .p12 file
- Go back and select **JSON** format (not P12)
- Create a new key

### Issue: "File downloaded but won't open"
**Solution**:
- The file should be a .json file
- Open with any text editor (Notepad, TextEdit, VS Code)
- Should contain readable JSON text, not binary data

## Security Warning ⚠️
- **Keep this file secure** - it's like a password
- **Don't share it** with anyone
- **Don't upload it** to public repositories
- **Store it safely** on your computer

## Next Steps After Download

1. **Go to your SOC dashboard**
2. **Select "BigQuery"** as data source
3. **Enter your settings**:
   - Project ID: `chronicle-dev-2be9`
   - Dataset: `gatra_database`
   - Table: `siem_events`
4. **Upload the JSON file** you just downloaded
5. **Test the connection**

## Quick Checklist ✅

- [ ] Opened Google Cloud Console
- [ ] Navigated to Service Accounts
- [ ] Found service account ending in ca687016
- [ ] Clicked on the service account
- [ ] Went to KEYS tab
- [ ] Clicked ADD KEY → Create new key
- [ ] Selected JSON format (not P12)
- [ ] Clicked CREATE
- [ ] File downloaded automatically
- [ ] Verified file starts with {"type": "service_account"...}

Once you have the JSON file, you're ready to connect your dashboard to BigQuery! 🚀
