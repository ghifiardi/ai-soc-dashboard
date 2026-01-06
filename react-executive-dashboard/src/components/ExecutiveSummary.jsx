import React from 'react';

const ExecutiveSummary = ({ metrics }) => {
  return (
    <div className="panel">
      <div className="summary-grid">
        <div className="summary-content">
          <h3>Key Findings</h3>

          <p>
            <strong>Security Posture:</strong> The organization's overall security posture remains <strong>strong</strong> with a security
            score of <strong>{metrics.current.securityScore}/100</strong>. Critical incident count has <strong>decreased by 12%</strong> compared to the previous period,
            indicating effective threat mitigation strategies.
          </p>

          <p>
            <strong>Operational Excellence:</strong> Mean Time to Detect (MTTD) improved by <strong>18%</strong> to <strong>{metrics.current.mttd.toFixed(0)} minutes</strong>,
            while Mean Time to Respond (MTTR) decreased to <strong>{metrics.current.mttr.toFixed(0)} minutes</strong>, demonstrating enhanced
            SOC operational efficiency.
          </p>

          <p>
            <strong>Compliance:</strong> All major compliance frameworks maintain scores above <strong>88%</strong>, with SOC 2
            achieving <strong>96%</strong> compliance. Continuous monitoring and quarterly audits ensure regulatory alignment.
          </p>

          <p><strong>Recommendations:</strong></p>
          <ul>
            <li>Prioritize patching of <strong>24 critical systems</strong> identified as high-risk</li>
            <li>Enhance phishing awareness training to reduce social engineering success rate</li>
            <li>Invest in advanced threat intelligence to improve proactive threat hunting</li>
          </ul>
        </div>

        <div className="quick-stats">
          <h3>Quick Stats</h3>

          <div className="stat-item">
            <div className="stat-label">Active Analysts</div>
            <div className="stat-value">
              12
              <span className="stat-delta delta-positive">+2</span>
            </div>
          </div>

          <div className="stat-item">
            <div className="stat-label">Security Tools</div>
            <div className="stat-value">
              24
              <span className="stat-delta delta-positive">+1</span>
            </div>
          </div>

          <div className="stat-item">
            <div className="stat-label">Automated Playbooks</div>
            <div className="stat-value">
              47
              <span className="stat-delta delta-positive">+5</span>
            </div>
          </div>

          <div className="stat-item">
            <div className="stat-label">Threat Intel Feeds</div>
            <div className="stat-value">
              15
              <span className="stat-delta delta-neutral">0</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ExecutiveSummary;
