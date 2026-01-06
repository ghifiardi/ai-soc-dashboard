# Executive Dashboard FastAPI Backend

FastAPI backend service that connects to Google BigQuery and serves real-time security metrics to the React Executive Dashboard.

## 🎯 Features

- **BigQuery Integration** - Fetches real security data from `gatra_database`
- **REST API** - Clean RESTful endpoints for dashboard data
- **Auto-Fallback** - Gracefully falls back to mock data if BigQuery is unavailable
- **CORS Enabled** - Configured for React frontend communication
- **Fast & Async** - Built with FastAPI for high performance
- **Type Safety** - Pydantic models for data validation
- **Auto Documentation** - Interactive API docs at `/docs`

## 📋 Prerequisites

- Python 3.10 or higher
- Google Cloud Platform account
- BigQuery access to `chronicle-dev-2be9` project
- Service account JSON key file

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit `.env` with your settings:

```env
# Google Cloud Configuration
GCP_PROJECT_ID=chronicle-dev-2be9
BIGQUERY_DATASET=gatra_database
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your-service-account-key.json

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=http://localhost:3001,http://localhost:3000

# Environment
ENVIRONMENT=development
```

### 3. Set Up Google Cloud Credentials

**Option A: Service Account Key (Recommended)**

1. Download your service account JSON key from Google Cloud Console
2. Save it to a secure location (e.g., `~/gcp-keys/chronicle-key.json`)
3. Update `GOOGLE_APPLICATION_CREDENTIALS` in `.env` to point to this file

**Option B: Application Default Credentials**

```bash
gcloud auth application-default login
```

### 4. Run the Server

**Development mode (with auto-reload):**

```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Production mode:**

```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

The API will be available at: **http://localhost:8000**

### 5. Test the API

**Health Check:**
```bash
curl http://localhost:8000/health
```

**Get Executive Dashboard Data:**
```bash
curl http://localhost:8000/api/executive/dashboard
```

**View Interactive API Docs:**
Open your browser to **http://localhost:8000/docs**

## 📊 API Endpoints

### Root Endpoint
- **GET** `/` - API information and available endpoints

### Executive Dashboard
- **GET** `/api/executive/dashboard?days=30` - Get complete dashboard data
  - Query Parameters:
    - `days` (optional): Number of days to analyze (default: 30, range: 1-365)
  - Returns: Complete executive dashboard metrics, trends, and visualizations

- **GET** `/api/executive/health` - Health check for executive dashboard service

### Global Health
- **GET** `/health` - General API health check

## 📁 Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                      # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   └── executive.py             # Executive dashboard endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── bigquery_service.py      # BigQuery data fetching
│   │   └── data_transformer.py      # Data transformation logic
│   ├── models/
│   │   ├── __init__.py
│   │   └── executive_metrics.py     # Pydantic data models
│   └── config/
│       ├── __init__.py
│       └── settings.py              # Application settings
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
└── README.md                        # This file
```

## 🗄️ BigQuery Schema

The API expects the following tables in your `gatra_database`:

### `activity_logs`
```sql
- timestamp (TIMESTAMP)
- severity (STRING): 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW'
- status (STRING): 'RESOLVED', 'IN_PROGRESS', 'OPEN'
- detection_time (TIMESTAMP)
- response_time (TIMESTAMP)
- is_false_positive (BOOLEAN)
```

### `agent_metrics`
```sql
- timestamp (TIMESTAMP)
- detection_time_minutes (FLOAT)
- response_time_minutes (FLOAT)
- resolution_time_minutes (FLOAT)
- security_score (INTEGER): 0-100
```

**Note:** If these tables don't exist or have different schemas, the API will gracefully fall back to mock data.

## 🔄 Data Flow

```
BigQuery (gatra_database)
    ↓
BigQueryService (Fetch & Query)
    ↓
DataTransformer (Transform & Format)
    ↓
FastAPI Endpoints
    ↓
