# Dockerfile for AI-SOC Dashboard Suite
# Build: docker build -t ai-soc-dashboard .
# Run: docker run -p 8501:8501 ai-soc-dashboard

FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Default to Enhanced SOC Dashboard
# Override with: docker run -p 8501:8501 ai-soc-dashboard streamlit run executive_dashboard.py
ENV DASHBOARD_FILE=enhanced_soc_dashboard.py

# Run the dashboard
ENTRYPOINT ["streamlit", "run"]
CMD ["enhanced_soc_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
