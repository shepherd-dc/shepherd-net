import Vue from 'vue'
import Vuex from 'vuex'
import URL from '~/globalurl'
import getters from './getters/getters'
import errorLog from './modules/errorLog'
import userInfo from './modules/userInfo'

Vue.use(Vuex)

const store = () => new Vuex.Store({
  state: {
    width: 1080,
    menus: []
  },
  mutations: {
    ADD_MENUS: (state, data) => {
      state.menus = data
      // console.log(data)
    },
    SET_WIDTH: (state, width) => {
      state.width = width
    }
  },
  actions: {
    async nuxtServerInit({ commit }, context) {
      let { data } = await context.$axios.get(`${URL}/menu`)
      commit('ADD_MENUS', data)
    },
    SetWidth ({ commit }, width) {
      commit('SET_WIDTH', width)
    }
  },
  getters,
  modules: {
    errorLog,
    userInfo
  }
})

export default store
