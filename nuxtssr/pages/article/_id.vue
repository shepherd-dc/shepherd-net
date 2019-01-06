<template>
  <div class="detail">
    <el-row
      :gutter="width > 1080 ? 10 : 0"
      type="flex">
      <el-col :span="width > 1080 ? 18 : 24">
        <el-card class="box-card">
          <div
            slot="header"
            class="head">
            <el-breadcrumb separator=">">
              <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
              <el-breadcrumb-item><a :href="'/'+menu">{{ menu }}</a></el-breadcrumb-item>
              <el-breadcrumb-item v-if="submenu"><a :href="'/'+menu+'/'+submenu">{{ submenu }}</a></el-breadcrumb-item>
              <el-breadcrumb-item>{{ article.title }}</el-breadcrumb-item>
            </el-breadcrumb>
          </div>
          <div class="content">
            <h2 class="title">
              {{ article.title }}
            </h2>
            <div class="author">
              <!-- <span>{{ article.author }} - {{ article.updatetime }}</span> -->
            </div>
            <div
              class="article"
              v-html="article.content"></div>
          </div>
        </el-card>
      </el-col>
      <el-col
        v-if="width > 1080"
        :span="6">
        <el-card class="box-card">
          <div
            slot="header"
            class="clearfix">
            <span>推荐</span>
            <el-button
              style="float: right; padding: 3px 0"
              type="text">更多</el-button>
          </div>
          <div
            v-for="o in 10"
            :key="o"
            class="text item">
            {{ '列表内容 ' + o }}
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  // import AsideCard from '~/components/AsideCard'
  import URL from "~/globalurl"

  export default {
    components: {
      // AsideCard
    },
    data () {
      return {
        width: '',
        menu: '',
        submenu: '',
        article: ''
      }
    },
    // async asyncData ({ app }) {
    //   let { data } = await app.$axios.get(`${URL}/article/${this.$route.params.id}`)
    //   console.log(data)
    //   return {
    //     article: data
    //   }
    // },
    watch: {
      width () {
        this.width = window.innerWidth
      }
    },
    async created () {
      console.log(this.$route)
      let { data } = await this.$axios.get(`${URL}/article/${this.$route.params.id}`)
      // console.log(data)
      this.article = data
      // this.menu = this.$route.params.list
      // this.submenu = this.$route.params.detail
    },
    mounted() {
      let width = window.innerWidth
      this.width = width
    }
  }
</script>

<style lang="less">
  .detail {
    padding-top: 80px;
    max-width: 1280px;
    margin: 0 auto;
  }
  .head {
    padding: 4px 30px;
    font-size: 14px;
  }
  .title {
    text-align: center;
    line-height: 56px;
  }
  .author {
    text-align: center;
    line-height: 36px;
    margin-bottom: 40px;
  }
  .content {
    padding: 30px;
    p {
      margin-bottom: 12px;
      line-height: 26px;
      text-indent: 2rem;
        img {
        display: block;
        margin: 0 auto;
        // width: 100%;
        max-width: 850px;
      }
    }
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
    clear: both
  }
  pre.ql-syntax {
    background-color: #23241f;
    color: #f8f8f2;
    padding: 16px;
    margin: 14px 0;
    overflow: auto;
  }
  blockquote {
    border-left: 4px solid #ccc;
    margin-bottom: 5px;
    margin-top: 5px;
    padding-left: 16px;
  }


</style>

