# PredictionMart - Cutting-Edge Prediction Market Platform

A professional single-page website for PredictionMart, a cutting-edge prediction market platform built with Vue.js frontend.

## 🚀 Features

- **Modern Design**: Sleek fintech startup landing page with professional styling
- **Vue.js Frontend**: Reactive, component-based architecture with static data
- **Tailwind CSS**: Utility-first CSS framework with custom fintech color palette
- **Responsive Design**: Mobile-first approach with collapsible navigation
- **Interactive Widgets**: Payoff calculator and YouTube video embed
- **Professional Sections**: Hero, mission, personas, how-it-works, examples, and more

## 🎨 Design System

### Color Palette
- **Deep Navy Blue** (#0F172A) - Background
- **Teal** (#14B8A6) - Highlights and primary actions
- **Emerald Green** (#10B981) - Interactive elements
- **White** (#FFFFFF) - Text backgrounds
- **Light Gray** (#F1F5F9) - Section backgrounds

### Typography
- **Headings**: Inter/Poppins (bold sans-serif)
- **Body Text**: Roboto (clean sans-serif)

## 🏗️ Project Structure

```
PredictionMart/
├── frontend/
│   ├── src/
│   │   ├── components/       # Vue.js components
│   │   ├── App.vue          # Main Vue app
│   │   ├── main.js          # Vue app entry point
│   │   └── style.css        # Tailwind CSS styles
│   ├── package.json         # Node.js dependencies
│   ├── vite.config.js       # Vite configuration
│   ├── tailwind.config.js   # Tailwind configuration
│   ├── postcss.config.js    # PostCSS configuration
│   └── index.html           # Frontend HTML template
├── start_frontend.py        # Frontend startup script
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites
- Node.js 16+
- npm or yarn

### Frontend Setup (Vue.js)

#### Option 1: Using the Startup Script (Recommended)
```bash
python start_frontend.py
```

#### Option 2: Manual Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

### Production Build

To build for production:

```bash
cd frontend
npm run build
```

## 📱 Sections Overview

### 1. Hero Section
- Large headline: "Trade on the Future. Discover the Market's Collective Wisdom."
- Subtext explaining the platform
- Call-to-action buttons
- Abstract financial graph background

### 2. Mission Statement
- Platform mission with key values (Transparent, Fair, Liquid)
- Professional card layout with icons

### 3. Target Personas
- Individual Traders
- Researchers & Analysts  
- Institutions
- Each with descriptions and use cases

### 4. How It Works
- 4-step process with icons and examples
- Visual connection lines
- Detailed explanations

### 5. Concept Explainers
- Event Definition
- Trading Contracts
- Price = Probability
- Settlement
- Each with examples and formulas

### 6. Example Transactions
- Real worked examples with calculations
- Winning and losing trade scenarios
- ROI calculations and insights

### 7. Payoff Calculator Widget
- Interactive form with real-time calculations
- Client-side calculation logic
- Quick example buttons
- Risk warnings

### 8. YouTube Widget
- Embedded explainer video
- Additional learning resources
- Community links

### 9. Call to Action
- Join waitlist form
- Contact information collection
- Trust indicators

## 🔧 Data & Functionality

### Static Data
All data is now stored directly in Vue.js components:
- Example transactions
- Target personas
- How-it-works steps
- Contact form (simulated submission)

### Payoff Calculator
The payoff calculator now performs calculations client-side using JavaScript:
- Real-time calculations as user types
- Formula: `shares = investment / price`, `payoff = shares * $1`
- ROI calculation: `(payoff - investment) / investment * 100`

## 🎯 Key Features

### Payoff Calculator
- Real-time calculations as user types
- Formula display and explanations
- Quick example scenarios
- Risk warnings and disclaimers

### Responsive Design
- Mobile-first approach
- Collapsible hamburger menu
- Stacking cards on mobile
- Optimized widgets for small screens

### Professional Styling
- Smooth animations and transitions
- Hover effects and micro-interactions
- Gradient text effects
- Glass morphism elements

## 🚀 Deployment

### GitHub Pages
The site is designed to be hosted on GitHub Pages. To deploy:

1. Build the frontend:
```bash
cd frontend
npm run build
```

2. Copy the `dist` folder contents to your GitHub Pages repository

### Static Hosting
Since this is now a static site, you can deploy it to any static hosting service:
- Netlify
- Vercel
- AWS S3 + CloudFront
- Firebase Hosting

## 📄 License

This project is created for demonstration purposes. Please ensure compliance with applicable laws and regulations when implementing prediction markets.

## ⚠️ Disclaimer

This is a demonstration website. PredictionMart is for entertainment and educational purposes only. Trading involves risk and may not be suitable for all individuals. Please invest responsibly and only trade with money you can afford to lose.

## 🤝 Contributing

This is a demonstration project. For production use, please ensure proper security measures, legal compliance, and thorough testing.

---

Built with ❤️ using Vue.js and Tailwind CSS
