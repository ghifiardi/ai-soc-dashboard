import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Area, AreaChart } from 'recharts';

const IncidentTrendChart = ({ data }) => {
  return (
    <div className="panel">
      <div className="panel-title">📈 Incident Trend (30 Days)</div>
      <ResponsiveContainer width="100%" height={300}>
        <AreaChart data={data}>
          <defs>
            <linearGradient id="colorIncidents" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#3B82F6" stopOpacity={0.3}/>
              <stop offset="95%" stopColor="#3B82F6" stopOpacity={0}/>
            </linearGradient>
          </defs>
          <CartesianGrid strokeDasharray="3 3" stroke="#E2E8F0" />
          <XAxis
            dataKey="date"
            stroke="#64748B"
            style={{ fontSize: '0.875rem' }}
          />
          <YAxis
            stroke="#64748B"
            style={{ fontSize: '0.875rem' }}
          />
          <Tooltip
            contentStyle={{
              backgroundColor: 'white',
              border: '1px solid #E2E8F0',
              borderRadius: '8px',
              boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)'
            }}
          />
          <Area
            type="monotone"
            dataKey="incidents"
            stroke="#3B82F6"
            strokeWidth={3}
            fill="url(#colorIncidents)"
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
};

export default IncidentTrendChart;