React Frontend (http://localhost:3001)
```

## 🛠️ Development

### Adding New Endpoints

1. Create model in `app/models/`:
```python
from pydantic import BaseModel

class NewMetric(BaseModel):
    name: str
    value: int
```

2. Add service method in `app/services/bigquery_service.py`:
```python
def get_new_metric(self):
    query = f"""
    SELECT name, value
    FROM `{self.project_id}.{self.dataset_id}.new_table`
    """
    return self._execute_query(query)
```

3. Create endpoint in `app/api/`:
```python
@router.get("/new-endpoint")
async def get_new_data():
    data = bigquery_service.get_new_metric()
    return data
```

### Testing

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

## 🐳 Docker Deployment

**Build Image:**
```bash
docker build -t executive-dashboard-api .
```

**Run Container:**
```bash
docker run -d \
  -p 8000:8000 \
  -e GCP_PROJECT_ID=chronicle-dev-2be9 \
  -e BIGQUERY_DATASET=gatra_database \
  -v /path/to/key.json:/app/key.json \
  -e GOOGLE_APPLICATION_CREDENTIALS=/app/key.json \
  executive-dashboard-api
```

## 🔐 Security Best Practices

1. **Never commit `.env` or service account keys** to version control
2. **Use environment variables** for sensitive configuration
3. **Restrict CORS origins** in production to only your frontend domains
4. **Use HTTPS** in production environments
5. **Implement authentication** (OAuth2, JWT) for production APIs
6. **Rotate service account keys** regularly
7. **Use least-privilege IAM roles** for BigQuery access

## 🚨 Troubleshooting

### "Permission denied" errors

**Solution:** Check that your service account has these IAM roles:
- `BigQuery Data Viewer`
- `BigQuery Job User`

### "Table not found" errors

**Solution:** Verify:
1. Project ID is correct: `chronicle-dev-2be9`
2. Dataset exists: `gatra_database`
3. Tables exist: `activity_logs`, `agent_metrics`

### API returns mock data instead of real data

**Solution:** Check:
1. `.env` file has correct `GOOGLE_APPLICATION_CREDENTIALS` path
2. Service account key file exists and is readable
3. Check API logs for BigQuery connection errors

### CORS errors in React app

**Solution:** Ensure `CORS_ORIGINS` in `.env` includes your React app URL:
```env
CORS_ORIGINS=http://localhost:3001,http://localhost:3000
```

## 📝 Environment Variables Reference

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `GCP_PROJECT_ID` | Google Cloud project ID | `chronicle-dev-2be9` | Yes |
| `BIGQUERY_DATASET` | BigQuery dataset name | `gatra_database` | Yes |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to service account key JSON | - | Yes |
| `API_HOST` | API server host | `0.0.0.0` | No |
| `API_PORT` | API server port | `8000` | No |
| `CORS_ORIGINS` | Allowed CORS origins (comma-separated) | `http://localhost:3001` | No |
| `ENVIRONMENT` | Environment name | `development` | No |

## 🔗 Integration with React Frontend

The React Executive Dashboard automatically connects to this API:

1. **Start the backend** (port 8000)
2. **Start the React frontend** (port 3001)
3. Frontend will fetch data from `http://localhost:8000/api/executive/dashboard`
4. If API is unavailable, frontend falls back to mock data

See `react-executive-dashboard/README.md` for frontend setup.

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Google BigQuery Python Client](https://googleapis.dev/python/bigquery/latest/)
- [Pydantic Models](https://docs.pydantic.dev/)
- [Uvicorn Server](https://www.uvicorn.org/)

## 🆘 Support

For issues or questions:
- Check the troubleshooting section above
- Review FastAPI logs for error messages
- Verify BigQuery permissions and table schemas
- Test with `/docs` interactive API documentation

---

**Version:** 1.0.0
**Last Updated:** January 6, 2026
**Maintained by:** AI SOC Dashboard Team
