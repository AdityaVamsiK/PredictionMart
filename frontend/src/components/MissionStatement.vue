<template>
  <section id="about" class="section-padding bg-gray-50">
    <div class="container-custom">
      <div class="max-w-4xl mx-auto text-center">
        <div class="animate-fade-in">
          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-heading font-bold text-gray-900 mb-8">
            Our Mission
          </h2>
          
          <div class="bg-white rounded-2xl shadow-xl p-8 sm:p-12 lg:p-16">
            <div class="text-6xl mb-6">🎯</div>
            <p class="text-xl sm:text-2xl text-gray-700 leading-relaxed mb-8">
              PredictionMart's mission is to democratize access to global event forecasting 
              by creating a transparent, fair, and liquid prediction market.
            </p>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-12">
              <div class="text-center">
                <div class="w-16 h-16 bg-teal-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <svg class="w-8 h-8 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </div>
                <h3 class="text-lg font-semibold text-gray-900 mb-2">Transparent</h3>
                <p class="text-gray-600">Open-source algorithms and clear pricing mechanisms</p>
              </div>
              
              <div class="text-center">
                <div class="w-16 h-16 bg-emerald-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <svg class="w-8 h-8 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
                  </svg>
                </div>
                <h3 class="text-lg font-semibold text-gray-900 mb-2">Fair</h3>
                <p class="text-gray-600">Equal access and unbiased market mechanisms</p>
              </div>
              
              <div class="text-center">
                <div class="w-16 h-16 bg-teal-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <svg class="w-8 h-8 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                  </svg>
                </div>
                <h3 class="text-lg font-semibold text-gray-900 mb-2">Liquid</h3>
                <p class="text-gray-600">Deep markets with tight spreads and instant execution</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'MissionStatement'
}
</script>
