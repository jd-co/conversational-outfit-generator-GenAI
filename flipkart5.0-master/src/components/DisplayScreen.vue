<template>
  <div class="row" style="height: 100vh">
    <div class="col-lg-8 scrollable-col">
      <nav
        class="navbar navbar-expand-lg m-4 rounded"
        style="background-color: black"
      >
        <a class="navbar-brand text-white mx-4" href="#">Flipkart ChatBot</a>
      </nav>
      <div class="position-relative h-100">
        <div class="product-container">
          <div>
            <p class="heading">Shop</p>
            <p class="text-secondary">Shop for your needs</p>
            <div class="d-flex gap mt-5">
              <div v-for="(keyword, index) in keywords" :key="index">
                <div class="">
                  <a class="btn btn-outline-secondary text-dark">{{
                    keyword
                  }}</a>
                </div>
              </div>
            </div>
            <div>
              <div v-for="(product, index) in products" :key="index">
                <p class="mt-3 secondary">{{ product["name"] }}</p>
                <div class="container mt-4">
                  <div
                    v-for="(detail, index) in product['details']"
                    :key="index"
                  >
                    <div class="card">
                      <div class="card-body">
                        <img :src="detail['img']" :style="{ width: '100%' }" />
                        <div class="p-3">
                          <div class="mb-3">
                            <p class="text-secondary" style="font-weight: 500">
                              {{ detail["brand"] }}
                            </p>
                            <p>{{ detail["name"] }}</p>
                            <p>{{ detail["price"] }}</p>
                          </div>
                          <div class="key-container">
                            <div
                              v-for="(keyword, index) in detail['keyword']"
                              :key="index"
                            >
                              <div class="">
                                <a
                                  class="btn btn-outline-secondary text-dark"
                                  >{{ keyword }}</a
                                >
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-lg-4 fixed-col">
      <div style="background-color: black">
        <nav class="navbar navbar-expand-lg navbar-light bg-primary">
          <a class="navbar-brand mx-4 text-white" href="#">Assistant</a>
        </nav>
        <div
          class="p-3"
          style="
            background-image: url('https://d1tgh8fmlzexmh.cloudfront.net/ccbp-static-website/chatbg.png');
          "
        >
          <div class="messages">
            <div
              v-for="(message, index) in chatMessages"
              :key="index"
              class="message mb-3"
            >
              <div :class="`${message['from']} px-3 py-2 rounded`">
                {{ message.text }}
              </div>
            </div>
          </div>
          <div class="fixed">
            <div class="user-input">
              <input
                v-model="userInput"
                @keyup.enter="sendMessage"
                placeholder="Type your message..."
              />
              <a @click="sendMessage" class="btn btn-primary mx-2">Send</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "page-displayScreen",
  data() {
    return {
      keywords: ["Under 10000", "Track Pants", "Jeans", "Watches", "Similar"],
      products: [],
      chatMessages: [
        { text: "Hello! I'm your chatbot. How can I assist you?", from: "bot" },
      ],
      userInput: "",
    };
  },
  components: {},
  props: {
    msg: String,
  },
  methods: {
    sendMessage() {
      const userMessage = { text: this.userInput, from: "user" };
      this.userInput = "";
      this.chatMessages.push(userMessage);
      const data = {
        query: this.userInput,
      };
      axios
        .post("http://localhost:2000/query", data)
        .then((response) => {
          console.log(response);
          const botMessage = { text: response.data.text, from: "bot" };
          this.chatMessages.push(botMessage);
          this.products = response.data.products;
          // if (response.request.status == 200) {
          //   // this.flash_message = response.data.message;
          // } else {
          //   // this.flash_message = response.data.message;
          // }
        })
        .catch((error) => {
          console.error("Login failed:", error);
        });
      // const userMessage = { text: this.userInput, from: "user" };
      // this.chatMessages.push(userMessage);
      // this.userInput = "";
      // setTimeout(() => {
      //   const botResponse = {
      //     text: "I'm a simple chatbot. I don't understand everything.",
      //     from: "bot",
      //   };
      //   this.chatMessages.push(botResponse);
      // }, 500);
    },
  },
};
</script>
<style scoped>
.scrollable-col {
  height: 100%;
  overflow-y: scroll;
}
.gap {
  gap: 3rem;
}
/* Customize scrollbar appearance */
.scrollable-col::-webkit-scrollbar {
  width: 0em;
  background-color: #f5f5f5;
}

.scrollable-col::-webkit-scrollbar-thumb {
  background-color: #c1c1c1;
  border-radius: 4px;
}

.fixed-col {
  position: sticky;
  top: 0;
  height: 100vh;
}
p {
  margin: 0;
}
.heading {
  font-size: 1.6rem;
  font-weight: 400;
}
.secondary {
  font-size: 1.2rem;
  font-weight: 400;
}
.product-container {
  position: absolute;
  top: 4%;
  left: 8%;
  width: 85%;
}
.container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(15vw, 1fr));
  gap: 20px;
}
.key-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.card-body {
  padding: 0;
}
.scrollable {
  height: 80%;
}
.fixed {
  position: sticky;
  bottom: 0;
}
.messages {
  height: 80vh;
  overflow: auto;
}
.messages::-webkit-scrollbar {
  width: 0em;
}

.messages::-webkit-scrollbar-thumb {
  background-color: #888;
  border-radius: 4px;
}

.messages::-webkit-scrollbar-track {
  background-color: transparent;
}
.message {
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

.user-input {
  display: flex;
  margin-top: 10px;
}

.user-input input {
  flex: 1;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.user {
  background-color: #007bff;
  align-self: flex-end;
  max-width: 70%;
  background-color: white;
  color: black;
}

.bot {
  background-color: #28a745;
  align-self: flex-start;
  max-width: 70%;
  background-color: grey;
  color: white;
}
.user-input button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
}
</style>
