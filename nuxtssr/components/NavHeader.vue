<template>
  <div class="header">
    <nav>
      <div class="logo">
        <i><b>SN</b></i>
      </div>
      <el-row
        v-if="width > 1080"
        :gutter="10">
        <el-col
          :xs="12"
          :sm="20"
          :md="24"
          :lg="24"
          :xl="24">
          <drop-down mymode="horizontal"/>
        </el-col>
      </el-row>
      <el-row
        v-if="width <= 1080 && !width == ''"
        :gutter="10">
        <el-col>
          <el-dropdown trigger="click">
            <span class="el-dropdown-link menu">
              <i class="el-icon-menu"/>
            </span>
            <el-dropdown-menu slot="dropdown">
              <drop-down/>
            </el-dropdown-menu>
          </el-dropdown>
        </el-col>
      </el-row>
    </nav>
    <div class="logo">
      Shepherd Net
    </div>
  </div>

</template>

<script>
  import DropDown from '~/components/DropDown.vue'
  export default {
    components: {
      DropDown
    },
    data() {
      return {
        activeIndex: '1',
        width: '',
        isfold: false
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
      // window.onresize =  () => {
      //   this.width = width
      //   console.log(width)
      // }
    },
    methods: {
      mouseenterHandler () {
        this.isfold = true
      },
      mouseleaveHandler () {
        this.isfold = false
      }
    }
  }
</script>

<style lang="less" scoped>
  .header {
    background-color: #333;
    color:#fff;
    height: 60px;
    display:flex;
    .logo {
      // border-right:1px #fff solid;
      padding: 0 20px;
      line-height: 60px;
    }
    nav {
      flex:1;
      display: flex;
      // justify-content: flex-end;
      position:relative;
      .menu {
        font-size:30px;
        color: #fff;
        line-height: 60px;
        padding-right: 20px;
        cursor: pointer;
      }
    }
  }
</style>

