<template>
  <div class="header">
    <nav>
      <a href="/">
        <div class="logo">
          <i><b>SN</b></i>
        </div>
      </a>
      <el-row
        v-if="width > 1080"
        :gutter="10">
        <el-col
          :xs="12"
          :sm="20"
          :md="24"
          :lg="24"
          :xl="24">
          <common-nav mymode="horizontal"/>
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
              <common-nav/>
            </el-dropdown-menu>
          </el-dropdown>
        </el-col>
      </el-row>
    </nav>
    <div class="login">
      <div v-if="!token && !userInfo.token">
        <span @click="routerToLogin()">登录</span> | <span @click="routerToRegister()">注册</span>
      </div>
      <div v-if="token || userInfo.token">
        <span>{{ userInfo.nickname || nickname }}</span> | <span @click="routerToLogout()">退出</span>
      </div>
    </div>
  </div>

</template>

<script>
  import URL from '~/globalurl'
  import CommonNav from './CommonNav'
  export default {
    components: {
      CommonNav
    },
    data () {
      return {
        activeIndex: '1',
        width: '',
        isfold: false,
        token: '',
        nickname: ''
      }
    },
    computed: {
      userInfo () {
        return this.$store.state.userInfo.userInfo
      }
    },
    watch: {
      width () {
        this.width = window.innerWidth
      }
    },
    async mounted () {
      let width = window.innerWidth
      this.width = width
      this.token = localStorage.getItem('token')
      if (this.token) {
        let { data } = await this.$axios.post(`${URL}/token/secret`,{
          "token": this.token
        })
        this.nickname = data.nickname
      }
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
      },
      routerToLogin () {
        this.$router.push({
          path: `/login`
        })
      },
      routerToRegister () {
        this.$router.push({
          path: `/register`
        })
      },
      routerToLogout () {
        this.$store.commit('LOGOUT')
        this.token = ''
        location = '/'
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
    .login {
      font-size: 14px;
      padding: 0 20px;
      line-height: 60px;
      span {
        cursor: pointer;
        &:hover {
          color: #41b883
        }
      }
    }
  }
</style>

