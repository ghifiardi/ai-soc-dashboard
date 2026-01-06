# Executive Dashboard Setup Guide
## React Frontend + FastAPI Backend + BigQuery Integration

Complete guide to set up the Executive Dashboard with real-time data from your BigQuery database.

---

## 🎯 Overview

Your setup will have **3 components**:

1. **BigQuery** (Google Cloud) - Data source with `gatra_database`
2. **FastAPI Backend** (Python) - Fetches data from BigQuery, serves REST API
3. **React Frontend** (JavaScript) - Beautiful dashboard UI

```
BigQuery (chronicle-dev-2be9) → FastAPI Backend (port 8000) → React Dashboard (port 3001)
```

---

## 📋 Prerequisites

✅ Python 3.10+
✅ Node.js 18+
✅ Google Cloud service account with BigQuery access
✅ Service account JSON key file

---

## 🚀 Quick Start (3 Steps)

### Step 1: Set Up FastAPI Backend

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env

# Edit .env file with your settings:
# - Set GCP_PROJECT_ID=chronicle-dev-2be9
# - Set BIGQUERY_DATASET=gatra_database
# - Set GOOGLE_APPLICATION_CREDENTIALS=/path/to/your-key.json

# Start the backend server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

✅ Backend running at **http://localhost:8000**
✅ API docs available at **http://localhost:8000/docs**

### Step 2: Set Up React Frontend

```bash
# Navigate to React directory
cd react-executive-dashboard

# Install Node dependencies
npm install

# Configure environment (optional)
cp .env.example .env
# Edit .env if needed: VITE_API_BASE_URL=http://localhost:8000

# Start the development server
npm run dev
```

✅ Dashboard running at **http://localhost:3001**

### Step 3: Verify Integration

1. Open **http://localhost:3001** in your browser
2. Look for the **● LIVE DATA** badge (green) in the subtitle
   - Green "LIVE DATA" = Connected to BigQuery via API ✅
   - Orange "DEMO MODE" = Using mock data (API unavailable) ⚠️

---

## 🔧 Detailed Configuration

### Backend Configuration (.env)

```env
# Google Cloud Platform
GCP_PROJECT_ID=chronicle-dev-2be9
BIGQUERY_DATASET=gatra_database
GOOGLE_APPLICATION_CREDENTIALS=/Users/you/path/to/service-account-key.json

# API Settings
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=http://localhost:3001,http://localhost:3000

# Environment
ENVIRONMENT=development
```

### Frontend Configuration (.env - Optional)

```env
# FastAPI Backend URL
VITE_API_BASE_URL=http://localhost:8000
```

---

## 📊 BigQuery Schema Requirements

The backend expects these tables in your `gatra_database`:

### Table: `activity_logs`
```sql
CREATE TABLE gatra_database.activity_logs (
  timestamp TIMESTAMP,
  severity STRING,        -- 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW'
  status STRING,          -- 'RESOLVED', 'IN_PROGRESS', 'OPEN'
  detection_time TIMESTAMP,
  response_time TIMESTAMP,
  is_false_positive BOOLEAN
);
```

### Table: `agent_metrics`
```sql
CREATE TABLE gatra_database.agent_metrics (
  timestamp TIMESTAMP,
  detection_time_minutes FLOAT64,
  response_time_minutes FLOAT64,
  resolution_time_minutes FLOAT64,
  security_score INT64    -- 0-100
);
```

**Note:** If tables have different schemas, the API will gracefully fall back to mock data.

---

## 🔐 Service Account Setup

### Option 1: Use Existing Key

If you already have a service account key:

1. Locate your `chronicle-key.json` or similar file
2. Update `GOOGLE_APPLICATION_CREDENTIALS` in backend `.env`
3. Restart the backend

### Option 2: Create New Service Account

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to **IAM & Admin** > **Service Accounts**
3. Click **Create Service Account**
4. Grant roles:
   - `BigQuery Data Viewer`
   - `BigQuery Job User`
5. Create and download JSON key
6. Save to secure location (e.g., `~/gcp-keys/chronicle-key.json`)
7. Update backend `.env` with the path

---

## 🧪 Testing the Setup

### Test 1: Backend Health Check

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2026-01-06T..."
}
```

### Test 2: Fetch Dashboard Data

```bash
curl http://localhost:8000/api/executive/dashboard?days=30
```

Should return JSON with metrics, trends, severity data, etc.

### Test 3: Frontend Integration

1. Open **http://localhost:3001**
2. Open browser DevTools (F12) → Network tab
3. Refresh the page
4. Look for request to `http://localhost:8000/api/executive/dashboard`
5. Check response status is **200 OK**

---

## 🚨 Troubleshooting

### Issue: "DEMO MODE" instead of "LIVE DATA"

**Causes:**
- Backend not running
- Backend can't connect to BigQuery
- CORS errors

