<template>
  <section class="section-padding bg-white">
    <div class="container-custom">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-heading font-bold text-gray-900 mb-6">
          Understanding Prediction Markets
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Learn the core concepts that make prediction markets powerful tools for 
          forecasting and decision-making.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <!-- Event Definition -->
        <div class="card p-8">
          <div class="flex items-center mb-6">
            <div class="w-12 h-12 bg-teal-100 rounded-full flex items-center justify-center mr-4">
              <svg class="w-6 h-6 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
              </svg>
            </div>
            <h3 class="text-2xl font-heading font-bold text-gray-900">Event Definition</h3>
          </div>
          
          <p class="text-gray-600 mb-6 leading-relaxed">
            Events are binary outcomes with clear, objective resolution criteria. 
            They must be verifiable and have a specific deadline for settlement.
          </p>
          
          <div class="bg-gray-50 rounded-lg p-6 mb-6">
            <h4 class="font-semibold text-gray-900 mb-3">Example:</h4>
            <div class="bg-white rounded-lg p-4 border-l-4 border-teal-500">
              <p class="text-gray-800 font-medium">
                "Will Kamala Harris win the 2024 U.S. Presidential Election?"
              </p>
              <div class="mt-3 text-sm text-gray-600">
                <div class="flex items-center space-x-4">
                  <span>✅ Binary outcome</span>
                  <span>✅ Clear criteria</span>
                  <span>✅ Specific deadline</span>
                </div>
              </div>
            </div>
          </div>

          <div class="text-sm text-gray-500">
            <strong>Key Requirements:</strong> Unambiguous wording, verifiable outcome, 
            specific resolution date, and neutral language.
          </div>
        </div>

        <!-- Trading Contracts -->
        <div class="card p-8">
          <div class="flex items-center mb-6">
            <div class="w-12 h-12 bg-emerald-100 rounded-full flex items-center justify-center mr-4">
              <svg class="w-6 h-6 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
              </svg>
            </div>
            <h3 class="text-2xl font-heading font-bold text-gray-900">Trading Contracts</h3>
          </div>
          
          <p class="text-gray-600 mb-6 leading-relaxed">
            Each event has two types of shares: "Yes" and "No". You can buy or sell 
            either type, with each share paying out $1 if your prediction is correct.
          </p>
          
          <div class="grid grid-cols-2 gap-4 mb-6">
            <div class="bg-green-50 rounded-lg p-4 text-center">
              <div class="text-2xl font-bold text-green-600 mb-2">YES</div>
              <div class="text-sm text-gray-600">Shares that pay $1 if the event occurs</div>
            </div>
            <div class="bg-red-50 rounded-lg p-4 text-center">
              <div class="text-2xl font-bold text-red-600 mb-2">NO</div>
              <div class="text-sm text-gray-600">Shares that pay $1 if the event doesn't occur</div>
            </div>
          </div>

          <div class="text-sm text-gray-500">
            <strong>Payout Structure:</strong> Winning shares = $1.00, Losing shares = $0.00
          </div>
        </div>

        <!-- Price = Probability -->
        <div class="card p-8">
          <div class="flex items-center mb-6">
            <div class="w-12 h-12 bg-teal-100 rounded-full flex items-center justify-center mr-4">
              <svg class="w-6 h-6 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
              </svg>
            </div>
            <h3 class="text-2xl font-heading font-bold text-gray-900">Price = Probability</h3>
          </div>
          
          <p class="text-gray-600 mb-6 leading-relaxed">
            Market prices directly represent the collective probability assessment. 
            A $0.85 price means the market believes there's an 85% chance the event will occur.
          </p>
          
          <div class="bg-gray-50 rounded-lg p-6 mb-6">
            <h4 class="font-semibold text-gray-900 mb-4">Probability Examples:</h4>
            <div class="space-y-3">
              <div class="flex items-center justify-between bg-white rounded-lg p-3">
                <span class="text-gray-700">$0.85 price</span>
                <span class="font-semibold text-teal-600">85% probability</span>
              </div>
              <div class="flex items-center justify-between bg-white rounded-lg p-3">
                <span class="text-gray-700">$0.30 price</span>
                <span class="font-semibold text-orange-600">30% probability</span>
              </div>
              <div class="flex items-center justify-between bg-white rounded-lg p-3">
                <span class="text-gray-700">$0.50 price</span>
                <span class="font-semibold text-gray-600">50% probability (coin flip)</span>
              </div>
            </div>
          </div>

          <div class="text-sm text-gray-500">
            <strong>Market Efficiency:</strong> Prices incorporate all available information 
            and update in real-time as new information emerges.
          </div>
        </div>

        <!-- Settlement -->
        <div class="card p-8">
          <div class="flex items-center mb-6">
            <div class="w-12 h-12 bg-emerald-100 rounded-full flex items-center justify-center mr-4">
              <svg class="w-6 h-6 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <h3 class="text-2xl font-heading font-bold text-gray-900">Settlement</h3>
          </div>
          
          <p class="text-gray-600 mb-6 leading-relaxed">
            After the event deadline passes, the outcome is determined and shares are 
            automatically settled. Winning shares pay $1, losing shares pay $0.
          </p>
          
          <div class="bg-gray-50 rounded-lg p-6 mb-6">
            <h4 class="font-semibold text-gray-900 mb-4">Payoff Calculation:</h4>
            <div class="bg-white rounded-lg p-4 space-y-3">
              <div class="text-sm">
                <span class="font-medium text-gray-700">If you bought 20 "Yes" shares at $0.30 each:</span>
              </div>
              <div class="text-sm text-gray-600">
                <div>Investment: 20 × $0.30 = $6.00</div>
                <div>If "Yes" wins: 20 × $1.00 = $20.00</div>
                <div class="font-semibold text-green-600">Profit: $20.00 - $6.00 = $14.00</div>
              </div>
            </div>
          </div>

          <div class="text-sm text-gray-500">
            <strong>Automatic Settlement:</strong> No manual intervention required. 
            Payouts are processed immediately upon event resolution.
          </div>
        </div>
      </div>

      <!-- Key Benefits -->
      <div class="mt-16 bg-gradient-to-r from-teal-50 to-emerald-50 rounded-2xl p-8">
        <h3 class="text-2xl font-heading font-bold text-gray-900 text-center mb-8">
          Why Prediction Markets Are Powerful
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="text-center">
            <div class="w-16 h-16 bg-teal-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <h4 class="text-lg font-semibold text-gray-900 mb-2">Real-time Updates</h4>
            <p class="text-gray-600">Prices update instantly as new information becomes available</p>
          </div>
          <div class="text-center">
            <div class="w-16 h-16 bg-emerald-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
              </svg>
            </div>
            <h4 class="text-lg font-semibold text-gray-900 mb-2">Collective Intelligence</h4>
            <p class="text-gray-600">Aggregates insights from diverse participants worldwide</p>
          </div>
          <div class="text-center">
            <div class="w-16 h-16 bg-teal-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
              </svg>
            </div>
            <h4 class="text-lg font-semibold text-gray-900 mb-2">Incentivized Accuracy</h4>
            <p class="text-gray-600">Financial rewards encourage truthful information sharing</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ConceptExplainers'
}
</script>
