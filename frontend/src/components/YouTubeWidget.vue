<template>
  <section class="section-padding bg-gray-50">
    <div class="container-custom">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-heading font-bold text-gray-900 mb-6">
          Learn More About Prediction Markets
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Watch this comprehensive explanation of prediction markets to better understand 
          how they work and why they're so powerful for forecasting.
        </p>
      </div>

      <div class="max-w-4xl mx-auto">
        <!-- YouTube Video Container -->
        <div class="relative bg-gray-900 rounded-2xl shadow-2xl overflow-hidden">
          <!-- Video Placeholder/Embed -->
          <div class="relative w-full" style="padding-bottom: 56.25%;">
            <iframe
              class="absolute top-0 left-0 w-full h-full"
              :src="videoEmbedUrl"
              title="Prediction Markets Explained"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen
            ></iframe>
          </div>
          
          <!-- Video Overlay Info -->
          <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/70 to-transparent p-6">
            <h3 class="text-xl font-semibold text-white mb-2">
              {{ videoTitle }}
            </h3>
            <p class="text-gray-300 text-sm">
              {{ videoDescription }}
            </p>
          </div>
        </div>

        <!-- Video Details -->
        <div class="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="card p-6 text-center">
            <div class="w-12 h-12 bg-teal-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-6 h-6 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <h4 class="font-semibold text-gray-900 mb-2">Duration</h4>
            <p class="text-gray-600">{{ videoDuration }}</p>
          </div>
          
          <div class="card p-6 text-center">
            <div class="w-12 h-12 bg-emerald-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-6 h-6 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4V2a1 1 0 011-1h8a1 1 0 011 1v2m0 0V1a1 1 0 011-1h2a1 1 0 011 1v18a1 1 0 01-1 1H4a1 1 0 01-1-1V1a1 1 0 011-1h2a1 1 0 011 1v3m8-4H8m8 0v18H8V4z"/>
              </svg>
            </div>
            <h4 class="font-semibold text-gray-900 mb-2">Language</h4>
            <p class="text-gray-600">English</p>
          </div>
          
          <div class="card p-6 text-center">
            <div class="w-12 h-12 bg-teal-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-6 h-6 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <h4 class="font-semibold text-gray-900 mb-2">Level</h4>
            <p class="text-gray-600">Beginner Friendly</p>
          </div>
        </div>

        <!-- Additional Resources -->
        <div class="mt-12 bg-white rounded-2xl shadow-lg p-8">
          <h3 class="text-2xl font-heading font-bold text-gray-900 text-center mb-8">
            More Learning Resources
          </h3>
          
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <a 
              v-for="resource in additionalResources" 
              :key="resource.title"
              :href="resource.url"
              target="_blank"
              rel="noopener noreferrer"
              class="group block p-6 border border-gray-200 rounded-lg hover:border-teal-500 hover:shadow-lg transition-all duration-300"
            >
              <div class="text-center">
                <div 
                  class="w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform duration-300"
                  :class="resource.iconBg"
                >
                  <svg class="w-6 h-6" :class="resource.iconColor" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="resource.iconPath"/>
                  </svg>
                </div>
                <h4 class="font-semibold text-gray-900 mb-2 group-hover:text-teal-600 transition-colors duration-300">
                  {{ resource.title }}
                </h4>
                <p class="text-gray-600 text-sm">{{ resource.description }}</p>
              </div>
            </a>
          </div>
        </div>

        <!-- Call to Action -->
        <div class="mt-12 text-center">
          <div class="bg-gradient-to-r from-teal-500 to-emerald-500 rounded-2xl p-8 text-white">
            <h3 class="text-2xl font-heading font-bold mb-4">
              Ready to Start Trading?
            </h3>
            <p class="text-teal-100 mb-6 max-w-2xl mx-auto">
              Now that you understand how prediction markets work, it's time to put your knowledge to the test. 
              Join PredictionMart and start trading on the future today.
            </p>
            <button class="bg-white text-teal-600 hover:bg-gray-100 font-semibold py-3 px-8 rounded-lg transition-all duration-300 transform hover:scale-105">
              Get Started Now
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'YouTubeWidget',
  data() {
    return {
      // Using a placeholder YouTube video about prediction markets
      videoId: 'dQw4w9WgXcQ', // Replace with actual prediction market video ID
      videoTitle: 'Prediction Markets Explained: How to Trade on the Future',
      videoDescription: 'Learn the fundamentals of prediction markets and how they can help you make better forecasts and potentially profit from your insights.',
      videoDuration: '12:34',
      additionalResources: [
        {
          title: 'Wikipedia Article',
          description: 'Comprehensive overview of prediction markets',
          url: 'https://en.wikipedia.org/wiki/Prediction_market',
          iconBg: 'bg-blue-100',
          iconColor: 'text-blue-600',
          iconPath: 'M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253'
        },
        {
          title: 'Academic Papers',
          description: 'Research on prediction market accuracy',
          url: '#',
          iconBg: 'bg-green-100',
          iconColor: 'text-green-600',
          iconPath: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z'
        },
        {
          title: 'Trading Strategies',
          description: 'Advanced techniques for prediction markets',
          url: '#',
          iconBg: 'bg-purple-100',
          iconColor: 'text-purple-600',
          iconPath: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z'
        },
        {
          title: 'Community Forum',
          description: 'Connect with other traders',
          url: '#',
          iconBg: 'bg-orange-100',
          iconColor: 'text-orange-600',
          iconPath: 'M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-2-2V10a2 2 0 012-2h8z'
        }
      ]
    }
  },
  computed: {
    videoEmbedUrl() {
      return `https://www.youtube.com/embed/${this.videoId}?rel=0&modestbranding=1&showinfo=0`
    }
  }
}
</script>
