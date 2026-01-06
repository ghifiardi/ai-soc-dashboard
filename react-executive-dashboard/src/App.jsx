import React, { useState, useEffect } from 'react';
import './App.css';
import KPICard from './components/KPICard';
import IncidentTrendChart from './components/IncidentTrendChart';
import SeverityPieChart from './components/SeverityPieChart';
import RiskAssessment from './components/RiskAssessment';
import ComplianceScorecard from './components/ComplianceScorecard';
import ExecutiveSummary from './components/ExecutiveSummary';
import {
  generateExecutiveData,
  calculateDelta,
  formatDelta,
  generateTrendData,
  generateSeverityData,
  generateRiskData,
  generateComplianceData
} from './utils/dataGenerator';

function App() {
  const [period, setPeriod] = useState('Last 30 Days');
  const [metrics, setMetrics] = useState(null);
  const [trendData, setTrendData] = useState([]);
  const [severityData, setSeverityData] = useState([]);
  const [riskData, setRiskData] = useState([]);
  const [complianceData, setComplianceData] = useState([]);

  useEffect(() => {
    // Generate all data on mount
    const metricsData = generateExecutiveData();
    setMetrics(metricsData);
    setTrendData(generateTrendData(30));
    setSeverityData(generateSeverityData());
    setRiskData(generateRiskData());
    setComplianceData(generateComplianceData());
  }, []);

  if (!metrics) {
    return (
      <div className="app">
        <div className="container">
          <p style={{ textAlign: 'center', color: '#64748B' }}>Loading dashboard...</p>
        </div>
      </div>
    );
  }

  const { current, previous } = metrics;

  // Calculate deltas for KPIs
  const totalIncidentsDelta = formatDelta(
    calculateDelta(current.totalIncidents, previous.totalIncidents),
    true // inverse - lower is better
  );

  const criticalIncidentsDelta = formatDelta(
    calculateDelta(current.criticalIncidents, previous.criticalIncidents),
    true
  );

  const resolvedRateDelta = formatDelta(
    calculateDelta(current.resolvedRate, previous.resolvedRate)
  );

  const securityScoreDelta = formatDelta(
    calculateDelta(current.securityScore, previous.securityScore)
  );

  const mttdDelta = formatDelta(
    calculateDelta(current.mttd, previous.mttd),
    true
  );

  const mttrDelta = formatDelta(
    calculateDelta(current.mttr, previous.mttr),
    true
  );

  const mttrResolveDelta = formatDelta(
    calculateDelta(current.mttrResolve, previous.mttrResolve),
    true
  );

  const currentDate = new Date().toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });

  return (
    <div className="app">
      <div className="container">
        {/* Header */}
        <h1 className="executive-title">🎯 Executive Security Dashboard</h1>
        <p className="executive-subtitle">
          Strategic Overview | Security Posture | Business Risk Assessment
        </p>

        {/* Period Selector */}
        <div className="period-selector">
          <select
            value={period}
            onChange={(e) => setPeriod(e.target.value)}
          >
            <option>Last 7 Days</option>
            <option>Last 30 Days</option>
            <option>Last Quarter</option>
            <option>Year to Date</option>
          </select>
        </div>

        <div className="divider" />

        {/* Key Performance Indicators */}
        <h2 className="section-title">📊 Key Security Metrics</h2>
        <div className="kpi-grid">
          <KPICard
            label="Total Incidents"
            value={current.totalIncidents}
            delta={totalIncidentsDelta}
            borderColor="blue"
          />
          <KPICard
            label="Critical Incidents"
            value={current.criticalIncidents}
            delta={criticalIncidentsDelta}
            borderColor="red"
          />
          <KPICard
            label="Resolution Rate"
            value={`${current.resolvedRate.toFixed(1)}%`}
            delta={resolvedRateDelta}
            borderColor="green"
          />
          <KPICard
            label="Security Score"
            value={`${current.securityScore}/100`}
            delta={securityScoreDelta}
            borderColor="amber"
          />
        </div>

        <div className="divider" />

        {/* Operational Performance */}
        <h2 className="section-title">⏱️ Operational Performance</h2>
        <div className="metrics-grid">
          <KPICard
            label="Mean Time to Detect"
            value={`${current.mttd.toFixed(0)}m`}
            delta={mttdDelta}
            borderColor="blue"
          />
          <KPICard
            label="Mean Time to Respond"
            value={`${current.mttr.toFixed(0)}m`}
            delta={mttrDelta}
            borderColor="blue"
          />
          <KPICard
            label="Mean Time to Resolve"
            value={`${(current.mttrResolve / 60).toFixed(1)}h`}
            delta={mttrResolveDelta}
            borderColor="blue"
          />
        </div>

        <div className="divider" />

        {/* Charts */}
        <div className="charts-grid">
          <IncidentTrendChart data={trendData} />
          <SeverityPieChart data={severityData} />
        </div>

        <div className="divider" />

        {/* Risk Posture */}
        <h2 className="section-title">🛡️ Current Risk Posture</h2>
        <div className="risk-grid">
          <RiskAssessment risks={riskData} />
          <ComplianceScorecard frameworks={complianceData} />
        </div>

        <div className="divider" />

        {/* Executive Summary */}
        <h2 className="section-title">📋 Executive Summary</h2>
        <ExecutiveSummary metrics={metrics} />

        {/* Footer */}
        <div className="footer">
          <div className="footer-title">
            🎯 Executive Security Dashboard | Report Generated: {currentDate}
          </div>
          <div>
            For detailed operational metrics, please refer to the full SOC dashboard
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
