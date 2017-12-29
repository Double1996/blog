import axios from 'axios'

let base = 'http://localhost:8080/api/v1'

export const requestLogin = params => { return axios.post(`${base}/login/`, params).then(res => res.data) }
export const requestRegister = params => { return axios.post(`${base}/register/`, params).then(res => res.data) }
