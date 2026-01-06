# AI-SOC Dashboard - React + TypeScript Edition 🛡️

Modern, high-performance Security Operations Center dashboard suite built with React, TypeScript, and cutting-edge web technologies.

## 🚀 Tech Stack

### Core
- **React 18** - Modern React with hooks and concurrent features
- **TypeScript 5** - Full type safety and improved developer experience
- **Vite** - Lightning-fast build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework

### State & Data
- **Zustand** - Lightweight state management
- **TanStack Query** - Powerful data fetching and caching
- **Axios** - Promise-based HTTP client

### Visualization
- **Recharts** - Composable charting library
- **Plotly.js** - Interactive scientific charts
- **React-Plotly.js** - React wrapper for Plotly

### UI/UX
- **Framer Motion** - Production-ready animation library
- **Lucide React** - Beautiful icon library
- **date-fns** - Modern date utility library

## 📦 Installation

```bash
cd react-dashboard

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 🎯 Features

### Enhanced Performance
- ⚡ **Vite** for instant HMR and optimized builds
- 🔄 **Virtual scrolling** for large datasets
- 📦 **Code splitting** for optimal loading
- 🎨 **CSS-in-JS** with Tailwind for minimal runtime
- 🚀 **React.memo** and **useMemo** for optimized re-renders

### Improved UX
- 🎭 **Smooth animations** with Framer Motion
- 📱 **Fully responsive** design
- ♿ **Accessible** components (ARIA labels, keyboard navigation)
- 🌓 **Dark mode** native support
- 🔍 **Real-time search** and filtering
- 📊 **Interactive charts** with drill-down capabilities

### Type Safety
- 🛡️ **Full TypeScript** coverage
- 📝 **Interface definitions** for all data models
- 🔒 **Compile-time** error catching
- 💡 **IntelliSense** support throughout

### Developer Experience
- 🎯 **Path aliases** (@/components, @/hooks, etc.)
- 🔥 **Hot Module Replacement** (HMR)
- 📦 **Component-based** architecture
- 🧪 **ESLint** configuration
- 🎨 **Prettier** for code formatting

## 📂 Project Structure

```
react-dashboard/
├── src/
│   ├── components/
│   │   ├── common/          # Reusable UI components
│   │   │   ├── MetricCard.tsx
│   │   │   ├── DataTable.tsx
│   │   │   ├── LoadingSpinner.tsx
│   │   │   └── ErrorBoundary.tsx
│   │   ├── dashboards/      # Dashboard-specific components
│   │   │   ├── EnhancedSOC/
│   │   │   ├── Executive/
│   │   │   ├── Compliance/
│   │   │   └── ThreatHunting/
│   │   └── charts/          # Chart components
│   │       ├── ThreatTimeline.tsx
│   │       ├── NetworkTopology.tsx
│   │       └── MitreHeatmap.tsx
│   ├── hooks/               # Custom React hooks
│   │   ├── useSecurityEvents.ts
│   │   ├── useThreatHunts.ts
│   │   └── useAutoRefresh.ts
│   ├── store/               # Zustand state management
│   │   ├── dashboardStore.ts
│   │   └── authStore.ts
│   ├── types/               # TypeScript type definitions
│   │   └── dashboard.ts
│   ├── utils/               # Utility functions
│   │   ├── mockData.ts
│   │   └── formatters.ts
│   ├── pages/               # Page components
│   │   ├── EnhancedSOCPage.tsx
│   │   ├── ExecutivePage.tsx
│   │   ├── CompliancePage.tsx
│   │   └── ThreatHuntingPage.tsx
│   ├── App.tsx              # Main app component
│   ├── main.tsx             # App entry point
│   └── index.css            # Global styles
├── public/                  # Static assets
├── index.html              # HTML template
├── vite.config.ts          # Vite configuration
├── tailwind.config.js      # Tailwind configuration
├── tsconfig.json           # TypeScript configuration
└── package.json            # Dependencies and scripts
```

## 🎨 Available Dashboards

### 1. Enhanced SOC Dashboard
**Route:** `/enhanced`

Advanced operational dashboard with:
- Real-time threat timeline
- Network topology visualization
- MITRE ATT&CK heatmap
- Geographic threat distribution
- Incident response funnel
- AI-powered analytics

### 2. Executive Dashboard
**Route:** `/executive`

Strategic overview with:
- Executive KPIs
- Performance metrics (MTTD, MTTR)
- 30-day trend analysis
- Risk assessment
- Compliance scorecard
- Executive summary

### 3. Compliance Dashboard
**Route:** `/compliance`

Regulatory tracking with:
- Multi-framework compliance (NIST, ISO, SOC 2, GDPR, HIPAA)
- Control status tracking
- Audit trail management
- Compliance trends
- Export capabilities

### 4. Threat Hunting Dashboard
**Route:** `/threat-hunting`

Proactive hunting with:
- AI/ML-powered alert analysis
- Active hunt mission tracking
- Social media threat monitoring
- IOC tracking
- Hunt metrics and KPIs

## 🔧 Configuration

### Environment Variables

Create a `.env` file:

```env
VITE_API_URL=http://localhost:8000
VITE_BIGQUERY_ENABLED=false
VITE_AUTO_REFRESH=true
VITE_REFRESH_INTERVAL=30000
```

### Tailwind Customization

Modify `tailwind.config.js` to customize colors, fonts, and animations:

```javascript
theme: {
  extend: {
    colors: {
      primary: {
        dark: '#0A0E27',
        blue: '#0066FF',
        cyan: '#00D4FF',
      },
    },
  },
}
```

## 🔌 API Integration

### Backend Setup (Optional)

Create a FastAPI or Flask backend:

```python
# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/events")
async def get_events():
    # Return security events
    return events_data