**Solutions:**
1. Verify backend is running on port 8000
2. Check backend logs for errors
3. Verify service account permissions
4. Check `.env` configuration

### Issue: Backend shows BigQuery errors

**Solutions:**
1. Verify `GCP_PROJECT_ID` is correct: `chronicle-dev-2be9`
2. Check service account key path is correct
3. Ensure tables exist: `activity_logs`, `agent_metrics`
4. Verify IAM permissions (BigQuery Data Viewer + Job User)

### Issue: CORS errors in browser console

**Solution:**
Add React app URL to backend `.env`:
```env
CORS_ORIGINS=http://localhost:3001,http://localhost:3000
```

### Issue: "Module not found" errors

**Backend:**
```bash
cd backend
pip install -r requirements.txt --force-reinstall
```

**Frontend:**
```bash
cd react-executive-dashboard
rm -rf node_modules package-lock.json
npm install
```

---

## 📁 Project Structure

```
ai-soc-dashboard/
├── backend/                          # FastAPI Backend
│   ├── app/
│   │   ├── api/executive.py         # API endpoints
│   │   ├── services/
│   │   │   ├── bigquery_service.py  # BigQuery integration
│   │   │   └── data_transformer.py  # Data transformation
│   │   ├── models/executive_metrics.py  # Pydantic models
│   │   ├── config/settings.py       # Configuration
│   │   └── main.py                  # FastAPI app
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
├── react-executive-dashboard/       # React Frontend
│   ├── src/
│   │   ├── components/              # UI components
│   │   ├── utils/
│   │   │   ├── apiClient.js        # API integration
│   │   │   └── dataGenerator.js    # Mock data fallback
│   │   ├── App.jsx                  # Main app
│   │   └── App.css                  # Styles
│   ├── package.json
│   └── README.md
│
└── SETUP_GUIDE.md                   # This file
```

---

## 🔄 Development Workflow

### Starting Both Services

**Terminal 1 - Backend:**
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd react-executive-dashboard
npm run dev
```

### Making Changes

**Backend Changes:**
- Edit files in `backend/app/`
- Server auto-reloads with `--reload` flag
- Test at http://localhost:8000/docs

**Frontend Changes:**
- Edit files in `react-executive-dashboard/src/`
- Vite automatically hot-reloads
- View at http://localhost:3001

---

## 🚢 Production Deployment

### Backend (FastAPI)

**Deploy to Cloud Run / App Engine:**
```bash
gcloud run deploy executive-dashboard-api \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```

**Or use Docker:**
```bash
docker build -t executive-api ./backend
docker run -p 8000:8000 executive-api
```

### Frontend (React)

**Build for production:**
```bash
cd react-executive-dashboard
npm run build
```

**Deploy to:**
- **Vercel:** `vercel deploy`
- **Netlify:** Drag `dist/` folder
- **Firebase:** `firebase deploy`
- **S3 + CloudFront:** Upload `dist/` to S3

**Update API URL:**
Create `.env.production`:
```env
VITE_API_BASE_URL=https://your-api-domain.com
```

---

## 📚 Additional Resources

- [Backend README](backend/README.md) - Detailed backend documentation
- [Frontend README](react-executive-dashboard/README.md) - React app documentation
- [FastAPI Docs](https://fastapi.tiangolo.com/) - FastAPI framework
- [BigQuery Python Client](https://googleapis.dev/python/bigquery/latest/) - Google BigQuery
- [Vite Documentation](https://vitejs.dev/) - Frontend build tool

---

## 🆘 Getting Help

**Check Logs:**

Backend:
```bash
# Backend logs show in terminal where uvicorn is running
# Look for BigQuery connection errors, query errors, etc.
```

Frontend:
```bash
# Open browser DevTools (F12) → Console
# Look for API fetch errors, CORS errors
```

**Common Log Messages:**

✅ `"status": "healthy"` - Backend connected successfully
❌ `"Permission denied"` - Service account lacks BigQuery permissions
❌ `"Table not found"` - BigQuery table doesn't exist
❌ `"CORS policy"` - CORS not configured correctly

---

## ✅ Checklist

Before asking for help, verify:

- [ ] Python 3.10+ installed (`python --version`)
- [ ] Node.js 18+ installed (`node --version`)
- [ ] Backend dependencies installed (`pip list | grep fastapi`)
- [ ] Frontend dependencies installed (`ls node_modules`)
- [ ] `.env` file exists in `backend/`
- [ ] Service account key file exists
- [ ] `GCP_PROJECT_ID` matches: `chronicle-dev-2be9`
- [ ] `BIGQUERY_DATASET` matches: `gatra_database`
- [ ] Backend running on port 8000
- [ ] Frontend running on port 3001
- [ ] http://localhost:8000/health returns `{"status": "healthy"}`
- [ ] http://localhost:3001 loads the dashboard

---

**Version:** 1.0.0
**Last Updated:** January 6, 2026
**Status:** ✅ Production Ready
