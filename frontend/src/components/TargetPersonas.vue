<template>
  <section class="section-padding bg-white">
    <div class="container-custom">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-heading font-bold text-gray-900 mb-6">
          Who Uses PredictionMart?
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          From individual traders to large institutions, our platform serves diverse users 
          seeking to leverage collective intelligence for better decision-making.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Individual Traders -->
        <div 
          v-for="persona in personas" 
          :key="persona.id"
          class="card p-8 text-center group hover:scale-105 transition-all duration-300"
        >
          <div class="mb-6">
            <div class="w-20 h-20 mx-auto mb-4 rounded-full flex items-center justify-center transition-colors duration-300"
                 :class="getPersonaIconBg(persona.icon)">
              <svg class="w-10 h-10" :class="getPersonaIconColor(persona.icon)" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path v-if="persona.icon === 'trader'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
                <path v-else-if="persona.icon === 'researcher'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
                <path v-else-if="persona.icon === 'institution'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
              </svg>
            </div>
          </div>
          
          <h3 class="text-2xl font-heading font-bold text-gray-900 mb-4">
            {{ persona.title }}
          </h3>
          
          <p class="text-gray-600 text-lg leading-relaxed">
            {{ persona.description }}
          </p>

          <!-- Additional details for each persona -->
          <div class="mt-6 pt-6 border-t border-gray-100">
            <div v-if="persona.icon === 'trader'" class="text-sm text-gray-500">
              <div class="flex items-center justify-center space-x-4">
                <span>📈 Speculation</span>
                <span>💡 Insights</span>
                <span>💰 Profits</span>
              </div>
            </div>
            <div v-else-if="persona.icon === 'researcher'" class="text-sm text-gray-500">
              <div class="flex items-center justify-center space-x-4">
                <span>📊 Analytics</span>
                <span>🔍 Research</span>
                <span>📈 Forecasting</span>
              </div>
            </div>
            <div v-else-if="persona.icon === 'institution'" class="text-sm text-gray-500">
              <div class="flex items-center justify-center space-x-4">
                <span>🏢 Enterprise</span>
                <span>⚖️ Risk Management</span>
                <span>📊 Sentiment</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Call to action for personas -->
      <div class="text-center mt-16">
        <div class="bg-gray-50 rounded-2xl p-8 max-w-4xl mx-auto">
          <h3 class="text-2xl font-heading font-bold text-gray-900 mb-4">
            Ready to Join Our Community?
          </h3>
          <p class="text-gray-600 mb-6">
            Whether you're a seasoned trader, curious researcher, or institutional decision-maker, 
            PredictionMart offers the tools and insights you need.
          </p>
          <button class="btn-primary">
            Start Trading Today
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'TargetPersonas',
  data() {
    return {
      personas: [
        {
          id: 1,
          title: "Individual Traders",
          description: "Speculate and profit from your insights",
          icon: "trader"
        },
        {
          id: 2,
          title: "Researchers & Analysts",
          description: "Leverage collective probabilities for forecasting",
          icon: "researcher"
        },
        {
          id: 3,
          title: "Institutions",
          description: "Understand crowd sentiment on global risks",
          icon: "institution"
        }
      ]
    }
  },
  methods: {
    getPersonaIconBg(icon) {
      const bgClasses = {
        'trader': 'bg-teal-100 group-hover:bg-teal-200',
        'researcher': 'bg-emerald-100 group-hover:bg-emerald-200',
        'institution': 'bg-gray-100 group-hover:bg-gray-200'
      }
      return bgClasses[icon] || 'bg-gray-100 group-hover:bg-gray-200'
    },
    getPersonaIconColor(icon) {
      const colorClasses = {
        'trader': 'text-teal-600',
        'researcher': 'text-emerald-600',
        'institution': 'text-gray-600'
      }
      return colorClasses[icon] || 'text-gray-600'
    }
  }
}
</script>
