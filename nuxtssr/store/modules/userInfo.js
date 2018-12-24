const userInfo = {
  state: {
    userInfo: {
      nickname: '',
      token: ''
    }
  },
  mutations: {
    ADD_USER_INFO: (state, { data }) => {
      localStorage.setItem('currentUser_name', data.nickname)
      localStorage.setItem('currentUser_token', data.email)
      state.userInfo.nickname = data.nickname
      state.userInfo.token = data.email
    },
    LOGOUT: (state) => {
      localStorage.removeItem('currentUser_name')
      localStorage.removeItem('currentUser_token')
      state.userInfo = {}
    }
  },
  actions: {
    USER_INFO ({ commit }, data) {
      commit('ADD_USER_INFO', data)
    }
  }
}

export default userInfo
