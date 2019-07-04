import request from '@/utils/request'

export function fetchUserList(query = '') {
  return request({
    url: `user/list`,
    method: 'get',
    params: query
  })
}

export function userDetail(id) {
  return request({
    url: `/user/${id}`,
    method: 'get'
  })
}

export function addUser(data) {
  return request({
    url: `/user/add`,
    method: 'post',
    data
  })
}

export function editUser(data) {
  return request({
    url: `/user/edit`,
    method: 'put',
    data
  })
}

export function deleteUser(data) {
  return request({
    url: `/user/delete`,
    method: 'post',
    data
  })
}

export function hardDeleteUser(data) {
  return request({
    url: `/user/delete`,
    method: 'delete',
    data
  })
}
