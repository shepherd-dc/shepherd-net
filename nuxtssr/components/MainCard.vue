<template>
  <el-card class="box-card">
    <div
      slot="header"
      class="clearfix">
      <span>{{ card_data.menu_name }}</span>
      <el-button
        v-if="islist"
        style="float: right; padding: 3px 0"
        type="text"
        @click="routerTo(card_data.en_name)">更多</el-button>
    </div>
    <div class="text item">
      <el-row>
        <el-col
          v-for="(item, index) in card_data.submenu"
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
    islist: {
      type: Boolean,
      default: true
    },
    card_data: {
      type: Object,
      default: () => {}
    }
  },
  computed: {
    width () {
      return this.$store.state.width
    }
  },
  methods: {
    routerTo (path) {
      this.$router.push({
        path: `/${path}`
      })
    }
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
  margin-bottom: 10px;
}

.card-margin {
  margin-bottom: 20px;
}
</style>
