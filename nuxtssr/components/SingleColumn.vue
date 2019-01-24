<template>
  <section>
    <div class="container">
      <div class="content">
        <el-row
          :gutter="width > 1080 ? 10 : 0"
          type="flex">
          <el-col :span="width > 1080 ? 18 : 24">
            <el-card class="box-card">
              <div
                slot="header"
                class="clearfix">
                <el-breadcrumb separator=">">
                  <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
                  <el-breadcrumb-item><a @click.stop="routerBread">{{ column_data.menu_name }}</a></el-breadcrumb-item>
                  <el-breadcrumb-item>{{ column_data.name }}</el-breadcrumb-item>
                </el-breadcrumb>
              </div>
              <div class="text">
                <el-row type="felx">
                  <el-col :span="width > 1080 ? 8 : 24">
                    <a
                      :href="column_data.official_doc"
                      target="_blank">
                      <div class="image">
                        <img :src="column_data.pic">
                      </div>
                      <a/>
                  </a></el-col>
                  <el-col :span="width > 1080 ? 16 : 24">
                    <div class="text-info">
                      <h4 class="detail-title">{{ column_data.name | capitalize }}
                        <a
                          :href="column_data.official_doc"
                          target="_blank">
                          <el-button
                            style="float: right; padding: 5px 0"
                            type="text">官方文档</el-button>
                        </a>
                      </h4>
                      <div class="clearfix">
                        <p class="description">{{ column_data.description }}
                          <a
                            :href="column_data.official_doc"
                            target="_blank">
                            <el-button
                              style="float: right; padding: 5px 0"
                              type="text"> 更多 >></el-button>
                          </a>
                        </p>
                      </div>
                    </div>
                  </el-col>
                </el-row>
              </div>
            </el-card>
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
import URL from "~/globalurl"
import PicCard from "~/components/PicCard"
import AsideCard from "~/components/AsideCard"
import ArticleList from "~/components/ArticleList"

export default {
  components: {
    PicCard,
    AsideCard,
    ArticleList
  },
  props: {
    column_data: {
      type: Object,
      default: () => {}
    },
    articles_data: {
      type: Array,
      default: () => {}
    }
  },
  data() {
    return {
      width: '',
      title1: '最新'
    }
  },
  watch: {
    width() {
      this.width = window.innerWidth
    }
  },
  async created() {
    // let { data } = await this.$axios.get(
    //   `${URL}/menu/sublist/${this.$route.params.item}`
    // )
    // console.log(this.$route)
  },
  mounted() {
    let width = window.innerWidth
    this.width = width
    // console.log(this.column_data)
  },
  methods: {
    routerToDetail (id) {
      this.$router.push({
        path: `/article/${id}`
      })
    },
    routerBread () {
      this.$router.push({
        path: `/${this.column_data.path.split('/')[0]}`
      })
    }
  },
}
</script>

<style lang="less">
.container {
  padding-top: 60px;
}
.content {
  max-width: 1280px;
  margin: 10px auto;
  padding-top: 10px;
}
.box-card {
  margin-bottom: 10px;
}
.el-breadcrumb__inner.is-link:hover, .el-breadcrumb__inner a:hover {
  color: #41b883;
}
.el-breadcrumb {
  line-height: 22px;
}
.el-button--text {
  color: #41b883;
}
</style>

<style lang="less" scoped>
  .text-info {
    padding: 0 0 0 20px;
  }
  .detail-title {
    font-size: 18px;
  }

  .description {
    font-size: 14px;
    color: #999;
    line-height: 28px;
    margin: 16px 0;
  }

  .image {
    height: 150px;
    border-radius: 6px;
    overflow: hidden;
    cursor: pointer;
    img {
      display: block;
      width: 100%;
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
</style>
