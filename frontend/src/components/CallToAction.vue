<template>
  <section id="contact" class="section-padding bg-gradient-to-br from-navy-900 via-navy-800 to-navy-900">
    <div class="container-custom">
      <div class="text-center max-w-4xl mx-auto">
        <!-- Main CTA -->
        <div class="mb-16">
          <h2 class="text-4xl sm:text-5xl lg:text-6xl font-heading font-bold text-white mb-8 leading-tight">
            Join PredictionMart Today
          </h2>
          <p class="text-xl sm:text-2xl text-gray-300 mb-12 leading-relaxed">
            Start Trading on Tomorrow
          </p>
          
          <div class="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
            <button class="btn-primary text-lg px-12 py-4 w-full sm:w-auto transform hover:scale-105">
              Start Trading Now
            </button>
            <button class="bg-white/10 hover:bg-white/20 text-white font-semibold py-4 px-8 rounded-lg transition-all duration-300 w-full sm:w-auto">
              Learn More
            </button>
          </div>
        </div>

        <!-- Features Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
          <div class="text-center">
            <div class="w-16 h-16 bg-teal-500/20 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-white mb-2">Instant Trading</h3>
            <p class="text-gray-300">Start trading immediately with our intuitive platform</p>
          </div>
          
          <div class="text-center">
            <div class="w-16 h-16 bg-emerald-500/20 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-white mb-2">Secure & Safe</h3>
            <p class="text-gray-300">Bank-level security protects your investments</p>
          </div>
          
          <div class="text-center">
            <div class="w-16 h-16 bg-teal-500/20 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-white mb-2">Global Community</h3>
            <p class="text-gray-300">Trade alongside thousands of smart investors</p>
          </div>
        </div>

        <!-- Contact Form -->
        <div class="bg-white/10 backdrop-blur-md rounded-2xl p-8 max-w-2xl mx-auto">
          <h3 class="text-2xl font-heading font-bold text-white mb-6">
            Get Early Access
          </h3>
          <p class="text-gray-300 mb-8">
            Be the first to know when PredictionMart launches. Join our waitlist for exclusive early access.
          </p>
          
          <form @submit.prevent="submitContactForm" class="space-y-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <input
                v-model="contactForm.firstName"
                type="text"
                placeholder="First Name"
                required
                class="w-full px-4 py-3 rounded-lg bg-white/10 border border-white/20 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent"
              />
              <input
                v-model="contactForm.lastName"
                type="text"
                placeholder="Last Name"
                required
                class="w-full px-4 py-3 rounded-lg bg-white/10 border border-white/20 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent"
              />
            </div>
            
            <input
              v-model="contactForm.email"
              type="email"
              placeholder="Email Address"
              required
              class="w-full px-4 py-3 rounded-lg bg-white/10 border border-white/20 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent"
            />
            
            <select
              v-model="contactForm.interest"
              class="w-full px-4 py-3 rounded-lg bg-white/10 border border-white/20 text-white focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent"
            >
              <option value="" class="text-gray-900">Select your interest</option>
              <option value="trader" class="text-gray-900">Individual Trading</option>
              <option value="researcher" class="text-gray-900">Research & Analysis</option>
              <option value="institution" class="text-gray-900">Institutional Use</option>
              <option value="general" class="text-gray-900">General Interest</option>
            </select>
            
            <button
              type="submit"
              :disabled="submitting"
              class="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="submitting" class="flex items-center justify-center">
                <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Joining...
              </span>
              <span v-else>Join Waitlist</span>
            </button>
          </form>

          <!-- Success Message -->
          <div v-if="submissionSuccess" class="mt-6 p-4 bg-green-500/20 border border-green-500/30 rounded-lg">
            <div class="flex items-center">
              <svg class="w-5 h-5 text-green-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <span class="text-green-300">Thank you! We'll be in touch soon with early access details.</span>
            </div>
          </div>

          <!-- Error Message -->
          <div v-if="submissionError" class="mt-6 p-4 bg-red-500/20 border border-red-500/30 rounded-lg">
            <div class="flex items-center">
              <svg class="w-5 h-5 text-red-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <span class="text-red-300">{{ submissionError }}</span>
            </div>
          </div>
        </div>

        <!-- Trust Indicators -->
        <div class="mt-16 text-center">
          <p class="text-gray-400 mb-6">Trusted by thousands of traders worldwide</p>
          <div class="flex flex-wrap justify-center items-center space-x-8 opacity-60">
            <!-- Placeholder for trust badges/logos -->
            <div class="text-gray-400 font-semibold">SEC Compliant</div>
            <div class="text-gray-400 font-semibold">Bank-Grade Security</div>
            <div class="text-gray-400 font-semibold">24/7 Support</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'CallToAction',
  data() {
    return {
      contactForm: {
        firstName: '',
        lastName: '',
        email: '',
        interest: ''
      },
      submitting: false,
      submissionSuccess: false,
      submissionError: ''
    }
  },
  methods: {
    submitContactForm() {
      this.submitting = true
      this.submissionSuccess = false
      this.submissionError = ''

      // Simulate form submission
      setTimeout(() => {
        this.submissionSuccess = true
        this.contactForm = {
          firstName: '',
          lastName: '',
          email: '',
          interest: ''
        }
        this.submitting = false
      }, 1000)
    }
  }
}
</script>
