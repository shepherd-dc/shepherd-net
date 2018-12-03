<template>
  <section class="container">
    <div>
      <slogan/>
      <!-- <vue-swiper/> -->
      <div class="content">
        <el-row
          :gutter="width > 1080 ? 10 : 0"
          type="flex">
          <el-col :span="width > 1080 ? 18 : 24">
            <main-card
              v-for="(title, index) in card_title"
              :key="index"
              :card_title="title"
              class="card-margin"/>
          </el-col>
          <el-col
            v-if="width > 1080"
            :span="6">
            <aside-card
              v-for="(title, index) in aside_title"
              :key="index"
              :aside_title="title"
              class="card-margin" />
          </el-col>
        </el-row>
      </div>
    </div>
  </section>
</template>

<script>
import { SERVER_URL } from '~/globalurl'
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
      card_title: [
        '前台',
        '后台'
      ],
      aside_title: [
        '最新',
        '推荐',
        '友链'
      ]
    }
  },
  async asyncData ({ app }) {
    let { data } = await app.$axios.get(`${SERVER_URL}/test`)
    // console.log(data)
    return {
      tasks: data.tasks
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
  }
}
</script>

<style>
  .content {
    max-width: 1280px;
    margin: 10px auto;
    padding-top: 10px;
  }
  .card-margin {
    margin-bottom: 10px;
  }
</style>