```

### Frontend API Client

```typescript
// src/api/client.ts
import axios from 'axios';

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000,
});

export const getSecurityEvents = async () => {
  const response = await apiClient.get('/api/events');
  return response.data;
};
```

## 🚀 Deployment

### Build for Production

```bash
npm run build
```

This creates an optimized production build in the `dist/` folder.

### Deploy to Vercel

```bash
npm install -g vercel
vercel
```

### Deploy to Netlify

```bash
npm install -g netlify-cli
netlify deploy --prod --dir=dist
```

### Deploy to GitHub Pages

```bash
# Add to package.json
"homepage": "https://yourusername.github.io/ai-soc-dashboard",

# Install gh-pages
npm install --save-dev gh-pages

# Add deploy script
"scripts": {
  "deploy": "npm run build && gh-pages -d dist"
}

# Deploy
npm run deploy
```

## 🎯 Performance Optimizations

### Implemented
- ✅ Code splitting with React.lazy
- ✅ Memoization with React.memo and useMemo
- ✅ Virtual scrolling for large lists
- ✅ Debounced search and filters
- ✅ Optimized re-renders
- ✅ Tree-shaking with Vite
- ✅ Asset optimization
- ✅ Service Worker (PWA-ready)

### Lighthouse Scores (Target)
- Performance: 95+
- Accessibility: 100
- Best Practices: 100
- SEO: 100

## 🔐 Security Features

- 🔒 Content Security Policy (CSP)
- 🛡️ XSS protection
- 🚫 CSRF protection
- 🔐 Secure headers
- ✅ Input validation
- 🔑 Authentication ready (JWT/OAuth)

## 🧪 Testing (Recommended Setup)

```bash
# Install testing libraries
npm install --save-dev vitest @testing-library/react @testing-library/jest-dom

# Add test script to package.json
"scripts": {
  "test": "vitest",
  "test:ui": "vitest --ui"
}
```

## 📊 vs Python Streamlit Version

| Feature | React + TypeScript | Python Streamlit |
|---------|-------------------|------------------|
| Performance | ⚡ Fast (client-side) | 🐢 Slower (server-side) |
| Type Safety | ✅ Full TypeScript | ❌ Python types limited |
| Customization | 🎨 Complete control | 🎨 Limited by Streamlit |
| Deployment | 🚀 Static hosting | 🖥️ Requires Python server |
| Interactivity | 🖱️ Instant | ⏱️ Server round-trips |
| Scalability | 📈 Horizontal | 📊 Vertical (server-dependent) |
| Offline Support | ✅ PWA capable | ❌ Requires server |
| Mobile UX | 📱 Optimized | 📱 Basic responsive |
| Learning Curve | 📚 Steeper | 📚 Easier |
| Dev Experience | 🔥 HMR, TypeScript | 🔄 Auto-reload |

## 🎁 Bonus Features

### PWA Support
Add manifest.json for Progressive Web App:

```json
{
  "name": "AI-SOC Dashboard",
  "short_name": "SOC",
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#0A0E27",
  "background_color": "#0A0E27",
  "icons": [...]
}
```

### Keyboard Shortcuts

- `Ctrl/Cmd + K` - Search
- `Ctrl/Cmd + R` - Refresh data
- `Ctrl/Cmd + D` - Toggle dark mode
- `Ctrl/Cmd + ,` - Settings
- `/` - Focus search

### Export Capabilities

- 📄 PDF export (using jsPDF)
- 📊 CSV export
- 📋 JSON export
- 🖼️ PNG/SVG chart export

## 🤝 Contributing

```bash
# Fork and clone
git clone https://github.com/yourusername/ai-soc-dashboard.git

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push and create PR
git push origin feature/amazing-feature
```

## 📝 License

MIT License - see LICENSE file

## 🆘 Support

- 📖 Documentation: [Full docs](https://docs.ai-soc.example.com)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/ai-soc-dashboard/discussions)
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/ai-soc-dashboard/issues)

## 🎉 Next Steps

1. **Install dependencies**: `npm install`
2. **Start dev server**: `npm run dev`
3. **Open browser**: `http://localhost:3000`
4. **Explore dashboards**: Navigate between routes
5. **Customize**: Modify components and styles
6. **Deploy**: Build and deploy to your platform

---

**Built with ❤️ using React + TypeScript**

**Version:** 2.0.0
**Last Updated:** January 6, 2026
**Maintainer:** Development Team
