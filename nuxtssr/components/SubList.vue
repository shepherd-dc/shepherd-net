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
                <span>{{ sub_data.menu_name }}</span>
              </div>
              <div class="text item">
                <el-row type="felx">
                  <el-col :span="width > 1080 ? 8 : 24">
                    <pic-card
                      :sub_data="sub_data"
                      :issublist="issublist"/>
                  </el-col>
                </el-row>
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
  data() {
    return {
      width: "",
      issublist: false,
      sub_data: {},
      aside_title: ["最新", "推荐", "友链"]
    }
  },
  watch: {
    width() {
      this.width = window.innerWidth
    }
  },
  async created() {
    let { data } = await this.$axios.get(
      `${URL}/menu/sublist/${this.$route.params.item}`
    )
    // console.log(data)
    this.sub_data = data
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
</style>
