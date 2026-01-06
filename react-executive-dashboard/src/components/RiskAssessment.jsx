import React from 'react';

const RiskAssessment = ({ risks }) => {
  return (
    <div className="panel">
      <div className="panel-title">Top Security Risks</div>
      {risks.map((risk, index) => (
        <div key={index} className="risk-item">
          <div className="risk-info">
            <div className="risk-name">{risk.risk}</div>
            <div className="risk-meta">
              <span className={`risk-badge ${risk.severity.toLowerCase()}`}>
                {risk.severity}
              </span>
              <span className="risk-affected">
                {risk.affected} affected assets
              </span>
            </div>
          </div>
          <div className="risk-trend">{risk.trend}</div>
        </div>
      ))}
    </div>
  );
};

export default RiskAssessment;
