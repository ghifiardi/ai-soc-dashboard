# Executive Security Dashboard - React Version

A modern, professional React implementation of the Executive SOC Dashboard, designed for C-suite executives and management to monitor security posture and operational metrics.

## 🎯 Features

### Key Performance Indicators
- **Total Incidents** - Overall incident count with period-over-period comparison
- **Critical Incidents** - High-priority security events tracking
- **Resolution Rate** - Percentage of successfully resolved incidents
- **Security Score** - Overall security posture rating (0-100)

### Operational Metrics
- **Mean Time to Detect (MTTD)** - Average time to identify security threats
- **Mean Time to Respond (MTTR)** - Average response time to incidents
- **Mean Time to Resolve** - Average time to fully resolve incidents

### Visualizations
- **30-Day Incident Trend** - Historical incident patterns with area chart
- **Severity Distribution** - Pie chart showing incident breakdown by severity
- **Risk Assessment Panel** - Top 5 security risks with severity badges
- **Compliance Scorecard** - Multi-framework compliance status with progress bars

### Executive Summary
- Key findings and security posture overview
- Operational excellence metrics
- Compliance status summary
- Actionable recommendations
- Quick stats (analysts, tools, playbooks, threat intel feeds)

## 🚀 Quick Start

### Prerequisites
- Node.js 18.x or higher
- npm or yarn package manager

### Installation

1. Navigate to the React dashboard directory:
```bash
cd react-executive-dashboard
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser to:
```
http://localhost:3000
```

### Production Build

To create an optimized production build:

```bash
npm run build
```

The build artifacts will be stored in the `dist/` directory.

To preview the production build locally:

```bash
npm run preview
```

## 📁 Project Structure

```
react-executive-dashboard/
├── src/
│   ├── components/
│   │   ├── KPICard.jsx                    # Reusable KPI metric card
│   │   ├── IncidentTrendChart.jsx         # 30-day trend line chart
│   │   ├── SeverityPieChart.jsx           # Incident severity pie chart
│   │   ├── RiskAssessment.jsx             # Top risks panel
│   │   ├── ComplianceScorecard.jsx        # Compliance framework scores
│   │   └── ExecutiveSummary.jsx           # Executive summary section
│   ├── utils/
│   │   └── dataGenerator.js               # Mock data generation utilities
│   ├── App.jsx                            # Main application component
│   ├── App.css                            # Global styles and theme
│   └── main.jsx                           # Application entry point
├── index.html                             # HTML template
├── vite.config.js                         # Vite configuration
├── package.json                           # Project dependencies
└── README.md                              # This file
```

## 🎨 Design & Styling

### Theme
- **Light Professional Theme** - Clean white panels on gradient background
- **Color Palette**:
  - Navy (#1E293B) - Primary text and headings
  - Blue (#3B82F6) - Primary accent and data visualization
  - Green (#10B981) - Positive trends and success states
  - Red (#EF4444) - Critical alerts and negative trends
  - Amber (#F59E0B) - Warnings and medium-priority items
  - Gray (#64748B) - Secondary text and subtle elements

### Typography
- **Font Family**: Inter (Google Fonts)
- **Weight Range**: 300-800 (Light to Extra Bold)
- Optimized for readability and professional appearance

### Responsive Design
- Fully responsive grid layouts
- Mobile-friendly breakpoints
- Adaptive charts and visualizations

## 🔧 Technology Stack

- **React 18.3.1** - UI framework
- **Vite 5.3.1** - Build tool and dev server
- **Recharts 2.12.0** - Charting library for data visualization
- **CSS3** - Custom styling with CSS variables

## 📊 Data Management

### Mock Data Generation
The dashboard uses client-side mock data generation to simulate real-time metrics. This approach:
- Generates randomized but realistic metrics on each page load
- Calculates period-over-period deltas automatically
- Provides consistent data structure for all visualizations

### Integrating Real Data

To connect the dashboard to real data sources, modify `src/utils/dataGenerator.js`:

1. **Replace mock functions** with API calls:
```javascript
export const generateExecutiveData = async () => {
  const response = await fetch('/api/executive-metrics');
  return response.json();
};
```

2. **Update App.jsx** to handle async data:
```javascript
useEffect(() => {
  const fetchData = async () => {
    const metricsData = await generateExecutiveData();
    setMetrics(metricsData);
  };
  fetchData();
}, []);
```

3. **Add real-time updates** with polling or WebSockets:
```javascript
useEffect(() => {
  const interval = setInterval(fetchData, 60000); // Update every minute
  return () => clearInterval(interval);
}, []);
```

## 🔄 Comparison with Streamlit Version

### Similarities
- **Identical visual design** - Matches the professional light theme
- **Same KPIs and metrics** - All executive-level metrics preserved
- **Equivalent visualizations** - Charts and data displays match 1:1
- **Consistent data structure** - Uses the same data model

### React Advantages
- **Better performance** - Faster rendering and smoother interactions
- **Enhanced interactivity** - More responsive user interactions
- **Easier integration** - Simpler to connect with modern APIs and services
- **Deployment flexibility** - Can be hosted on any static hosting service
- **Component reusability** - Modular architecture for easy customization

### When to Use Each

**Use Streamlit Version When:**
- Python backend integration is primary
- Rapid prototyping is needed
- Team is primarily Python developers
- BigQuery integration is required

**Use React Version When:**
- Frontend performance is critical
- Modern web stack integration needed
- Standalone web application desired
- Extensive customization required
- Mobile responsiveness is priority

## 🚢 Deployment Options

### Static Hosting (Recommended)
Deploy to any static hosting provider:

- **Vercel**: `vercel deploy`
- **Netlify**: Drag and drop the `dist/` folder
- **GitHub Pages**: Configure with GitHub Actions
- **AWS S3**: Upload to S3 bucket with static website hosting
- **Azure Static Web Apps**: Deploy with Azure CLI

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Build and run:
```bash
docker build -t executive-dashboard-react .
docker run -p 80:80 executive-dashboard-react
```

## 🔐 Security Considerations

- All data is client-side by default (no sensitive data exposure)
- CORS must be configured when connecting to APIs
- Use HTTPS in production environments
- Implement authentication/authorization as needed
- Follow OWASP guidelines for web application security

## 🤝 Contributing

To contribute enhancements:

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📝 License

Part of the AI SOC Dashboard suite. See main project README for license information.

## 🆘 Support

For issues or questions:
- Check the main project documentation
- Review existing GitHub issues
- Create a new issue with detailed information

## 🔮 Future Enhancements

Potential additions:
- Real-time data integration with WebSocket support
- Advanced filtering and date range selection
- Export functionality (PDF, CSV, Excel)
- User authentication and role-based access control
- Dark mode theme toggle
- Customizable dashboard layouts
- Alert notifications and email reports
- Integration with SIEM platforms
- Multi-tenant support
- Historical data comparison views

---

**Version**: 1.0.0
**Last Updated**: January 2026
**Maintained by**: AI SOC Dashboard Team
