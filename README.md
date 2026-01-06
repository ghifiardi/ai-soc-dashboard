AI-SOC Command Center - Enhanced Edition 🛡️
==========================================

A comprehensive suite of enterprise-grade Security Operations Center (SOC) dashboards built with Streamlit, featuring real-time threat intelligence, advanced analytics, compliance tracking, and executive reporting.

## 🌟 Overview

This project provides **five specialized dashboards** designed for different stakeholders in your security operations:

1. **🛡️ Enhanced SOC Dashboard** - Full-featured operational dashboard for SOC analysts
2. **🎯 Executive Dashboard** - Strategic overview for C-suite and management
3. **📜 Compliance Dashboard** - Regulatory compliance tracking and audit management
4. **🔍 Threat Hunting Dashboard** - AI-powered proactive threat hunting and investigation
5. **🔥 Original SOC Dashboard** - Streamlined operational view with BigQuery integration

---

## 📊 Dashboard Features

### 🛡️ Enhanced SOC Dashboard (`enhanced_soc_dashboard.py`)

**Target Audience:** SOC Analysts, Security Engineers, Threat Hunters

**Key Features:**
- **Real-time Threat Timeline** - Interactive visualization of security events over time
- **Network Topology Mapping** - Visual representation of network connections and threat paths
- **MITRE ATT&CK Heatmap** - Distribution of attack techniques based on MITRE framework
- **Geographic Threat Distribution** - Global map showing threat origins
- **Incident Response Funnel** - Track incidents through investigation pipeline
- **AI-Powered Analytics** - Threat actor profiling, protocol analysis, asset targeting
- **Advanced Filtering** - Multi-criteria filtering by severity, time range, event type
- **Search & Export** - Full-text search with CSV/JSON export capabilities
- **Auto-Refresh** - Configurable auto-refresh for real-time monitoring
- **Customizable Views** - Toggle dashboard sections on/off based on needs

**Notable Visualizations:**
- Interactive timeline charts with severity breakdown
- Network graph topology with threat concentration
- Heat maps for MITRE technique distribution
- Choropleth maps for geographic analysis
- Funnel charts for incident response workflow

---

### 🎯 Executive Dashboard (`executive_dashboard.py`)

**Target Audience:** CISOs, C-Suite Executives, Senior Management

**Key Features:**
- **Executive KPIs** - High-level security metrics and trends
  - Total incidents with period-over-period comparison
  - Critical incident tracking
  - Resolution rate percentages
  - Overall security score (0-100)
- **Operational Performance Metrics**
  - Mean Time to Detect (MTTD)
  - Mean Time to Respond (MTTR)
  - Mean Time to Resolve
- **Trend Analysis** - 30-day incident trends with visual indicators
- **Risk Assessment** - Top security risks with severity classification
- **Compliance Scorecard** - Multi-framework compliance status (NIST, ISO, SOC 2, GDPR, HIPAA)
- **Executive Summary** - Narrative summary with key findings and recommendations

**Design Philosophy:**
- Clean, professional light theme suitable for presentations
- Focus on high-level metrics and business impact
- Clear delta indicators showing improvement/degradation
- Minimal technical jargon, maximum strategic insight

**🆕 React Version Available:**
A modern React implementation of the Executive Dashboard is now available at `react-executive-dashboard/`. This provides:
- Enhanced performance and responsiveness
- Modern component architecture with React 18
- Interactive Recharts visualizations
- Easier integration with web services and APIs
- Standalone deployment to static hosting (Vercel, Netlify, etc.)
- Full feature parity with Streamlit version

See `react-executive-dashboard/README.md` for setup and deployment instructions.

---

### 📜 Compliance & Audit Dashboard (`compliance_dashboard.py`)

**Target Audience:** Compliance Officers, Auditors, Risk Management Teams

**Supported Frameworks:**
- NIST Cybersecurity Framework (CSF)
- ISO 27001
- SOC 2 (Trust Service Criteria)
- GDPR (General Data Protection Regulation)
- HIPAA (Health Insurance Portability and Accountability Act)
- PCI DSS (Payment Card Industry Data Security Standard)
- CIS Controls (Center for Internet Security)

