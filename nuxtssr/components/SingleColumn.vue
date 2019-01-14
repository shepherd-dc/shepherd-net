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
                  <el-breadcrumb-item><a :href="'/'+column_data.path.split('/')[0]">{{ column_data.menu_name }}</a></el-breadcrumb-item>
                  <el-breadcrumb-item>{{ column_data.name }}</el-breadcrumb-item>
                </el-breadcrumb>
              </div>
              <div class="text item">
                <el-row type="felx">
                  <el-col :span="width > 1080 ? 8 : 24">
                    <el-card
                      :body-style="{ padding: '0px' }"
                      shadow="hover">
                      <img
                        :src="column_data.pic"
                        class="image">
                      <div class="text-info">
                        <h4
                          class="detail-title">{{ column_data.name }}</h4>
                        <div class="bottom clearfix">
                          <time class="time">2018-12-7</time>
                        </div>
                      </div>
                    </el-card>
                  </el-col>
                </el-row>
              </div>
            </el-card>
            <el-card class="box-card">
              <div
                slot="header"
                class="clearfix">
                <span>文章列表</span>
              </div>
              <div
                v-for="article in articles_data"
                :key="article.id"
                class="text item"
                @click="routerToDetail(article.id)">
                {{ article.title }}
              </div>
            </el-card>
          </el-col>
          <el-col
            v-if="width > 1080"
            :span="6">
            <aside-card
              v-for="(title, index) in aside_title"
              :key="index"
              :aside_title="title"
              class="card-margin"
            />
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

export default {
  components: {
    PicCard,
    AsideCard
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
      width: "",
      aside_title: ["最新", "推荐", "友链"]
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
    console.log(this.column_data)
  },
  methods: {
    routerToDetail (id) {
      this.$router.push({
        path: `/article/${id}`
      })
    }
  },
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
.box-card {
  margin-bottom: 10px;
}
</style>

<style lang="less" scoped>
  .text-info {
    padding: 14px;
  }
  .detail-title {
    cursor: pointer;
    &:hover {
      color: #41b883;
    }
  }

  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
    cursor: pointer;
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
