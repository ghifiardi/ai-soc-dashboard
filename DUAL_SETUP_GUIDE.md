# 🚀 Dual Setup Guide - Python + React Dashboards

This guide explains how to use **both** dashboard versions together, when to use each one, and how to set them up.

## 📋 Overview

You now have **TWO** complete dashboard implementations:

### 🐍 Python/Streamlit Version
**Location:** `/home/user/ai-soc-dashboard/*.py`

**Best For:**
- ✅ Rapid prototyping and development
- ✅ Internal tools and admin panels
- ✅ Data science workflows
- ✅ Quick demos and POCs
- ✅ Teams familiar with Python

**Advantages:**
- 🚀 **Fastest development** - Build dashboards in minutes
- 🐍 **Python ecosystem** - Direct access to pandas, numpy, scipy
- 📊 **Data science friendly** - Jupyter notebook integration
- 🔧 **Easy backend integration** - Direct database/API access
- 📝 **Less code** - Simple, declarative syntax

### ⚛️ React/TypeScript Version
**Location:** `/home/user/ai-soc-dashboard/react-dashboard/`

**Best For:**
- ✅ Production deployments
- ✅ Public-facing dashboards
- ✅ High-traffic applications
- ✅ Mobile-first experiences
- ✅ Teams familiar with JavaScript/TypeScript

**Advantages:**
- ⚡ **10x faster** - Client-side rendering, no server delays
- 🛡️ **Type safety** - Catch bugs at compile time
- 🎨 **Full customization** - Any UI/UX you can imagine
- 📦 **Static hosting** - Deploy to CDN (Vercel, Netlify, Cloudflare)
- 📱 **Better mobile** - Native-like mobile experience
- 🌐 **Offline support** - PWA capabilities
- 💰 **Lower costs** - No server needed, just static files

---

## 🎯 When to Use Which Version

### Use Python/Streamlit When:

1. **Rapid Prototyping**
   ```python
   # Create a dashboard in 50 lines
   import streamlit as st
   st.title("My Dashboard")
   st.metric("Users", 1000)
   st.line_chart(data)
   ```

2. **Internal Tools**
   - Admin panels
   - Data exploration tools
   - Quick reports for team

3. **Data Science Workflows**
   - Integrating with Jupyter
   - Using pandas/numpy heavily
   - ML model visualization

4. **Backend Integration**
   - Direct database access
   - Server-side processing
   - Complex calculations

### Use React/TypeScript When:

1. **Production Deployments**
   - Customer-facing dashboards
   - High availability requirements
   - Need for performance

2. **Public Websites**
   - Company security portal
   - Client dashboards
   - Marketing/demo pages

3. **Mobile Apps**
   - Responsive mobile design
   - Touch interactions
   - Offline capability

4. **High Traffic**
   - Scales to millions of users
   - CDN distribution
   - No server costs

---

## 🚀 Setup Instructions

### Option 1: Run Python Version

```bash
cd /home/user/ai-soc-dashboard

# Install dependencies (if not already installed)
pip install -r requirements.txt

# Run any dashboard
streamlit run enhanced_soc_dashboard.py
streamlit run executive_dashboard.py --server.port 8502
streamlit run compliance_dashboard.py --server.port 8503
streamlit run threat_hunting_dashboard.py --server.port 8506

# Or run all at once
./run_all_dashboards.sh
```

**Access:**
- Enhanced SOC: `http://localhost:8501`
- Executive: `http://localhost:8502`
- Compliance: `http://localhost:8503`
- Threat Hunting: `http://localhost:8506`

### Option 2: Run React Version

```bash
cd /home/user/ai-soc-dashboard/react-dashboard

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

**Access:**
- All dashboards: `http://localhost:3000`
- Navigation between dashboards built-in

### Option 3: Run Both Simultaneously

```bash
# Terminal 1: Python dashboards
cd /home/user/ai-soc-dashboard
streamlit run enhanced_soc_dashboard.py

# Terminal 2: React dashboard
cd /home/user/ai-soc-dashboard/react-dashboard
npm run dev
```

**Access:**
- Python: `http://localhost:8501`
- React: `http://localhost:3000`

---

## 🔧 Shared Backend (Optional)

Create a shared API backend that both versions can use:

### FastAPI Backend (Python)

```python
# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow both frontend apps to access
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React
        "http://localhost:8501",   # Streamlit
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/events")
async def get_events():
    # Return security events from database
    return {"events": [...]}

@app.get("/api/hunts")
async def get_hunts():
    # Return threat hunts
    return {"hunts": [...]}
```

### Python Dashboard Connection

```python
import requests

@st.cache_data
def load_events():
    response = requests.get("http://localhost:8000/api/events")
    return response.json()

events = load_events()
```

### React Dashboard Connection

```typescript
// src/api/client.ts
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
});

export const getEvents = async () => {
  const response = await api.get('/api/events');
  return response.data;
};
```

---

## 📦 Deployment Strategies

### Strategy 1: Python for Internal, React for External