**Key Features:**
- **Framework Compliance Scoring** - Real-time compliance percentage for each framework
- **Control Status Tracking** - Passed/failed controls with detailed breakdowns
- **Category Analysis** - Sub-category compliance scores within each framework
- **Compliance Trend Analysis** - 12-month historical trend tracking
- **Comprehensive Audit Trail** - Detailed event logging with:
  - Event type classification
  - Severity levels
  - User attribution
  - Resource tracking
  - IP address logging
  - Timestamp precision
- **Advanced Filtering** - Multi-dimensional filtering by severity, event type, user
- **Search Capabilities** - Full-text search across audit entries
- **Export Functions** - Generate compliance reports and export audit logs
- **Audit Scheduling** - Track last and next audit dates for all frameworks

**Audit Event Types:**
- Access Control
- Data Modification
- Configuration Change
- Policy Update
- Compliance Check

---

### 🔍 Threat Hunting Dashboard (`threat_hunting_dashboard.py`)

**Target Audience:** Threat Hunters, SOC Analysts, Security Researchers

**Key Features:**
- **Real-Time Timestamp Generation** - All data uses current datetime (fixes old timestamp issue)
- **AI/ML-Powered Alert Analysis** - 7 ML models for threat classification
  - Random Forest, Neural Network, XGBoost, Isolation Forest, Deep Learning CNN
  - True positive/false positive rate tracking
  - Confidence scoring and threshold filtering
- **Active Hunt Mission Management** - Track ongoing investigations
  - Mission status (Active, Investigating, Completed, On Hold)
  - IOC (Indicators of Compromise) tracking
  - Priority classification (Critical, High, Medium, Low)
  - Entity analysis and confidence scores
- **Social Media Threat Monitoring** - Real-time threat detection from social platforms
  - Twitter, Facebook, Instagram, LinkedIn, Reddit monitoring
  - Keyword tracking and frequency analysis
  - Threat score calculation and trend analysis
  - Platform engagement metrics
- **Security Alert Processing** - Live alert monitoring with AI classification
  - Timestamps within last 24 hours (always current)
  - Multi-source integration (SIEM, EDR, IDS/IPS, Firewall)
  - Confidence-based filtering
  - Hunt status tracking
- **Advanced Analytics** - Behavioral threat analytics
  - ML model confidence distribution
  - Alert category predictions
  - Hourly threat timeline analysis
  - Keyword frequency distribution
- **Hunt Controls** - Customizable hunting parameters
  - Configurable time ranges (1 hour to 30 days)
  - Hunt focus selection (APT, Insider Threat, Malware, C2, etc.)
  - Confidence threshold slider
  - Auto-refresh with configurable intervals

**Notable Visualizations:**
- Hunt mission status pie charts
- Priority distribution bar charts
- ML model confidence box plots
- Social media threat timeline (dual-axis)
- Top threat keywords frequency chart
- Alert category heatmaps
- Real-time data tables with current timestamps

**Timestamp Fix:**
All security alerts, social media threats, and hunt missions now generate timestamps relative to `datetime.now()`, ensuring data is always current and recent (no more October 2025 dates!).

---

### 🔥 Original SOC Dashboard (`streamlit_soc_dashboard.py`)

**Target Audience:** SOC Analysts, Security Operations

**Key Features:**
- **BigQuery Integration** - Live data from Google Cloud BigQuery
- **Fallback Demo Mode** - High-quality mock data when BigQuery unavailable
- **Real-time Metrics** - Total events, unique sources, threat levels
- **Global Threat Map** - Geographic visualization of threat origins
- **Severity Distribution** - Bar charts showing threat severity breakdown
- **Attack Type Analysis** - Pie charts for attack classification
- **Recent Events Table** - Detailed view of latest security events
- **Connection Status** - Clear indication of data source (live vs demo)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ghifiardi/ai-soc-dashboard.git
   cd ai-soc-dashboard
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Dashboards

#### Streamlit Dashboards

**Enhanced SOC Dashboard (Recommended):**
```bash
streamlit run enhanced_soc_dashboard.py
```

