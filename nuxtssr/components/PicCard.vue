<template>
  <el-row>
    <el-col>
      <el-card
        :body-style="{ padding: '0px' }"
        shadow="hover">
        <img
          src="/card.jpg"
          class="image">
        <div style="padding: 14px;">
          <span>古灯</span>
          <div class="bottom clearfix">
            <time class="time">{{ currentDate }}</time>
            <el-button
              type="text"
              class="button">更多</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

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

<script>
export default {
  data() {
    return {
      currentDate: new Date()
    };
  }
}
</script>
