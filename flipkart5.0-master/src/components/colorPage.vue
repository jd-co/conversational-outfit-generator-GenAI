<template>
  <div class="f-container">
    <div class="container">
      <div class="card">
        <div class="content">
          <div class="text-container">
            <p class="typing-text">{{ currentText }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.container {
  text-align: center;
}
.f-container {
  background-image: url('https://res.cloudinary.com/df6tfgugw/image/upload/v1692471149/2007.i121.028.isometric_chatbot_flowchart_de18zz.jpg');
  height: 100vh;
  background-size: cover;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-position: center;
  /* Apply blur effect to the overlay */
}

.card {
  background-color: rgba(
    255,
    255,
    255,
    0.8
  ); /* Card background color with opacity */
  border-radius: 10px;
  padding: 20px;
  margin: 0 auto;
  max-width: 800px; /* Adjust card width as needed */
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.content {
  display: flex;
  align-items: center;
}

.text-container {
  overflow: hidden; /* Ensures text doesn't immediately show */
  border-right: 0.15em solid orange; /* Typing cursor effect */
  white-space: pre-line; /* Allow newline characters to create new lines */
  margin: 0 auto; /* Centers the text */
  letter-spacing: 0.15em; /* Space between characters */
  font-size: 40px;
  color: green;
  /* Fixed width of text container */
  animation: typing 6s steps(40, end);
}

.image-container {
  flex-shrink: 0; /* Prevents image from shrinking */
  margin-left: 20px; /* Add spacing between text and image */
}

.image-icon {
  width: 100%; /* Ensure image width takes up available space */
  max-height: 250px; /* Limit image height while maintaining aspect ratio */
}

@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}

@keyframes blink-caret {
  from,
  to {
    border-color: transparent;
  }
  50% {
    border-color: orange;
  }
}
</style>

<script>
export default {
  data() {
    return {
      textArray: [
        'Welcome to our chatbot website! How can I help you today?',
        'Ask anything about technology trends and innovations.',
        "Curious about machine learning? I've got you covered.",
        'Discover the future of AI and human interaction.',
        'Interact with our virtual assistant and get instant responses.',
        'Stay updated with the latest news in the tech world.',
        "Ready to dive into the world of AI and chatbots? Let's go!",
      ],
      currentIndex: 4,
    }
  },
  computed: {
    currentText() {
      return this.textArray[this.currentIndex]
    },
  },
  mounted() {
    setInterval(this.updateTextAndGif, 2000) // Change the interval as needed
  },
  methods: {
    updateTextAndGif() {
      this.currentIndex = (this.currentIndex + 1) % this.textArray.length
    },
  },
}
</script>
