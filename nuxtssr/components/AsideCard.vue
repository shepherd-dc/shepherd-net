<template>
  <el-card class="box-card">
    <div
      slot="header"
      class="clearfix">
      <span>{{ aside_title }}</span>
      <el-button
        style="float: right; padding: 3px 0"
        type="text">更多</el-button>
    </div>
    <div
      v-for="data in aside_data"
      :key="data.id"
      class="text item"
      @click="routerToDetail(data.id)">
      {{ data.title }}
    </div>
  </el-card>
</template>

<script>
export default {
  props: {
    aside_title: {
      type: String,
      default: ''
    },
    aside_data: {
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

<style>
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
  width: 100%;
}
</style>
