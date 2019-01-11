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
            <el-breadcrumb separator=">">
              <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
              <el-breadcrumb-item><a :href="'/'+menu">{{ menu }}</a></el-breadcrumb-item>
              <el-breadcrumb-item>{{ submenu }}</el-breadcrumb-item>
            </el-breadcrumb>
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
        articles: [],
        menu: '',
        submenu: ''
      }
    },
    watch: {
      width () {
        this.width = window.innerWidth
      }
    },
    async created () {
      let { data } = await this.$axios.get(`${URL}/article`)
      let path = this.$route.fullPath
      this.menu = path.split('/')[1]
      this.submenu = path.split('/')[2]
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

