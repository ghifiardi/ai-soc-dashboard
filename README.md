AI‑SOC Command Center (Enhanced AI‑Driven SOC Dashboard)
=======================================================

An enhanced Streamlit dashboard for Security Operations with a modern UI and simulated live telemetry.

Features
--------
- 📡 Telemetry Ingestion & Validation: Live events with severity, MITRE mapping, and validation status
- 🤖 AI Enrichment & Correlation: MITRE ATT&CK mapping and asset risk scoring heatmap
- ⚖️ Risk Decision Engine: Auto-remediation vs. analyst review vs. IR escalation with Sankey visualization
- 🔧 Patch Management: Active deployments and success metrics
- 📊 Governance & Compliance: Framework scorecards and report snapshot
- ⚙️ System Health & Performance: CPU, memory, uptime, and latency metrics

Repository layout
-----------------
- `streamlit_soc_dashboard.py`: Main Streamlit app entrypoint
- `requirements.txt`: Python dependencies
- (Optional) Other historical dashboard variants: `fast_loading_dashboard.py`, `dark_mode_fixed_dashboard.py`, etc.

Quick start (local)
-------------------
1. Python 3.10+ recommended
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run streamlit_soc_dashboard.py
   ```
4. Open the URL printed by Streamlit (typically `http://localhost:8501`).

Deploy on Streamlit Cloud
-------------------------
1. Create a new app in Streamlit Cloud and connect this repo: `ghifiardi/ai-soc-dashboard`
2. Set Main file path to:
   - `streamlit_soc_dashboard.py`
3. Select branch: `main`
4. Deploy

Configuration and usage
-----------------------
- Use the sidebar to select sections to display and enable auto‑refresh.
- The current build uses simulated data; no external services are required.

Notes
-----
- Dependencies include some optional packages for future integrations (e.g., BigQuery). They are not required to run the enhanced dashboard as-is.
- To slim dependencies, you can remove unused packages from `requirements.txt` if desired.

Troubleshooting
---------------
- If port 8501 is in use locally, run: `streamlit run streamlit_soc_dashboard.py --server.port 8502`
- On Streamlit Cloud, if a deploy fails, verify the Main file path is `streamlit_soc_dashboard.py` and that the Python version supports the listed dependencies.


