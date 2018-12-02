<template>
  <section class="container">
    <div>
      <vue-swiper/>
      <div class="content">
        <el-row
          :gutter="10"
          type="flex">
          <el-col :span="18">
            <main-card
              v-for="(title, index) in card_title"
              :key="index"
              :card_title="title"
              class="card-margin"/>
          </el-col>
          <el-col :span="6">
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
import VueSwiper from '~/components/VueSwiper'
import MainCard from '~/components/MainCard'
import AsideCard from '~/components/AsideCard'

export default {
  components: {
    VueSwiper,
    MainCard,
    AsideCard
  },
  data () {
    return {
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
  }
}
</script>

<style>
  .content {
    max-width: 1280px;
    margin: 0 auto;
    padding-top: 10px;
  }
  .card-margin {
    margin-bottom: 10px;
  }
</style>
