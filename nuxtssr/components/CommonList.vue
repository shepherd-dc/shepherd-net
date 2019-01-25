<template>
  <section>
    <div class="container">
      <div class="content">
        <el-row
          :gutter="width > 1080 ? 10 : 0"
          type="flex">
          <el-col :span="width > 1080 ? 18 : 24">
            <main-card
              :card_data="card_data"
              :islist="islist"/>
            <article-list :articles_data="articles_data"/>
          </el-col>
          <el-col
            v-if="width > 1080"
            :span="6">
            <aside-card
              :aside_title="title1"
              :aside_data="articles_data"/>
          </el-col>
        </el-row>
      </div>
    </div>
  </section>
</template>

<script>
import URL from '~/globalurl'
import MainCard from '~/components/MainCard'
import AsideCard from '~/components/AsideCard'
import ArticleList from '~/components/ArticleList'
export default {
  components: {
    MainCard,
    AsideCard,
    ArticleList
  },
  props: {
    card_data: {
      type: Object,
      default: () => {}
    },
    articles_data: {
      type: Array,
      default: () => {}
    }
  },
  data () {
    return {
      islist: false,
      title1: '最新'
    }
  },
  computed: {
    width () {
      return this.$store.state.width
    }
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
</style>
