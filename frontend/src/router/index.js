import Vue from 'vue'
import Router from 'vue-router'
// 用户
// import userLogin from '@/pages/user/Login.vue'

Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/login',
      // component: userLogin,
      name: 'Login'
    }
  ]
})
