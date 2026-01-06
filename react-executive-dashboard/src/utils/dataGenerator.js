/**
 * Generate executive-level metrics and KPIs
 * Mimics the Python version from executive_dashboard.py
 */

export const generateExecutiveData = () => {
  const random = (min, max) => Math.random() * (max - min) + min;
  const randomInt = (min, max) => Math.floor(random(min, max));

  const current = {
    totalIncidents: randomInt(80, 150),
    criticalIncidents: randomInt(5, 15),
    avgResponseTime: random(15, 45),
    resolvedRate: random(85, 98),
    falsePositiveRate: random(3, 12),
    securityScore: randomInt(75, 95),
    complianceScore: randomInt(88, 99),
    mttr: random(30, 120),  // Mean Time To Respond
    mttd: random(10, 60),   // Mean Time To Detect
    mttrResolve: random(240, 720),  // Mean Time To Resolve
  };

  const previous = Object.fromEntries(
    Object.entries(current).map(([key, value]) => [
      key,
      value * random(0.85, 1.15)
    ])
  );

  return { current, previous };
};

export const calculateDelta = (current, previous) => {
  if (previous === 0) return 0;
  return ((current - previous) / previous) * 100;
};

export const formatDelta = (delta, inverse = false) => {
  if (delta === 0) return { text: '0%', className: 'neutral' };

  let isPositive = delta > 0;
  if (inverse) isPositive = !isPositive;

  const sign = delta > 0 ? '+' : '';
  const className = isPositive ? 'delta-positive' : 'delta-negative';
  const icon = delta > 0 ? '▲' : '▼';

  return {
    text: `${icon} ${sign}${delta.toFixed(1)}%`,
    className
  };
};

export const generateTrendData = (days = 30) => {
  const data = [];
  const today = new Date();

  for (let i = days - 1; i >= 0; i--) {
    const date = new Date(today);
    date.setDate(date.getDate() - i);
    data.push({
      date: date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
      incidents: randomInt(2, 8)
    });
  }

  return data;
};

const randomInt = (min, max) => Math.floor(Math.random() * (max - min) + min);

export const generateSeverityData = () => {
  return [
    { name: 'Critical', value: randomInt(2, 15), color: '#EF4444' },
    { name: 'High', value: randomInt(10, 25), color: '#F59E0B' },
    { name: 'Medium', value: randomInt(20, 40), color: '#3B82F6' },
    { name: 'Low', value: randomInt(15, 30), color: '#10B981' }
  ];
};

export const generateRiskData = () => {
  return [
    {
      risk: 'Unpatched Systems',
      severity: 'Critical',
      affected: 24,
      trend: '▲'
    },
    {
      risk: 'Phishing Attempts',
      severity: 'High',
      affected: 156,
      trend: '▼'
    },
    {
      risk: 'Unauthorized Access Attempts',
      severity: 'High',
      affected: 89,
      trend: '▲'
    },
    {
      risk: 'Data Exfiltration Alerts',
      severity: 'Medium',
      affected: 12,
      trend: '▬'
    },
    {
      risk: 'Malware Detections',
      severity: 'Medium',
      affected: 34,
      trend: '▼'
    }
  ];
};

export const generateComplianceData = () => {
  return [
    { name: 'NIST CSF', score: 94 },
    { name: 'ISO 27001', score: 91 },
    { name: 'SOC 2', score: 96 },
    { name: 'GDPR', score: 88 },
    { name: 'HIPAA', score: 92 }
  ];
};
