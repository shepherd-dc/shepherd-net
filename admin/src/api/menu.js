import request from '@/utils/request'

export function fetchMenu(query = '') {
  return request({
    url: `/menu?nav=${query}`,
    method: 'get'
  })
}
