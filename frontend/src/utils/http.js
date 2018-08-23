/**
 * http axiosconfig
 */
import axios from 'axios'
import store from '../store'
import { getToken } from '@/utils/auth'
import qs from 'querystring'
// axios config
const defaultHeaders = {
  'Accept': 'application/json',
  'Content-Type': 'application/json' // application/x-www-form-urlencoded
}
// axios.defaults.withCredentials = true

/**
 * 检查response状态
 * @param response
 */
const service = axios.create({
  baseURL: process.env.BASE_API, // api的base_url
  timeout: 20000 // 请求超时时间
})

// request拦截器
service.interceptors.request.use(config => {
  config.headers = defaultHeaders
  if (store.getters.token) {
    config.headers['accesstoken'] = getToken() // 让每个请求携带自定义token 请根据实际情况自行修改
  }
  return config
}, error => {
  // Do something with request error
  console.log(error) // for debug
  Promise.reject(new Error(error))
})

// respone拦截器
service.interceptors.response.use(
  response => {
    /**
     * result为非0时抛错 可结合自己业务进行修改
     */

    // const res = response.data
    // console.log(res)
    // debugger
    // let message = 'error'
    // if (res.resultcode !== '1') {
    //   console.log(res.message)
    //   return Promise.reject(new Error(message))
    // } else {
    return response.data
    // }
  },
  error => {
    let msg = error.message
    if (error.response) {
      switch (error.response.status) {
        case 400:
          // 访问地址不存在
          msg = '访问地址不存在'
          break
        case 302:
          msg = '302'
          break
      }
    }
    console.log('err' + error + msg)// for debug
    return Promise.reject(new Error(error))
  }
)

export default service

export const post = (url, args = {}, options = {}) => {
  // debugger
  return service({
    url: url,
    method: 'post',
    data: args
  })
}

export const get = (url, args, options = {}) => {
  let query = args
  if (args) {
    if (typeof query === 'object') {
      query = qs.stringify(query)
    }
    url += (url.indexOf('?') !== -1) ? '&' : '?'
    url += query
  }
  // console.log(url)
  return service({
    url: url,
    method: 'get',
    data: args
  })
}
