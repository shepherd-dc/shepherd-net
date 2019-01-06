<template>
  <div class="article">
    <el-row
      :gutter="width > 1080 ? 10 : 0"
      type="flex">
      <el-col
        :span="width > 1080 ? 18 : 24"
        :offset="width > 1080 ? 3 : 0">
        <el-card class="box-card">
          <div
            slot="header"
            class="clearfix">
            <span>文章列表</span>
            <el-button
              style="float: right; padding: 3px 0"
              type="text">更多</el-button>
          </div>
          <div
            v-for="article in articles"
            :key="article.id"
            class="text item"
            @click="routerToDetail(article.id)">
            {{ article.title }}
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import URL from '~/globalurl'
  export default {
    components: {
      // list
    },
    // async asyncData ({ app }) {
    //   let { data } = await app.$axios.get(`${URL}/article`)
    //   // console.log(data)
    //   return {
    //     articles: data
    //   }
    // },
    data () {
      return {
        width: '',
        articles: []
      }
    },
    watch: {
      width () {
        this.width = window.innerWidth
      }
    },
    async created () {
      let { data } = await this.$axios.get(`${URL}/article`)
      console.log(data)
      this.articles = data
    },
    mounted() {
      let width = window.innerWidth
      this.width = width
      // let { data } = await this.$axios.get(`${URL}/user`,{
      //   "token": this.token
      // })
      // console.log(this.token)
    },
    methods: {
      routerToDetail (id) {
        this.$router.push({
          path: `/article/${id}`
        })
      }
    }
  }
</script>

<style lang="less" scoped>
  .article {
    padding-top: 60px;
    min-height: 92vh;
  }
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both;
  }
  .box-card {
    margin-top: 30px;
    .publish-head {
      font-size: 18px;
      font-weight: bold;
      text-align: center;
    }
    .item-body {
      padding-right: 30px;
    }
  }
</style>

