<template>
  <nav 
    :class="[
      'fixed top-0 left-0 right-0 z-50 transition-all duration-300',
      isScrolled ? 'bg-navy-900/95 backdrop-blur-md shadow-lg' : 'bg-transparent'
    ]"
  >
    <div class="container-custom">
      <div class="flex items-center justify-between h-16 px-4 sm:px-6 lg:px-8">
        <!-- Logo -->
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <h1 class="text-2xl font-heading font-bold gradient-text">
              PredictionMart
            </h1>
          </div>
        </div>

        <!-- Desktop Navigation -->
        <div class="hidden md:block">
          <div class="ml-10 flex items-baseline space-x-8">
            <a 
              v-for="item in navItems" 
              :key="item.name"
              :href="item.href"
              class="text-gray-300 hover:text-teal-400 px-3 py-2 text-sm font-medium transition-colors duration-200"
            >
              {{ item.name }}
            </a>
          </div>
        </div>

        <!-- CTA Button -->
        <div class="hidden md:block">
          <button class="btn-primary">
            Get Started
          </button>
        </div>

        <!-- Mobile menu button -->
        <div class="md:hidden">
          <button
            @click="toggleMobileMenu"
            class="text-gray-300 hover:text-white focus:outline-none focus:text-white"
          >
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Navigation -->
      <div v-show="mobileMenuOpen" class="md:hidden">
        <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-navy-900/95 backdrop-blur-md">
          <a 
            v-for="item in navItems" 
            :key="item.name"
            :href="item.href"
            @click="closeMobileMenu"
            class="text-gray-300 hover:text-teal-400 block px-3 py-2 text-base font-medium transition-colors duration-200"
          >
            {{ item.name }}
          </a>
          <button class="btn-primary w-full mt-4">
            Get Started
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  data() {
    return {
      isScrolled: false,
      mobileMenuOpen: false,
      navItems: [
        { name: 'Home', href: '#home' },
        { name: 'About', href: '#about' },
        { name: 'How It Works', href: '#how-it-works' },
        { name: 'Examples', href: '#examples' },
        { name: 'Contact', href: '#contact' }
      ]
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
    handleScroll() {
      this.isScrolled = window.scrollY > 50
    },
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen
    },
    closeMobileMenu() {
      this.mobileMenuOpen = false
    }
  }
}
</script>
