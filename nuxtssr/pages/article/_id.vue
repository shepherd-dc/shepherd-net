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
              <el-breadcrumb-item><a :href="'/'+menu">{{ menuBread }}</a></el-breadcrumb-item>
              <el-breadcrumb-item><a :href="'/'+menu+'/'+submenuBread">{{ submenuBread }}</a></el-breadcrumb-item>
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
        <aside-card
          :aside_title="title1"
          :aside_data="articles_data"
          class="card-margin"
        />
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import AsideCard from '~/components/AsideCard'
  import URL from "~/globalurl"

  export default {
    components: {
      AsideCard
    },
    data () {
      return {
        width: '',
        title1: '最新'
      }
    },
    async asyncData (context) {
      let { data } = await context.$axios.get(`${URL}/article/${context.params.id}`)
      // console.log(data)
      let articles = await context.$axios.get(`${URL}/article`)
      return {
        article: data,
        menuBread: data.menu_name,
        submenuBread: data.column_name,
        menu: data.en_name,
        articles_data: articles.data
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
      // console.log(this.menuBread)
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
    padding: 0 30px;
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

  .el-breadcrumb {
    line-height: 22px;
  }
  .el-button--text {
    color:#41b883;
  }
  .item {
  cursor: pointer;
  &:hover {
    color: #41b883;
  }
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

