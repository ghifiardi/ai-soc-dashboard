import React from 'react';

const KPICard = ({ label, value, delta, borderColor = 'blue' }) => {
  return (
    <div className={`kpi-card border-${borderColor}`}>
      <div className="kpi-label">{label}</div>
      <div className="kpi-value">{value}</div>
      <div className={`kpi-delta ${delta.className}`}>
        {delta.text} vs previous
      </div>
    </div>
  );
};

export default KPICard;
