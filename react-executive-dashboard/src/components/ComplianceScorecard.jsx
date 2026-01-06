import React from 'react';

const ComplianceScorecard = ({ frameworks }) => {
  const getScoreClass = (score) => {
    if (score >= 90) return 'high';
    if (score >= 75) return 'medium';
    return 'low';
  };

  const getBarColor = (score) => {
    if (score >= 90) return '#10B981';
    if (score >= 75) return '#F59E0B';
    return '#EF4444';
  };

  return (
    <div className="panel">
      <div className="panel-title">Compliance Status</div>
      {frameworks.map((fw, index) => (
        <div key={index} className="compliance-item">
          <div className="compliance-header">
            <span className="compliance-name">{fw.name}</span>
            <span className={`compliance-score ${getScoreClass(fw.score)}`}>
              {fw.score}%
            </span>
          </div>
          <div className="compliance-bar-container">
            <div
              className="compliance-bar"
              style={{
                width: `${fw.score}%`,
                backgroundColor: getBarColor(fw.score)
              }}
            />
          </div>
        </div>
      ))}
    </div>
  );
};

export default ComplianceScorecard;
