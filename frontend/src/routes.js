// 首页相关
import Home from './pages/home'

// 用户
import login from './pages/user/Login.vue'
import userRegister from './pages/user/Register.vue'

const routes = [
  {
    path: '/register',
    component: userRegister,
    name: 'userRegister'
  },
  {
    path: '/login',
    component: login,
    name: 'login'
  },
  {
    path: '/',
    component: Home,
    name: 'home'
  }
]

export default routes
