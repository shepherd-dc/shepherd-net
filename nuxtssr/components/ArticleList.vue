<template>
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
</template>

<script>
export default {
  props: {
    articles_data: {
      type: Array,
      default: () => {}
    }
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

<style lang="less">
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
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
  clear: both;
}

.box-card {
  width: 100%;
}
</style>
