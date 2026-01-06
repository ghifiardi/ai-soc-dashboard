#!/bin/bash
# Run all AI-SOC Dashboards simultaneously on different ports

echo "🚀 Starting all AI-SOC Dashboards..."
echo ""

# Enhanced SOC Dashboard - Port 8501
echo "Starting Enhanced SOC Dashboard on http://localhost:8501"
streamlit run enhanced_soc_dashboard.py --server.port 8501 &

# Executive Dashboard - Port 8502
echo "Starting Executive Dashboard on http://localhost:8502"
streamlit run executive_dashboard.py --server.port 8502 &

# Compliance Dashboard - Port 8503
echo "Starting Compliance Dashboard on http://localhost:8503"
streamlit run compliance_dashboard.py --server.port 8503 &

# Threat Hunting Dashboard - Port 8506
echo "Starting Threat Hunting Dashboard on http://localhost:8506"
streamlit run threat_hunting_dashboard.py --server.port 8506 &

# Original SOC Dashboard - Port 8504
echo "Starting Original SOC Dashboard on http://localhost:8504"
streamlit run streamlit_soc_dashboard.py --server.port 8504 &

echo ""
echo "✅ All dashboards started!"
echo ""
echo "Access your dashboards at:"
echo "  🛡️  Enhanced SOC:      http://localhost:8501"
echo "  🎯  Executive:         http://localhost:8502"
echo "  📜  Compliance:        http://localhost:8503"
echo "  🔍  Threat Hunting:    http://localhost:8506"
echo "  🔥  Original:          http://localhost:8504"
echo ""
echo "Press Ctrl+C to stop all dashboards"

wait
