import Vue from 'vue'
import Vuex from 'vuex'
import URL from '~/globalurl'
import getters from './getters/getters'
import errorLog from './modules/errorLog'
import userInfo from './modules/userInfo'

Vue.use(Vuex)

const store = () => new Vuex.Store({
  state: {
    menus: []
  },
  mutations: {
    ADD_MENUS: (state, data) => {
      state.menus = data
      // console.log(data)
    }
  },
  actions: {
    async nuxtServerInit({ commit }, context) {
      let { data } = await await context.$axios.get(`${URL}/menu`)
      await commit('ADD_MENUS', data)
    }
  },
  getters,
  modules: {
    errorLog,
    userInfo
  }
})

export default store
