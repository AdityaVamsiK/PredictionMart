<template>
  <div id="app" class="min-h-screen bg-navy-900">
    <!-- Navigation -->
    <NavBar />
    
    <!-- Hero Section -->
    <HeroSection />
    
    <!-- Mission Statement -->
    <MissionStatement />
    
    <!-- Target Personas -->
    <TargetPersonas />
    
    <!-- How It Works -->
    <HowItWorks />
    
    <!-- Concept Explainers -->
    <ConceptExplainers />
    
    <!-- Example Transactions -->
    <ExampleTransactions />
    
    <!-- Payoff Calculator Widget -->
    <PayoffCalculator />
    
    <!-- YouTube Widget -->
    <YouTubeWidget />
    
    <!-- Call to Action -->
    <CallToAction />
    
    <!-- Footer -->
    <Footer />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import MissionStatement from './components/MissionStatement.vue'
import TargetPersonas from './components/TargetPersonas.vue'
import HowItWorks from './components/HowItWorks.vue'
import ConceptExplainers from './components/ConceptExplainers.vue'
import ExampleTransactions from './components/ExampleTransactions.vue'
import PayoffCalculator from './components/PayoffCalculator.vue'
import YouTubeWidget from './components/YouTubeWidget.vue'
import CallToAction from './components/CallToAction.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    HeroSection,
    MissionStatement,
    TargetPersonas,
    HowItWorks,
    ConceptExplainers,
    ExampleTransactions,
    PayoffCalculator,
    YouTubeWidget,
    CallToAction,
    Footer
  }
}
</script>
