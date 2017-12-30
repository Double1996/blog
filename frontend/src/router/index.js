import Vue from 'vue'
import VueRouter from 'vue-router'
// 用户
import UserLogin from '@/pages/user/Login.vue'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/login',
      component: UserLogin,
      name: 'Login'
    }
  ]
})

export default router
