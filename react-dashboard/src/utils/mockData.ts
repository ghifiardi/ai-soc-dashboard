import { SecurityEvent, ThreatHunt, SocialMediaThreat, MLClassification } from '../types/dashboard';

export const generateSecurityEvents = (count: number = 100): SecurityEvent[] => {
  const events: SecurityEvent[] = [];

  const threatTypes = [
    'Advanced Persistent Threat',
    'Malware Infection',
    'Phishing Attack',
    'DDoS Attack',
    'Data Exfiltration',
    'Insider Threat',
    'Ransomware',
    'SQL Injection',
    'XSS Attack',
    'Zero-Day Exploit',
    'Brute Force',
    'Man-in-the-Middle',
  ];

  const severities: Array<'Critical' | 'High' | 'Medium' | 'Low'> = ['Critical', 'High', 'Medium', 'Low'];
  const severityWeights = [0.15, 0.25, 0.35, 0.25];

  const sources = [
    '185.220.101.45',
    '203.0.113.45',
    '198.51.100.10',
    '45.142.214.123',
    '91.205.189.15',
    '103.251.167.20',
  ];

  const destinations = [
    '192.168.1.100',
    '192.168.1.50',
    '10.0.0.10',
    '172.16.0.5',
    '192.168.2.75',
  ];

  const statuses: Array<'Active' | 'Investigating' | 'Contained' | 'Resolved' | 'False Positive'> = [
    'Active',
    'Investigating',
    'Contained',
    'Resolved',
    'False Positive',
  ];

  const countries = ['China', 'Russia', 'North Korea', 'Iran', 'Unknown', 'Brazil', 'Nigeria'];

  for (let i = 0; i < count; i++) {
    const severity = weightedRandom(severities, severityWeights);
    const timeRange = severity === 'Critical' ? 30 : severity === 'High' ? 120 : severity === 'Medium' ? 360 : 720;
    const timestamp = new Date(Date.now() - Math.random() * timeRange * 60 * 1000);

    events.push({
      id: `evt-${i}`,
      timestamp,
      eventId: `EVT-${Math.floor(Math.random() * 900000) + 100000}`,
      severity,
      eventType: threatTypes[Math.floor(Math.random() * threatTypes.length)],
      sourceIp: sources[Math.floor(Math.random() * sources.length)],
      destinationIp: destinations[Math.floor(Math.random() * destinations.length)],
      sourceCountry: countries[Math.floor(Math.random() * countries.length)],
      status: statuses[Math.floor(Math.random() * statuses.length)],
      mitreTechnique: `T${Math.floor(Math.random() * 1500) + 1000}.${Math.floor(Math.random() * 10).toString().padStart(3, '0')}`,
      confidence: Math.random() * 0.34 + 0.65,
      packets: Math.floor(Math.random() * 99000) + 1000,
      bytesTransferred: Math.floor(Math.random() * 10485760) + 1024,
      protocol: ['HTTP', 'HTTPS', 'SSH', 'FTP', 'SMB', 'DNS'][Math.floor(Math.random() * 6)],
      threatActor: ['APT28', 'APT29', 'Lazarus Group', 'FIN7', 'Unknown'][Math.floor(Math.random() * 5)],
      affectedAsset: `Server-${Math.floor(Math.random() * 10) + 1}`,
      analystAssigned: Math.random() > 0.5 ? `Analyst ${Math.floor(Math.random() * 8) + 1}` : undefined,
      responseTimeMin: Math.random() > 0.3 ? Math.floor(Math.random() * 120) + 1 : undefined,
      falsePositiveScore: Math.random(),
    });
  }

  return events.sort((a, b) => b.timestamp.getTime() - a.timestamp.getTime());
};

export const generateThreatHunts = (count: number = 10): ThreatHunt[] => {
  const hunts: ThreatHunt[] = [];

  const huntTypes = [
    'Insider Threat Detection',
    'APT Campaign Tracking',
    'Credential Theft Investigation',
    'Lateral Movement Analysis',
    'Command & Control Hunt',
    'Data Exfiltration Search',
    'Malware Family Investigation',
    'Zero-Day Vulnerability Hunt',
  ];

  const statuses: Array<'Active' | 'Investigating' | 'Completed' | 'On Hold'> = [
    'Active',
    'Investigating',
    'Completed',
    'On Hold',
  ];

  const priorities: Array<'Critical' | 'High' | 'Medium' | 'Low'> = ['Critical', 'High', 'Medium', 'Low'];

  for (let i = 0; i < count; i++) {
    const daysAgo = Math.floor(Math.random() * 30);
    const startDate = new Date(Date.now() - daysAgo * 24 * 60 * 60 * 1000);

    hunts.push({
      missionId: `HUNT-2026${Math.floor(Math.random() * 9000) + 1000}`,
      huntType: huntTypes[Math.floor(Math.random() * huntTypes.length)],
      startDate,
      status: statuses[Math.floor(Math.random() * statuses.length)],
      iocsFound: Math.floor(Math.random() * 50),
      entitiesAnalyzed: Math.floor(Math.random() * 4900) + 100,
      confidence: Math.random() * 0.35 + 0.60,
      priority: priorities[Math.floor(Math.random() * priorities.length)],
      hunter: `Analyst ${Math.floor(Math.random() * 10) + 1}`,
    });
  }

  return hunts.sort((a, b) => b.startDate.getTime() - a.startDate.getTime());
};