**Executive Dashboard:**
```bash
streamlit run executive_dashboard.py
```

**Compliance Dashboard:**
```bash
streamlit run compliance_dashboard.py
```

**Threat Hunting Dashboard:**
```bash
streamlit run threat_hunting_dashboard.py
```

**Original SOC Dashboard:**
```bash
streamlit run streamlit_soc_dashboard.py
```

The dashboard will automatically open in your default browser at `http://localhost:8501`

#### React Executive Dashboard

**Navigate to React dashboard:**
```bash
cd react-executive-dashboard
npm install
npm run dev
```

The React dashboard will open at `http://localhost:3000`

See `react-executive-dashboard/README.md` for detailed setup instructions and deployment options.

### Custom Port

If port 8501 is in use:
```bash
streamlit run enhanced_soc_dashboard.py --server.port 8502
```

---

## 🎨 Dashboard Controls

### Enhanced SOC Dashboard

**Sidebar Controls:**
- **Auto-Refresh:** Enable/disable with configurable interval (5-60 seconds)
- **Time Range:** Select from 1 hour to 7 days
- **Severity Filter:** Multi-select Critical/High/Medium/Low
- **Dashboard Sections:** Toggle visibility of:
  - Overview Metrics
  - Threat Timeline
  - Network Topology
  - MITRE ATT&CK
  - Geographic Distribution
  - Advanced Analytics
  - Recent Events Table
- **System Status:** Monitor CPU, memory, and uptime
- **Export Options:** Download data in multiple formats

**Main View:**
- **Search Bar:** Full-text search across all events
- **Export Buttons:** CSV and JSON export for filtered data
- **Interactive Charts:** Click, zoom, and hover for details

### Executive Dashboard

**Controls:**
- **Reporting Period:** Select Last 7 Days, Last 30 Days, Last Quarter, or YTD
- **Metric Cards:** Hover for detailed tooltips
- **Trend Charts:** Interactive timeline exploration

### Compliance Dashboard

**Sidebar Controls:**
- **Framework Selection:** Choose which compliance frameworks to display
- **Reporting Period:** Current month, quarter, YTD, or custom range
- **Audit Trail Filters:**
  - Severity levels
  - Event types
- **Export Functions:**
  - Generate compliance reports
  - Export audit logs

**Main View:**
- **Audit Trail Search:** Filter events by user, resource, action
- **Framework Details:** Expandable category breakdowns
- **Trend Analysis:** 12-month compliance score visualization

---

## 📦 Dependencies

Core dependencies (see `requirements.txt` for versions):
- `streamlit` - Web framework for dashboards
- `pandas` - Data manipulation and analysis
- `plotly` - Interactive visualizations
- `numpy` - Numerical computing
- `google-cloud-bigquery` - Google Cloud BigQuery integration (optional)
- `google-auth` - Google Cloud authentication (optional)

---

## 🔧 Configuration

### BigQuery Integration (Optional)

For live data integration with Google BigQuery:

1. Set up Google Cloud credentials
2. Update project ID in dashboard files:
   ```python
   client = bigquery.Client(project="your-project-id")
   ```
3. Configure BigQuery dataset and table names

**Note:** All dashboards work with high-quality mock data if BigQuery is not configured.

### Data Customization

Mock data generators can be customized in each dashboard file:
- Event frequencies
- Threat types
- Severity distributions
- Geographic sources
- MITRE techniques

---

## 📂 Project Structure

```
ai-soc-dashboard/
├── enhanced_soc_dashboard.py      # Main enhanced dashboard
├── executive_dashboard.py         # Executive/C-suite dashboard (Streamlit)
├── compliance_dashboard.py        # Compliance & audit dashboard
├── threat_hunting_dashboard.py    # AI-powered threat hunting dashboard
├── streamlit_soc_dashboard.py     # Original BigQuery dashboard
├── react-executive-dashboard/     # React version of Executive Dashboard
│   ├── src/
│   │   ├── components/           # React components (KPIs, charts, etc.)
│   │   ├── utils/                # Data generation utilities
│   │   ├── App.jsx               # Main application
│   │   └── App.css               # Global styles
│   ├── package.json              # Node dependencies
│   └── README.md                 # React dashboard documentation
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── config.py                      # Configuration settings
├── config.toml                    # Streamlit config
├── Dockerfile                     # Docker container configuration
├── docker-compose.yml             # Docker Compose orchestration
├── DEPLOYMENT_GUIDE.md            # Comprehensive deployment guide
└── (legacy files)                 # Historical dashboard variants
```

