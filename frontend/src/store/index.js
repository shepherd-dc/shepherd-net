import Vue from 'vue'
import Vuex from 'vuex'
import userInfo from './modules/userInfo'
import user from './modules/user'
import errorLog from './modules/errorLog'
import getters from './getters'
// import createPersist from 'vuex-localstorage'
import language from './modules/language'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    errorLog,
    user,
    userInfo,
    language
  },
  getters
  // plugins: [createPersist({
  //   namespace: 'namespace-for-state',
  //   initialState: {},
  //   expires: 7 * 24 * 60 * 60 * 1e3
  // })]
})

export default store
