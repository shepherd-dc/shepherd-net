const userInfo = {
  state: {
    userInfo: {
      isLogin: false
    }
  },
  mutations: {
    ADD_USER_INFO: (state, data) => {
      // console.log(data)
      state.userInfo = data
    },
    LOGOUT: (state) => {
      state.userInfo = {}
    }
  },
  actions: {
    USER_INFO ({ commit }, data) {
      data.isLogin = true
      commit('ADD_USER_INFO', data)
    }
  }
}

export default userInfo