---

## 🚀 Deployment

### Streamlit Cloud

1. **Create Streamlit Cloud Account** at [streamlit.io/cloud](https://streamlit.io/cloud)

2. **Deploy Dashboard:**
   - Connect your GitHub repository
   - Select branch (e.g., `main`)
   - Set main file path to desired dashboard:
     - `enhanced_soc_dashboard.py` (recommended)
     - `executive_dashboard.py`
     - `compliance_dashboard.py`
     - `streamlit_soc_dashboard.py`

3. **Configure Secrets** (if using BigQuery):
   - Add Google Cloud credentials to Streamlit secrets
   - Configure environment variables

4. **Deploy** - Streamlit Cloud will build and host your dashboard

### Docker (Alternative)

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "enhanced_soc_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t ai-soc-dashboard .
docker run -p 8501:8501 ai-soc-dashboard
```

---

## 🎯 Use Cases

### For SOC Analysts
Use **Enhanced SOC Dashboard** for:
- Real-time threat monitoring
- Incident investigation and triage
- Network topology analysis
- MITRE ATT&CK mapping
- Threat hunting activities

### For Executives
Use **Executive Dashboard** for:
- Board presentations
- Strategic planning
- Budget justification
- Risk communication
- Performance reporting

### For Compliance Teams
Use **Compliance Dashboard** for:
- Regulatory audits
- Framework compliance tracking
- Audit trail management
- Policy compliance verification
- Risk assessment documentation

---

## 🔐 Security Considerations

- **Data Handling:** All mock data is generated in-memory; no sensitive data persists
- **Authentication:** Add Streamlit authentication for production deployments
- **Access Control:** Implement role-based access control (RBAC) as needed
- **Audit Logging:** Compliance dashboard includes comprehensive audit trail
- **Encryption:** Use HTTPS in production; encrypt data in transit
- **API Security:** Secure BigQuery credentials using secrets management

---

## 📈 Performance Optimization

- **Caching:** Streamlit's `@st.cache_data` decorator used for expensive operations
- **Data Sampling:** Large datasets are automatically sampled for visualization
- **Lazy Loading:** Charts render only when visible
- **Efficient Queries:** BigQuery queries optimized for performance
- **Auto-Refresh Limits:** Configurable intervals prevent excessive API calls

---

## 🐛 Troubleshooting

### Dashboard Won't Start
```bash
# Check Python version
python --version  # Should be 3.10+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### BigQuery Connection Errors
- Verify Google Cloud credentials are properly configured
- Check project ID and dataset names
- Ensure BigQuery API is enabled in Google Cloud Console
- Dashboard will automatically fall back to demo mode if BigQuery fails

### Port Already in Use
```bash
streamlit run enhanced_soc_dashboard.py --server.port 8502
```

### Slow Performance
- Reduce auto-refresh interval
- Limit time range for data queries
- Disable unused dashboard sections
- Use data sampling for large datasets

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 📧 Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Contact the development team
- Check documentation and troubleshooting guides

---

## 🎉 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Visualizations powered by [Plotly](https://plotly.com/)
- Data processing with [Pandas](https://pandas.pydata.org/)
- MITRE ATT&CK framework reference
- Compliance frameworks: NIST, ISO, SOC 2, GDPR, HIPAA, PCI DSS, CIS

---

## 📊 Version History

- **v2.1.0** - Added React version of Executive Dashboard with modern web stack
- **v2.0.0** - Enhanced Edition with multiple specialized dashboards
- **v1.0.0** - Initial release with basic SOC dashboard

---

**Last Updated:** January 6, 2026
**Status:** ✅ Production Ready
**Maintainer:** Development Team


