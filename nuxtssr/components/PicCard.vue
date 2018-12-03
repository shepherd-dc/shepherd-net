<template>
  <el-row>
    <el-col>
      <el-card
        :body-style="{ padding: '0px' }"
        shadow="hover">
        <img
          :src="sub_data.pic"
          class="image">
        <div style="padding: 14px;">
          <span>{{ sub_data.title }}</span>
          <div class="bottom clearfix">
            <time class="time">{{ sub_data.time }}</time>
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
}
</script>

<style>
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
