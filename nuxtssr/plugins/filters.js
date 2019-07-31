import Vue from 'vue'
// 时间格式化
let formatDate = (date, fmt) => {
  let newDate = new Date(date)
  if (/(y+)/.test(fmt)) {
    fmt = fmt.replace(RegExp.$1, (newDate.getFullYear() + '').substr(4 - RegExp.$1.length))
  }
  let o = {
    'M+': newDate.getMonth() + 1,
    'd+': newDate.getDate(),
    'h+': newDate.getHours(),
    'm+': newDate.getMinutes(),
    's+': newDate.getSeconds()
  }
  for (let k in o) {
    if (new RegExp(`(${k})`).test(fmt)) {
      let str = o[k] + ''
      fmt = fmt.replace(RegExp.$1, str)
    }
  }
  return fmt
}

let capitalize = (value) => {
  if (!value) return ''
  value = value.toString()
  return value==='php' ? 'PHP': value.charAt(0).toUpperCase() + value.slice(1)
}

let strSlice = (val, num) => {
  if (!val) return ''
  val = val.toString()
  return val.length > num ? val.slice(0, num) + '...' : val
}

let filters = {
  formatDate,
  capitalize,
  strSlice
}

Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})

export default filters
