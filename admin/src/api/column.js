import URL from '@/globalurl'
import request from '@/utils/request'

export function menuList(query = '') {
  return request({
    url: `${URL}/menu`,
    method: 'get',
    params: query
  })
}

export function submenuList(query = '') {
  return request({
    url: `${URL}/menu/submenu`,
    method: 'get',
    params: query
  })
}
