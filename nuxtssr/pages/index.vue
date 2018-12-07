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
              v-for="(title, index) in aside_title"
              :key="index"
              :aside_title="title"
              class="card-margin" />
          </el-col>
        </el-row>
      </div>
      <div
        v-for="(item, index) in data"
        :key="index">{{ item.name }}
        <p
          v-for="(sub, i) in item.submenu"
          :key="i">{{ sub }}</p>
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
      card_data: [
        {
          "columnid": 1,
          "column": "前端",
          "data": [
            {
              "id": 1,
              "pic": "/card.jpg",
              "title": "标题1",
              "time": "2018-12-3 17:40:50"
            },
            {
              "id": 2,
              "pic": "/card.jpg",
              "title": "标题2",
              "time": "2018-12-3 17:41:51"
            },
            {
              "id": 3,
              "pic": "/card.jpg",
              "title": "标题3",
              "time": "2018-12-3 17:42:52"
            }
          ]
        },
        {
          "columnid": 2,
          "column": "后端",
          "data": [
            {
              "id": 1,
              "pic": "/card.jpg",
              "title": "标题1",
              "time": "2018-12-3 17:40:50"
            },
            {
              "id": 2,
              "pic": "/card.jpg",
              "title": "标题2",
              "time": "2018-12-3 17:41:51"
            },
            {
              "id": 3,
              "pic": "/card.jpg",
              "title": "标题3",
              "time": "2018-12-3 17:42:52"
            }
          ]
        }
      ],
      aside_title: [
        '最新',
        '推荐',
        '友链'
      ]
    }
  },
  async asyncData ({ app }) {
    let { data } = await app.$axios.get(`${SERVER_URL}/menu`)
    console.log(data)
    return {
      data: data
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
</style>
