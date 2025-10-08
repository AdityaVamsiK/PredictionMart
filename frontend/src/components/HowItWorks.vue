<template>
  <section id="how-it-works" class="section-padding bg-gray-50">
    <div class="container-custom">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-heading font-bold text-gray-900 mb-6">
          How It Works
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          PredictionMart makes trading on future events simple and intuitive. 
          Here's how the process works in four easy steps.
        </p>
      </div>

      <div class="relative">
        <!-- Connection lines for desktop -->
        <div class="hidden lg:block absolute top-24 left-0 right-0 h-0.5 bg-gradient-to-r from-teal-500 via-emerald-500 to-teal-500 opacity-30"></div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div 
            v-for="(step, index) in steps" 
            :key="step.id"
            class="relative"
          >
            <!-- Step Card -->
            <div class="card p-8 text-center group hover:scale-105 transition-all duration-300">
              <!-- Step Number -->
              <div class="absolute -top-4 left-1/2 transform -translate-x-1/2">
                <div class="w-12 h-12 bg-gradient-to-r from-teal-500 to-emerald-500 rounded-full flex items-center justify-center text-white font-bold text-lg shadow-lg">
                  {{ step.id }}
                </div>
              </div>

              <!-- Icon -->
              <div class="mt-8 mb-6">
                <div class="w-16 h-16 mx-auto rounded-full flex items-center justify-center transition-colors duration-300"
                     :class="getStepIconBg(step.icon)">
                  <svg class="w-8 h-8" :class="getStepIconColor(step.icon)" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path v-if="step.icon === 'event'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
                    <path v-else-if="step.icon === 'trade'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
                    <path v-else-if="step.icon === 'price'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                    <path v-else-if="step.icon === 'settlement'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </div>
              </div>

              <!-- Content -->
              <h3 class="text-xl font-heading font-bold text-gray-900 mb-4">
                {{ step.title }}
              </h3>
              
              <p class="text-gray-600 leading-relaxed">
                {{ step.description }}
              </p>

              <!-- Example for each step -->
              <div class="mt-6 p-4 bg-gray-50 rounded-lg">
                <div class="text-sm text-gray-500 mb-2">Example:</div>
                <div class="text-sm text-gray-700 font-medium">
                  <span v-if="step.icon === 'event'">"Will Tesla stock reach $300 by Dec 2024?"</span>
                  <span v-else-if="step.icon === 'trade'">Buy 100 "Yes" shares at $0.65 each</span>
                  <span v-else-if="step.icon === 'price'">$0.65 = 65% probability</span>
                  <span v-else-if="step.icon === 'settlement'">If Yes: $100 payout, $35 profit</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Additional Info -->
      <div class="mt-16 text-center">
        <div class="bg-white rounded-2xl shadow-lg p-8 max-w-4xl mx-auto">
          <h3 class="text-2xl font-heading font-bold text-gray-900 mb-4">
            Why Prediction Markets Work
          </h3>
          <p class="text-gray-600 mb-6">
            Prediction markets aggregate information from diverse participants, creating more accurate 
            forecasts than individual experts. The wisdom of crowds, combined with financial incentives, 
            leads to remarkably precise probability estimates.
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center">
                <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
              </div>
              <span class="text-gray-700">Crowdsourced Intelligence</span>
            </div>
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center">
                <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
              </div>
              <span class="text-gray-700">Real-time Price Discovery</span>
            </div>
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center">
                <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
              </div>
              <span class="text-gray-700">Financial Incentives</span>
            </div>
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center">
                <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
              </div>
              <span class="text-gray-700">Transparent Settlement</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HowItWorks',
  data() {
    return {
      steps: [
        {
          id: 1,
          title: "Define an Event",
          description: "Create or select a binary event with clear resolution criteria",
          icon: "event"
        },
        {
          id: 2,
          title: "Buy or Sell Shares",
          description: "Trade Yes/No shares based on your prediction",
          icon: "trade"
        },
        {
          id: 3,
          title: "Market Sets Price = Probability",
          description: "Prices reflect collective market sentiment as probabilities",
          icon: "price"
        },
        {
          id: 4,
          title: "Settlement After Event",
          description: "Winning shares pay $1, losing shares pay $0",
          icon: "settlement"
        }
      ]
    }
  },
  methods: {
    getStepIconBg(icon) {
      const bgClasses = {
        'event': 'bg-teal-100 group-hover:bg-teal-200',
        'trade': 'bg-emerald-100 group-hover:bg-emerald-200',
        'price': 'bg-teal-100 group-hover:bg-teal-200',
        'settlement': 'bg-emerald-100 group-hover:bg-emerald-200'
      }
      return bgClasses[icon] || 'bg-gray-100 group-hover:bg-gray-200'
    },
    getStepIconColor(icon) {
      const colorClasses = {
        'event': 'text-teal-600',
        'trade': 'text-emerald-600',
        'price': 'text-teal-600',
        'settlement': 'text-emerald-600'
      }
      return colorClasses[icon] || 'text-gray-600'
    }
  }
}
</script>