```
Production Setup:
├── internal.company.com → Python/Streamlit
│   └── For internal team use
└── soc.company.com → React/TypeScript
    └── For external/client dashboards
```

**Benefits:**
- Internal teams get rapid iteration (Python)
- Customers get fast, professional UI (React)
- Each optimized for its use case

### Strategy 2: Progressive Migration

```
Phase 1: Launch Python version quickly
Phase 2: Migrate key dashboards to React
Phase 3: Keep Python for admin panels
```

**Benefits:**
- Get to market fast with Python
- Improve UX over time with React
- Maintain both for different needs

### Strategy 3: Microservices Architecture

```
Architecture:
├── API Backend (FastAPI/Flask)
│   └── Shared data layer
├── Python Dashboards (Internal)
│   └── streamlit.internal.com
└── React Dashboards (Public)
    └── soc.company.com
```

**Benefits:**
- Decoupled frontend and backend
- Share data layer
- Scale each independently

---

## 🎨 Feature Comparison

| Feature | Python/Streamlit | React/TypeScript | Winner |
|---------|------------------|------------------|---------|
| **Development Speed** | ⚡⚡⚡ Very Fast | ⚡⚡ Moderate | Python |
| **Runtime Performance** | 🐢 Slow (server) | ⚡⚡⚡ Fast (client) | React |
| **Type Safety** | ⚠️ Limited | ✅ Full | React |
| **Customization** | 🎨 Limited | 🎨🎨🎨 Unlimited | React |
| **Mobile UX** | 📱 Basic | 📱📱📱 Native-like | React |
| **Deployment Complexity** | 🔧🔧 Moderate | 🔧 Simple | React |
| **Hosting Cost** | 💰💰 Server needed | 💰 Free (static) | React |
| **Learning Curve** | 📚 Easy | 📚📚 Steeper | Python |
| **Data Science** | 🔬🔬🔬 Excellent | 🔬 Basic | Python |
| **Scalability** | 📈 Vertical | 📈📈📈 Horizontal | React |

---

## 🔄 Migration Path

### From Python to React (if needed)

1. **Start with Python** for rapid development
2. **Identify production dashboards** that need performance
3. **Migrate one dashboard at a time** to React
4. **Share backend API** between both
5. **Keep Python for internal tools**

### Code Reuse

**Data models** can be shared:

```python
# Python (models.py)
class SecurityEvent:
    id: str
    timestamp: datetime
    severity: str
```

```typescript
// TypeScript (types/dashboard.ts)
interface SecurityEvent {
  id: string;
  timestamp: Date;
  severity: string;
}
```

**API responses** are the same:

```json
{
  "id": "evt-123",
  "timestamp": "2026-01-06T12:00:00Z",
  "severity": "Critical"
}
```

---

## 💡 Best Practices

### Use Python When You Need:
- ✅ Quick iteration
- ✅ Data science libraries
- ✅ Server-side processing
- ✅ Direct database access
- ✅ Simple deployment for internal use

### Use React When You Need:
- ✅ High performance
- ✅ Custom UI/UX
- ✅ Mobile-first design
- ✅ Static hosting
- ✅ Type safety
- ✅ Offline support

### Combine Both When:
- ✅ Building internal + external dashboards
- ✅ Need rapid prototyping + production quality
- ✅ Team has mixed skill sets
- ✅ Want flexibility in deployment

---

## 📊 Real-World Example

### Scenario: SOC Dashboard for Enterprise

**Internal Analysts (Python):**
```
streamlit.internal-soc.company.com
- Quick data exploration
- Ad-hoc queries
- Rapid response tools
- Internal only, VPN required
```

**Executive Team (React):**
```
exec.soc.company.com
- Executive KPIs
- Clean, professional UI
- Mobile-friendly
- Accessible anywhere
```

**Customers (React):**
```
portal.soc.company.com
- Customer-facing portal
- High performance
- Custom branding
- Public internet
```

**Backend (Shared):**
```
api.soc.company.com
- FastAPI
- PostgreSQL
- BigQuery
- Shared by all frontends
```

---

## 🎉 Summary

| Aspect | Python | React | Both |
|--------|--------|-------|------|
| **Time to Market** | ⚡ Fast | 🐢 Slower | 🎯 Best |
| **Final Performance** | 🐢 Slow | ⚡ Fast | 🎯 Best |
| **Flexibility** | 🎨 Limited | 🎨 Unlimited | 🎯 Best |
| **Cost** | 💰 Server | 💰 Free | 💰 Optimized |
| **Team Skills** | 🐍 Python | ⚛️ JS/TS | 🎯 Both |

## 🚀 Get Started Now

### Quick Start (Both Versions):

```bash
# Clone repo
git clone https://github.com/ghifiardi/ai-soc-dashboard.git
cd ai-soc-dashboard

# Terminal 1: Python
pip install -r requirements.txt
streamlit run enhanced_soc_dashboard.py

# Terminal 2: React
cd react-dashboard
npm install
npm run dev
```

**Explore both versions and choose what works best for your use case!**

---

**Questions?** Check README.md in each directory for detailed documentation.

**Built with ❤️ - The best of both Python and React**
