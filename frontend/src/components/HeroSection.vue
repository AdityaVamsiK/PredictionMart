<template>
  <section id="home" class="relative min-h-screen flex items-center justify-center overflow-hidden">
    <!-- Background Pattern -->
    <div class="absolute inset-0 bg-gradient-to-br from-navy-900 via-navy-800 to-navy-900">
      <!-- Abstract Financial Graph Overlay -->
      <div class="absolute inset-0 opacity-10">
        <svg class="w-full h-full" viewBox="0 0 1200 800" fill="none">
          <!-- Grid lines -->
          <defs>
            <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
              <path d="M 40 0 L 0 0 0 40" fill="none" stroke="currentColor" stroke-width="1" opacity="0.1"/>
            </pattern>
          </defs>
          <rect width="1200" height="800" fill="url(#grid)" />
          
          <!-- Abstract chart lines -->
          <path 
            d="M 50 700 Q 200 500 350 600 T 650 400 T 950 300 T 1150 200" 
            stroke="currentColor" 
            stroke-width="3" 
            fill="none" 
            opacity="0.3"
          />
          <path 
            d="M 100 650 Q 250 550 400 500 T 700 450 T 1000 350 T 1100 250" 
            stroke="currentColor" 
            stroke-width="2" 
            fill="none" 
            opacity="0.2"
          />
          
          <!-- Data points -->
          <circle cx="200" cy="500" r="4" fill="currentColor" opacity="0.4"/>
          <circle cx="400" cy="450" r="4" fill="currentColor" opacity="0.4"/>
          <circle cx="600" cy="400" r="4" fill="currentColor" opacity="0.4"/>
          <circle cx="800" cy="350" r="4" fill="currentColor" opacity="0.4"/>
          <circle cx="1000" cy="300" r="4" fill="currentColor" opacity="0.4"/>
        </svg>
      </div>
    </div>

    <!-- Content -->
    <div class="relative z-10 container-custom text-center px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto">
        <!-- Main Headline -->
        <h1 class="text-4xl sm:text-5xl lg:text-6xl xl:text-7xl font-heading font-bold mb-6 leading-tight">
          <span class="block text-white">Trade on the Future.</span>
          <span class="block gradient-text">Discover the Market's Collective Wisdom.</span>
        </h1>

        <!-- Subtext -->
        <p class="text-xl sm:text-2xl text-gray-300 mb-8 max-w-3xl mx-auto leading-relaxed">
          PredictionMart lets you buy and sell shares on real-world events in tech, trade, 
          economics, and geopolitics. Prices reflect probabilities, powered by collective intelligence.
        </p>

        <!-- CTA Buttons -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
          <button class="btn-primary text-lg px-8 py-4 w-full sm:w-auto">
            Get Started
          </button>
          <button class="btn-secondary text-lg px-8 py-4 w-full sm:w-auto">
            Learn More
          </button>
        </div>

        <!-- Stats or Features -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-8 max-w-2xl mx-auto">
          <div class="text-center">
            <div class="text-3xl font-bold text-teal-400 mb-2">$1B+</div>
            <div class="text-gray-400">Volume Traded</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-emerald-400 mb-2">10K+</div>
            <div class="text-gray-400">Active Traders</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-teal-400 mb-2">95%</div>
            <div class="text-gray-400">Accuracy Rate</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Scroll Indicator -->
    <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
      <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>
      </svg>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HeroSection',
  mounted() {
    // Add scroll indicator click handler
    const scrollIndicator = document.querySelector('.animate-bounce')
    if (scrollIndicator) {
      scrollIndicator.addEventListener('click', () => {
        document.querySelector('#about')?.scrollIntoView({ behavior: 'smooth' })
      })
    }
  }
}
</script>
