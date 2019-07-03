const menu = {
  state: {
    menu: []
  },
  mutations: {
    FetchMenu: (state, payload) => {
      state.menu = payload
    }
  }
}

export default menu
