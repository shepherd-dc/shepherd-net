<template>
  <el-card class="box-card">
    <div
      slot="header"
      class="clearfix">
      <span>{{ card_title }}</span>
      <el-button
        style="float: right; padding: 3px 0"
        type="text">更多</el-button>
    </div>
    <div class="text item">
      <el-row type="felx">
        <el-col
          v-for="(item, index) in card_data"
          :key="index"
          :span="width > 1080 ? 8 : 24">
          <pic-card
            :sub_data="item"
            class="card-margin"/>
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
  },
  props: {
    card_title: {
      type: String,
      default: ''
    },
    card_data: {
      type: Array,
      default: () => {}
    }
  },
  data () {
    return {
      width: ''
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

.card-margin {
  margin-bottom: 20px;
}
</style>
