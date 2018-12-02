<template>
  <el-card class="box-card">
    <div
      slot="header"
      class="clearfix">
      <span>卡片名称</span>
      <el-button
        style="float: right; padding: 3px 0"
        type="text">更多</el-button>
    </div>
    <div class="text item">
      <el-row type="felx">
        <el-col
          v-for="o in 3"
          :key="o"
          :span="8">
          <pic-card/>
        </el-col>
      </el-row>
    </div>
  </el-card>
</template>

<script>
import PicCard from './PicCard'
export default {
  components: {
    PicCard
  }
}
</script>

<style lang="less" scoped>
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
