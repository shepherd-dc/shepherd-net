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

export function menuDetail(query = '') {
  return request({
    url: `${URL}/menu/detail`,
    method: 'get',
    params: query
  })
}

export function saveSubmenu(data) {
  return request({
    url: `${URL}/menu/submenu/save`,
    method: 'post',
    data
  })
}

export function deleteSubmenu(data) {
  return request({
    url: `${URL}/menu/submenu/delete`,
    method: 'delete',
    data
  })
}
