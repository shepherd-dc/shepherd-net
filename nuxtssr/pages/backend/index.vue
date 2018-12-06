<template>
  <div class="backend">
    <el-card
      class="box-card"
      style="width:1280px;">
      <div
        slot="header"
        class="clearfix">
        <span>卡片名称</span>
      </div>
      <div
        v-for="(item, index) in conferencetype"
        :key="index"
        class="text item">
        {{ item.typeid }} - {{ item.typename }}
        <div
          v-for="(subitem, index) in item.subtype"
          :key="index"
          style="padding-left: 1.4rem">{{ subitem.typeid }} - {{ subitem.typename }}</div>
      </div>
    </el-card>

  </div>
</template>

<script>
  export default {
    data () {
      return {
        "conferencetype": [
          {
            "typeid": 1,
            "typename": "宏观",
            "subtype": [
              {
                "typeid": 1,
                "typename": "行业"
              },
              {
                "typeid": 2,
                "typename": "个股"
              }
            ]
          },
          {
            "typeid": 2,
            "typename": "调研反馈",
            "subtype": [
              {
                "typeid": 1,
                "typename": "行业"
              },
              {
                "typeid": 2,
                "typename": "个股"
              }
            ]
          }
        ]
      }
    }
  }
</script>

<style>
  .backend{
    padding-top: 80px;
  }
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
    clear: both
  }

  .box-card {
    margin: 0 auto;
    height: 860px;
  }
</style>
