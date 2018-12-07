<template>
  <el-row>
    <el-col>
      <el-card
        :body-style="{ padding: '0px' }"
        shadow="hover">
        <img
          :src="sub_data.pic"
          class="image"
          @click="routerTo(sub_data.id)">
        <div class="text-info">
          <h4
            class="detail-title"
            @click="routerTo(sub_data.id)">{{ sub_data.name }}</h4>
          <div class="bottom clearfix">
            <time class="time">2018-12-7</time>
            <el-button
              type="text"
              class="button">更多</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
export default {
  props: {
    sub_data: {
      type: Object,
      default: () => {}
    }
  },
  data() {
    return {
      currentDate: new Date()
    }
  },
  methods: {
    routerTo (id) {
      this.$router.push({
        path: `/detail/${id}`
      })
    }
  }
}
</script>

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
