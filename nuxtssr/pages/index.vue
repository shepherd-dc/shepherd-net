<template>
  <section class="container">
    <div>
      <logo/>
      <h1 class="title">
        nuxtssr
      </h1>
      <h2 class="subtitle">
        shepherd net
      </h2>
      <div class="links">
        <p
          v-for="(item, index) in tasks"
          :key="index">{{ item.title }}</p>
      </div>
    </div>
  </section>
</template>

<script>
import Logo from '~/components/Logo.vue'
import { SERVER_URL } from '~/globalurl'

export default {
  components: {
    Logo
  },
  async asyncData ({ app }) {
    let { data } = await app.$axios.get(`${SERVER_URL}/test`)
    // console.log(data)
    return {
      tasks: data.tasks
    }
  }
}
</script>

<style>

.container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
