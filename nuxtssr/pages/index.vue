<template>
  <section class="container">
    <div>
      <vue-swiper/>
      <div class="content">
        <el-row
          :gutter="10"
          type="flex">
          <el-col :span="18">
            <div
              v-for="o in 2"
              :key="o"
              class="card-margin">
              <main-card/>
            </div>
          </el-col>
          <el-col :span="6">
            <div
              v-for="o in 3"
              :key="o"
              class="card-margin">
              <aside-card/>
            </div>
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
