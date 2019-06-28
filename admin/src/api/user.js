import request from '@/utils/request'

export function fetchUserList(query = '') {
  return request({
    url: `user/list`,
    method: 'get',
    params: query
  })
}
