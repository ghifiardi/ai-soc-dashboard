# 🚀 Deployment Guide - Publishing Your Dashboards to the Internet

This guide will help you deploy your AI-SOC dashboards to the internet for free using Streamlit Cloud.

## 🌐 Option 1: Streamlit Cloud (Recommended - FREE & Easy)

Streamlit Cloud is the official hosting platform for Streamlit apps. It's completely **FREE** for public repositories and incredibly easy to set up.

### Prerequisites
- ✅ GitHub account
- ✅ Your dashboards are in a GitHub repository (ghifiardi/ai-soc-dashboard)
- ✅ All code is pushed to the `main` branch

### Step-by-Step Deployment

#### 1. Sign Up for Streamlit Cloud

1. Go to [https://share.streamlit.io/](https://share.streamlit.io/)
2. Click **"Sign up"** in the top right
3. Sign in with your **GitHub account**
4. Authorize Streamlit to access your GitHub repositories

#### 2. Deploy Enhanced SOC Dashboard

1. Click **"New app"** button
2. Fill in the deployment form:
   - **Repository:** `ghifiardi/ai-soc-dashboard`
   - **Branch:** `main`
   - **Main file path:** `enhanced_soc_dashboard.py`
   - **App URL (optional):** Choose a custom URL like `ai-soc-enhanced`

3. Click **"Deploy!"**
4. Wait 2-3 minutes for initial deployment
5. Your dashboard will be live at: `https://[your-app-name].streamlit.app`

#### 3. Deploy Additional Dashboards

Repeat the process for each dashboard:

**Executive Dashboard:**
- Main file path: `executive_dashboard.py`
- Suggested URL: `ai-soc-executive`

**Compliance Dashboard:**
- Main file path: `compliance_dashboard.py`
- Suggested URL: `ai-soc-compliance`

**Original Dashboard:**
- Main file path: `streamlit_soc_dashboard.py`
- Suggested URL: `ai-soc-original`

### 🎯 After Deployment

Once deployed, your dashboards will be accessible to anyone with the URL:

- **Enhanced SOC Dashboard:** `https://ai-soc-enhanced.streamlit.app`
- **Executive Dashboard:** `https://ai-soc-executive.streamlit.app`
- **Compliance Dashboard:** `https://ai-soc-compliance.streamlit.app`
- **Original Dashboard:** `https://ai-soc-original.streamlit.app`

### 🔄 Auto-Updates

Streamlit Cloud automatically monitors your GitHub repository. Whenever you push changes to the `main` branch, your deployed app will automatically update within a few minutes!

### ⚙️ Optional: Configure BigQuery Secrets

If you want to use real BigQuery data instead of demo data:

1. In Streamlit Cloud dashboard, click on your app
2. Click **"Settings"** → **"Secrets"**
3. Add your Google Cloud credentials in TOML format:

```toml
[gcp_service_account]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\nYOUR-PRIVATE-KEY\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@your-project.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your-cert-url"
```

4. Update your dashboard code to read from secrets:
```python
import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)
```

---

## 🐳 Option 2: Docker Deployment (Advanced)

For custom hosting on your own server or cloud platform.

### Build Docker Image

```bash
docker build -t ai-soc-dashboard .
```

### Run Locally

```bash
docker run -p 8501:8501 ai-soc-dashboard
```

### Deploy to Cloud Platforms

**Google Cloud Run:**
```bash
gcloud builds submit --tag gcr.io/PROJECT-ID/ai-soc-dashboard
gcloud run deploy ai-soc-dashboard \
  --image gcr.io/PROJECT-ID/ai-soc-dashboard \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

**AWS ECS/Fargate:**
```bash
aws ecr create-repository --repository-name ai-soc-dashboard
docker tag ai-soc-dashboard:latest AWS_ACCOUNT.dkr.ecr.REGION.amazonaws.com/ai-soc-dashboard:latest
docker push AWS_ACCOUNT.dkr.ecr.REGION.amazonaws.com/ai-soc-dashboard:latest
# Then create ECS task and service
```

**Heroku:**
```bash
heroku container:login
heroku create ai-soc-dashboard
heroku container:push web
heroku container:release web
heroku open
```

---

## 📊 Option 3: Multiple Dashboards with Navigation

Create a main landing page that links to all dashboards:

**Create `Home.py`:**
```python
import streamlit as st

st.set_page_config(
    page_title="AI-SOC Dashboard Suite",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI-SOC Dashboard Suite")
st.markdown("Select a dashboard from the sidebar")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🛡️ Enhanced SOC Dashboard
    Full-featured operational dashboard for SOC analysts
    - Real-time threat timeline
    - Network topology
    - MITRE ATT&CK analysis
    - Advanced analytics
    """)

with col2:
    st.markdown("""
    ### 🎯 Executive Dashboard
    Strategic overview for C-suite and management
    - Key performance indicators
    - Compliance scorecard
    - Risk assessment
    - Trend analysis
    """)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    ### 📜 Compliance Dashboard
    Regulatory compliance and audit management
    - 7 compliance frameworks
    - Audit trail tracking
    - Control status monitoring
    - Compliance trends
    """)

with col4:
    st.markdown("""
    ### 🔥 Original Dashboard
    Streamlined SOC operations view
    - BigQuery integration
    - Real-time metrics
    - Threat visualization
    - Event tracking
    """)
```

**Create `pages/` directory:**
```bash
mkdir pages
mv enhanced_soc_dashboard.py pages/1_🛡️_Enhanced_SOC.py
mv executive_dashboard.py pages/2_🎯_Executive.py
mv compliance_dashboard.py pages/3_📜_Compliance.py
mv streamlit_soc_dashboard.py pages/4_🔥_Original.py
```

Deploy `Home.py` as the main file, and Streamlit will automatically create navigation for all pages!

---

## 🔒 Security Considerations for Public Deployment

### Important Notes:

1. **Demo Data by Default:** All dashboards use mock data by default, so it's safe to deploy publicly
2. **BigQuery Credentials:** Only add if you want real data; use Streamlit Secrets (encrypted)
3. **Authentication:** For production with real data, add authentication:
   ```python
   import streamlit_authenticator as stauth
   # See: https://blog.streamlit.io/streamlit-authenticator-part-1-adding-an-authentication-component-to-your-app/
   ```
4. **Rate Limiting:** Streamlit Cloud has built-in rate limiting
5. **HTTPS:** All Streamlit Cloud apps are automatically served over HTTPS

---

## 📈 Monitoring Your Deployed App

### Streamlit Cloud Dashboard

Access analytics at: [https://share.streamlit.io/](https://share.streamlit.io/)

Monitor:
- **Viewer count:** How many people are using your dashboard
- **Resource usage:** CPU, memory, bandwidth
- **Logs:** Real-time application logs
- **Errors:** Stack traces and error reports

### Usage Limits (Free Tier)

- **Apps:** Unlimited public apps
- **Resources:** 1 GB RAM per app
- **Bandwidth:** Generous free tier
- **Uptime:** 24/7 availability

---

## 🎨 Customizing Your Deployment

### Custom Domain (Premium)

Streamlit Cloud Teams allows custom domains:
- `soc.yourcompany.com` instead of `app.streamlit.app`
- Requires Streamlit Cloud Teams plan

### Branding

Update `config.toml` for custom branding:
```toml
[theme]
primaryColor = "#0066FF"
backgroundColor = "#0A0E27"
secondaryBackgroundColor = "#1a1f3a"
textColor = "#FFFFFF"
font = "sans serif"
```

---

## 🆘 Troubleshooting

### App Won't Deploy

1. Check all files are pushed to GitHub
2. Verify `requirements.txt` is present and correct
3. Check Streamlit Cloud logs for errors
4. Ensure Python version compatibility (3.10+)

### App Crashes

1. Check logs in Streamlit Cloud dashboard
2. Verify all dependencies in `requirements.txt`
3. Test locally first: `streamlit run enhanced_soc_dashboard.py`
4. Check for port conflicts or resource limits

### Slow Performance

1. Reduce data size or use sampling
2. Implement caching with `@st.cache_data`
3. Optimize queries and computations
4. Consider upgrading to Streamlit Cloud Teams for more resources

---

## 📞 Support

- **Streamlit Community:** [https://discuss.streamlit.io/](https://discuss.streamlit.io/)
- **Documentation:** [https://docs.streamlit.io/](https://docs.streamlit.io/)
- **GitHub Issues:** Report bugs in your repository

---

## ✅ Quick Checklist

Before deploying:
- [ ] All code pushed to `main` branch on GitHub
- [ ] `requirements.txt` is up to date
- [ ] Tested locally with `streamlit run`
- [ ] Created Streamlit Cloud account
- [ ] Configured app settings in Streamlit Cloud
- [ ] (Optional) Added BigQuery secrets if using real data
- [ ] Verified app is accessible at public URL
- [ ] Shared URL with your team/stakeholders

---

**🎉 Congratulations!** Your AI-SOC dashboards are now live on the internet!

Share your URLs:
- Enhanced SOC: `https://your-app.streamlit.app`
- Executive: `https://your-executive-app.streamlit.app`
- Compliance: `https://your-compliance-app.streamlit.app`

**Last Updated:** January 6, 2026