export const generateSocialMediaThreats = (count: number = 50): SocialMediaThreat[] => {
  const threats: SocialMediaThreat[] = [];

  const texts = [
    'IOH paket internet mahal banget, mending pindah ke kompetitor aja',
    'Indosat jaringan down lagi nih, gak bisa internet! #IM3 #gangguan',
    'XL lemot banget hari ini, ada yang ngalamin juga?',
    'Telkomsel error terus, jaringan down di area Jakarta',
    'Ada data breach di perusahaan X, password leaked!',
    'Hati-hati malware baru menyebar via email phishing',
    'Website perusahaan Y kena DDoS attack, down total',
    'Ransomware attack hits major corporation, data encrypted',
  ];

  const platforms: Array<'Twitter' | 'Facebook' | 'Instagram' | 'LinkedIn' | 'Reddit'> = [
    'Twitter',
    'Facebook',
    'Instagram',
    'LinkedIn',
    'Reddit',
  ];

  const severities: Array<'High' | 'Medium' | 'Low'> = ['High', 'Medium', 'Low'];

  for (let i = 0; i < count; i++) {
    const minutesAgo = Math.floor(Math.random() * 2880); // Last 48 hours
    const createdAt = new Date(Date.now() - minutesAgo * 60 * 1000);

    threats.push({
      id: `smt-${i}`,
      createdAt,
      text: texts[Math.floor(Math.random() * texts.length)],
      threatScore: Math.random() * 0.4 + 0.5,
      severity: severities[Math.floor(Math.random() * severities.length)],
      keywordsFound: ['IOH', 'mahal', 'paket', 'internet'],
      platform: platforms[Math.floor(Math.random() * platforms.length)],
      engagement: Math.floor(Math.random() * 4990) + 10,
      verifiedThreat: Math.random() > 0.5,
    });
  }

  return threats.sort((a, b) => b.createdAt.getTime() - a.createdAt.getTime());
};

export const generateMLClassifications = (count: number = 30): MLClassification[] => {
  const classifications: MLClassification[] = [];

  const models = [
    'Random Forest Classifier',
    'Neural Network',
    'Gradient Boosting',
    'Deep Learning CNN',
    'XGBoost Classifier',
    'Isolation Forest',
    'Autoencoder Anomaly',
  ];

  const categories = [
    'Malware',
    'Network Intrusion',
    'Data Breach',
    'Insider Threat',
    'DDoS Attack',
    'Phishing',
    'Ransomware',
    'Zero-Day',
  ];

  for (let i = 0; i < count; i++) {
    classifications.push({
      model: models[Math.floor(Math.random() * models.length)],
      category: categories[Math.floor(Math.random() * categories.length)],
      confidence: Math.random() * 0.29 + 0.70,
      truePositiveRate: Math.random() * 0.20 + 0.75,
      falsePositiveRate: Math.random() * 0.13 + 0.02,
      predictions: Math.floor(Math.random() * 450) + 50,
    });
  }

  return classifications;
};

// Helper function for weighted random selection
function weightedRandom<T>(items: T[], weights: number[]): T {
  const total = weights.reduce((sum, weight) => sum + weight, 0);
  let random = Math.random() * total;

  for (let i = 0; i < items.length; i++) {
    random -= weights[i];
    if (random <= 0) {
      return items[i];
    }
  }

  return items[items.length - 1];
}

// Format helpers
export const formatTimestamp = (date: Date): string => {
  return date.toLocaleString('en-US', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false,
  });
};

export const formatNumber = (num: number): string => {
  return num.toLocaleString('en-US');
};

export const formatBytes = (bytes: number): string => {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i];
};

export const formatPercentage = (value: number): string => {
  return `${(value * 100).toFixed(1)}%`;
};
