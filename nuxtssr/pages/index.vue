<template>
  <section>
    <div class="container">
      <slogan/>
      <!-- <vue-swiper/> -->
      <div class="content">
        <el-row
          :gutter="width > 1080 ? 10 : 0"
          type="flex">
          <el-col :span="width > 1080 ? 18 : 24">
            <main-card
              v-for="(item, index) in card_data"
              :key="index"
              :card_data="item"
              class="card-margin"/>
          </el-col>
          <el-col
            v-if="width > 1080"
            :span="6">
            <aside-card
              :aside_title="title1"
              :aside_data="articles_data"
              class="card-margin" />
          </el-col>
        </el-row>
      </div>
  </div></section>
</template>

<script>
import URL from '~/globalurl'
import Slogan from '~/components/Slogan'
// import VueSwiper from '~/components/VueSwiper'
import MainCard from '~/components/MainCard'
import AsideCard from '~/components/AsideCard'

export default {
  components: {
    Slogan,
    // VueSwiper,
    MainCard,
    AsideCard
  },
  data () {
    return {
      width: '',
      title1: '最新'
    }
  },
  async asyncData ({ app }) {
    let { data } = await app.$axios.get(`${URL}/menu`)
    let articles = await app.$axios.get(`${URL}/article`)
    return {
      card_data: data,
      articles_data: articles.data
    }
  },
  async fetch ({ app }) {
    let { data } = await app.$axios.get(`${URL}/menu`)
    await app.store.commit('ADD_MENUS', data)
  },
  computed: {
    menus () {
      return this.$store.state.menus
    },
    token () {
      return this.$store.state.userInfo.userInfo.token
    }
  },
  watch: {
    width () {
      this.width = window.innerWidth
    }
  },
  mounted() {
    let width = window.innerWidth
    this.width = width
    // let { data } = await this.$axios.get(`${URL}/user`,{
    //   "token": this.token
    // })
    // console.log(this.token)
  }
}
</script>

<style>
  .container {
    padding-top: 60px;
  }
  .content {
    max-width: 1280px;
    margin: 10px auto;
    padding-top: 10px;
  }
  .card-margin {
    margin-bottom: 10px;
  }
  .el-button--text {
    color: #41b883;
  }
</style>
