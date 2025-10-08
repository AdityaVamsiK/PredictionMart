<template>
  <section class="section-padding bg-white">
    <div class="container-custom">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-heading font-bold text-gray-900 mb-6">
          Payoff Calculator
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Calculate your potential profits before making any trades. Enter the price per share 
          and your investment amount to see your potential payoff.
        </p>
      </div>

      <div class="max-w-2xl mx-auto">
        <div class="card p-8">
          <form @submit.prevent="calculatePayoff" class="space-y-6">
            <!-- Price Input -->
            <div>
              <label for="price" class="block text-sm font-medium text-gray-700 mb-2">
                Price per Share ($)
              </label>
              <div class="relative">
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <span class="text-gray-500 text-sm">$</span>
                </div>
                <input
                  id="price"
                  v-model="formData.price"
                  type="number"
                  step="0.01"
                  min="0.01"
                  max="0.99"
                  class="block w-full pl-8 pr-3 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 text-lg"
                  placeholder="0.65"
                  @input="recalculateOnInput"
                />
              </div>
              <p class="mt-1 text-sm text-gray-500">
                Enter the current market price (e.g., $0.65 = 65% probability)
              </p>
            </div>

            <!-- Investment Input -->
            <div>
              <label for="investment" class="block text-sm font-medium text-gray-700 mb-2">
                Investment Amount ($)
              </label>
              <div class="relative">
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <span class="text-gray-500 text-sm">$</span>
                </div>
                <input
                  id="investment"
                  v-model="formData.investment"
                  type="number"
                  step="0.01"
                  min="0.01"
                  class="block w-full pl-8 pr-3 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 text-lg"
                  placeholder="100.00"
                  @input="recalculateOnInput"
                />
              </div>
              <p class="mt-1 text-sm text-gray-500">
                Amount you want to invest in this prediction
              </p>
            </div>

            <!-- Calculate Button -->
            <button
              type="submit"
              :disabled="!isFormValid || calculating"
              class="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="calculating" class="flex items-center justify-center">
                <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Calculating...
              </span>
              <span v-else>Calculate Payoff</span>
            </button>
          </form>

          <!-- Results -->
          <div v-if="calculationResult" class="mt-8 p-6 bg-gray-50 rounded-lg">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Calculation Results</h3>
            
            <div class="space-y-3">
              <div class="flex items-center justify-between py-2 border-b border-gray-200">
                <span class="text-gray-600">Shares You Can Buy:</span>
                <span class="font-semibold text-gray-900">{{ calculationResult.shares_bought }} shares</span>
              </div>
              
              <div class="flex items-center justify-between py-2 border-b border-gray-200">
                <span class="text-gray-600">Your Investment:</span>
                <span class="font-semibold text-gray-900">${{ formData.investment }}</span>
              </div>
              
              <div class="flex items-center justify-between py-2 border-b border-gray-200">
                <span class="text-gray-600">Price per Share:</span>
                <span class="font-semibold text-gray-900">${{ formData.price }}</span>
              </div>
              
              <div class="flex items-center justify-between py-3 bg-green-50 rounded-lg px-4">
                <span class="font-semibold text-gray-900">Potential Payout:</span>
                <span class="text-xl font-bold text-green-600">${{ calculationResult.potential_payoff }}</span>
              </div>
              
              <div class="flex items-center justify-between py-3 bg-blue-50 rounded-lg px-4">
                <span class="font-semibold text-gray-900">Potential Profit:</span>
                <span 
                  class="text-xl font-bold"
                  :class="calculationResult.potential_profit >= 0 ? 'text-green-600' : 'text-red-600'"
                >
                  {{ calculationResult.potential_profit >= 0 ? '+' : '' }}${{ calculationResult.potential_profit }}
                </span>
              </div>
              
              <div class="flex items-center justify-between py-3 bg-purple-50 rounded-lg px-4">
                <span class="font-semibold text-gray-900">ROI:</span>
                <span 
                  class="text-xl font-bold"
                  :class="calculationResult.roi_percentage >= 0 ? 'text-green-600' : 'text-red-600'"
                >
                  {{ calculationResult.roi_percentage >= 0 ? '+' : '' }}{{ calculationResult.roi_percentage }}%
                </span>
              </div>
            </div>

            <!-- Formula Display -->
            <div class="mt-6 p-4 bg-white rounded-lg border">
              <h4 class="font-semibold text-gray-900 mb-2">Calculation Formula:</h4>
              <div class="text-sm text-gray-600 space-y-1">
                <div>Shares Bought = Investment ÷ Price per Share</div>
                <div>Shares Bought = ${{ formData.investment }} ÷ ${{ formData.price }} = {{ calculationResult.shares_bought }} shares</div>
                <div class="mt-2">If Correct: Payout = {{ calculationResult.shares_bought }} × $1.00 = ${{ calculationResult.potential_payoff }}</div>
                <div>Profit = ${{ calculationResult.potential_payoff }} - ${{ formData.investment }} = ${{ calculationResult.potential_profit }}</div>
              </div>
            </div>

            <!-- Warning -->
            <div class="mt-4 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
              <div class="flex items-start">
                <svg class="w-5 h-5 text-yellow-600 mr-2 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.732-.833-2.5 0L4.314 16.5c-.77.833.192 2.5 1.732 2.5z"/>
                </svg>
                <div class="text-sm text-yellow-800">
                  <strong>Risk Warning:</strong> This is only your potential payout if your prediction is correct. 
                  If you're wrong, you'll lose your entire investment. Only trade with money you can afford to lose.
                </div>
              </div>
            </div>
          </div>

          <!-- Error Message -->
          <div v-if="errorMessage" class="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg">
            <div class="flex items-start">
              <svg class="w-5 h-5 text-red-600 mr-2 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <div class="text-sm text-red-800">
                {{ errorMessage }}
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Examples -->
        <div class="mt-8">
          <h3 class="text-lg font-semibold text-gray-900 mb-4 text-center">Quick Examples</h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <button 
              v-for="example in quickExamples" 
              :key="example.name"
              @click="loadExample(example)"
              class="p-4 border border-gray-200 rounded-lg hover:border-teal-500 hover:bg-teal-50 transition-colors duration-200 text-left"
            >
              <div class="font-semibold text-gray-900">{{ example.name }}</div>
              <div class="text-sm text-gray-600">{{ example.description }}</div>
              <div class="text-sm text-teal-600 mt-1">Click to try</div>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'PayoffCalculator',
  data() {
    return {
      formData: {
        price: '',
        investment: ''
      },
      calculationResult: null,
      errorMessage: '',
      calculating: false,
      quickExamples: [
        {
          name: 'Conservative Trade',
          description: '$0.80 per share, $50 investment',
          price: 0.80,
          investment: 50
        },
        {
          name: 'Moderate Trade',
          description: '$0.60 per share, $100 investment',
          price: 0.60,
          investment: 100
        },
        {
          name: 'High Risk Trade',
          description: '$0.30 per share, $200 investment',
          price: 0.30,
          investment: 200
        },
        {
          name: 'Low Confidence',
          description: '$0.90 per share, $25 investment',
          price: 0.90,
          investment: 25
        }
      ]
    }
  },
  computed: {
    isFormValid() {
      return this.formData.price && 
             this.formData.investment && 
             parseFloat(this.formData.price) > 0 && 
             parseFloat(this.formData.price) < 1 && 
             parseFloat(this.formData.investment) > 0
    }
  },
  methods: {
    calculatePayoff() {
      if (!this.isFormValid) return

      this.calculating = true
      this.errorMessage = ''
      this.calculationResult = null

      try {
        const pricePerShare = parseFloat(this.formData.price)
        const investmentAmount = parseFloat(this.formData.investment)
        
        if (pricePerShare <= 0 || investmentAmount <= 0) {
          this.errorMessage = 'Price and investment must be positive numbers'
          return
        }
            
        const sharesBought = investmentAmount / pricePerShare
        const potentialPayoff = sharesBought * 1.00  // $1 per winning share
        
        this.calculationResult = {
          shares_bought: Math.round(sharesBought * 100) / 100,
          potential_payoff: Math.round(potentialPayoff * 100) / 100,
          potential_profit: Math.round((potentialPayoff - investmentAmount) * 100) / 100,
          roi_percentage: Math.round(((potentialPayoff - investmentAmount) / investmentAmount) * 100 * 10) / 10
        }
      } catch (error) {
        this.errorMessage = 'Invalid input data'
      } finally {
        this.calculating = false
      }
    },
    recalculateOnInput() {
      // Auto-calculate as user types
      if (this.isFormValid) {
        clearTimeout(this.calculationTimeout)
        this.calculationTimeout = setTimeout(() => {
          this.calculatePayoff()
        }, 500)
      }
    },
    loadExample(example) {
      this.formData.price = example.price.toString()
      this.formData.investment = example.investment.toString()
      this.calculatePayoff()
    }
  },
  beforeUnmount() {
    if (this.calculationTimeout) {
      clearTimeout(this.calculationTimeout)
    }
  }
}
</script>
