import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters/getters'
import errorLog from './modules/errorLog'

Vue.use(Vuex)

const store = () => new Vuex.Store({
  state: {
    menus: []
  },
  mutations: {
    ADD_MENUS: (state, data) => {
      state.menus = data
      console.log(data)
    }
  },
  getters,
  modules: {
    errorLog
  }
})

export default store
