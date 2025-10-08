<template>
  <section id="examples" class="section-padding bg-gray-50">
    <div class="container-custom">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-heading font-bold text-gray-900 mb-6">
          Real Example Transactions
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          See how prediction market trading works with these real-world examples. 
          Each transaction shows the complete calculation from investment to payoff.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div 
          v-for="example in examples" 
          :key="example.id"
          class="card p-8"
          :class="example.result === 'winning' ? 'border-l-4 border-green-500' : 'border-l-4 border-red-500'"
        >
          <!-- Transaction Header -->
          <div class="flex items-center justify-between mb-6">
            <div class="flex items-center">
              <div 
                class="w-12 h-12 rounded-full flex items-center justify-center mr-4"
                :class="example.result === 'winning' ? 'bg-green-100' : 'bg-red-100'"
              >
                <svg 
                  class="w-6 h-6" 
                  :class="example.result === 'winning' ? 'text-green-600' : 'text-red-600'" 
                  fill="none" 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path v-if="example.result === 'winning'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-heading font-bold text-gray-900">
                  {{ example.result === 'winning' ? 'Winning Trade' : 'Losing Trade' }}
                </h3>
                <div class="text-sm text-gray-500">
                  {{ example.outcome }} Outcome
                </div>
              </div>
            </div>
            <div 
              class="text-2xl font-bold"
              :class="example.result === 'winning' ? 'text-green-600' : 'text-red-600'"
            >
              {{ example.result === 'winning' ? '+' : '' }}${{ example.profit.toFixed(2) }}
            </div>
          </div>

          <!-- Event Description -->
          <div class="bg-gray-50 rounded-lg p-4 mb-6">
            <h4 class="font-semibold text-gray-900 mb-2">Event:</h4>
            <p class="text-gray-700 text-sm leading-relaxed">
              {{ example.event }}
            </p>
          </div>

          <!-- Transaction Details -->
          <div class="space-y-4">
            <div class="flex items-center justify-between py-2 border-b border-gray-100">
              <span class="text-gray-600">Shares Bought:</span>
              <span class="font-semibold text-gray-900">{{ example.shares }} "{{ example.outcome }}" shares</span>
            </div>
            
            <div class="flex items-center justify-between py-2 border-b border-gray-100">
              <span class="text-gray-600">Price per Share:</span>
              <span class="font-semibold text-gray-900">${{ example.price.toFixed(2) }}</span>
            </div>
            
            <div class="flex items-center justify-between py-2 border-b border-gray-100">
              <span class="text-gray-600">Total Investment:</span>
              <span class="font-semibold text-gray-900">${{ example.investment.toFixed(2) }}</span>
            </div>
            
            <div class="flex items-center justify-between py-2 border-b border-gray-100">
              <span class="text-gray-600">Payout:</span>
              <span class="font-semibold text-gray-900">${{ example.payout.toFixed(2) }}</span>
            </div>
            
            <div class="flex items-center justify-between py-3 bg-gray-50 rounded-lg px-4">
              <span class="font-semibold text-gray-900">Net Profit/Loss:</span>
              <span 
                class="text-xl font-bold"
                :class="example.result === 'winning' ? 'text-green-600' : 'text-red-600'"
              >
                {{ example.result === 'winning' ? '+' : '' }}${{ example.profit.toFixed(2) }}
              </span>
            </div>
          </div>

          <!-- ROI Calculation -->
          <div class="mt-6 p-4 bg-gray-50 rounded-lg">
            <h5 class="font-semibold text-gray-900 mb-2">ROI Calculation:</h5>
            <div class="text-sm text-gray-600 space-y-1">
              <div>ROI = (Payout - Investment) ÷ Investment × 100%</div>
              <div>ROI = (${{ example.payout.toFixed(2) }} - ${{ example.investment.toFixed(2) }}) ÷ ${{ example.investment.toFixed(2) }} × 100%</div>
              <div class="font-semibold">
                ROI = {{ ((example.payout - example.investment) / example.investment * 100).toFixed(1) }}%
              </div>
            </div>
          </div>

          <!-- Key Insights -->
          <div class="mt-6">
            <h5 class="font-semibold text-gray-900 mb-2">Key Insights:</h5>
            <div class="text-sm text-gray-600 space-y-1">
              <div v-if="example.result === 'winning'" class="flex items-center">
                <svg class="w-4 h-4 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <span>Correct prediction led to significant profit</span>
              </div>
              <div v-else class="flex items-center">
                <svg class="w-4 h-4 text-red-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                </svg>
                <span>Incorrect prediction resulted in total loss</span>
              </div>
              <div class="flex items-center">
                <svg class="w-4 h-4 text-blue-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <span>Risk management is crucial in prediction markets</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Trading Tips -->
      <div class="mt-16 bg-white rounded-2xl shadow-lg p-8">
        <h3 class="text-2xl font-heading font-bold text-gray-900 text-center mb-8">
          Trading Tips for Success
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="text-center">
            <div class="w-16 h-16 bg-teal-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
              </svg>
            </div>
            <h4 class="text-lg font-semibold text-gray-900 mb-2">Research Events</h4>
            <p class="text-gray-600 text-sm">Understand the event criteria and resolution timeline</p>
          </div>
          <div class="text-center">
            <div class="w-16 h-16 bg-emerald-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
              </svg>
            </div>
            <h4 class="text-lg font-semibold text-gray-900 mb-2">Manage Risk</h4>
            <p class="text-gray-600 text-sm">Only trade with money you can afford to lose</p>
          </div>
          <div class="text-center">
            <div class="w-16 h-16 bg-teal-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <h4 class="text-lg font-semibold text-gray-900 mb-2">Diversify</h4>
            <p class="text-gray-600 text-sm">Spread investments across multiple events</p>
          </div>
          <div class="text-center">
            <div class="w-16 h-16 bg-emerald-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-5 5v-5zM4 19h6v-2H4v2zM4 15h6v-2H4v2zM4 11h6V9H4v2zM4 7h6V5H4v2z"/>
              </svg>
            </div>
            <h4 class="text-lg font-semibold text-gray-900 mb-2">Track Performance</h4>
            <p class="text-gray-600 text-sm">Monitor your trades and learn from outcomes</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ExampleTransactions',
  data() {
    return {
      examples: [
        {
          id: 1,
          event: "Will Kamala Harris win the 2024 U.S. Presidential Election?",
          price: 0.30,
          shares: 20,
          investment: 6.00,
          outcome: "Yes",
          payout: 20.00,
          profit: 14.00,
          result: "winning"
        },
        {
          id: 2,
          event: "Will Bitcoin reach $100,000 by end of 2024?",
          price: 0.75,
          shares: 10,
          investment: 7.50,
          outcome: "No",
          payout: 0.00,
          profit: -7.50,
          result: "losing"
        }
      ]
    }
  }
}
</script>
