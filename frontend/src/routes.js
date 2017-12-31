// 首页相关
import Home from './pages/home'

// 用户
import Login from './pages/user/Login.vue'

const routes = [
  {
    path: '/login',
    component: Login,
    name: 'login'
  },
  {
    path: '/',
    component: Home,
    name: 'home'
  }
]

export default routes
