<<template>
  <el-form :model="loginForm" class="login-container" :rules="loginRule">
  <h3 class="title">double的blog</h3>
  <el-form-item prop="email">
    <el-input type="text" v-model="loginForm.email" placeholder="电子邮箱", auto-complete="off"></el-input>
  </el-form-item>
  <el-form-item prop="password">
    <el-input v-model="loginForm.password" placeholder="密码"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click.native.prevent="handleLogin" :loading="logining">
      登录
    </el-button>
  </el-form-item>
  </el-form>
</template>
<script>
  import { requestLogin } from '../../api'
  
  export default {
    name: 'UserLogin',
    data () {
      return {
        logining: false,
        loginForm: {
          email: '',
          password: ''
        },
        loginRule: {
          email: [
            {requierd: true, message: '请输入电子邮箱', trigger: 'blur'}
          ],
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'}
          ]
        }
      }
    },
    methods: {
      handleLogin () {
        this.$refs.loginForm.validate((valid) => {
          if (valid) {
            this.logining = true
            let loginParams = {email: this.loginForm.email, password: this.loginForm.password}
            requestLogin(loginParams).then(data => {
              this.login = false
              let {msg, code} = data
              if (code !== 0) {
                this.$msg({
                  msg: msg,
                  type: 'error'
                })
              } else {
                this.$router.push({path: '/'})
                // ssionStorage.setItem('token', JSON.stringify(token))
              }
            })
          } else {
            return false
          }
        }
        )
      }
    }
  }
</script>
<<style lang="scss" scoped>
  .login-container {
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    margin: 180px auto;
    width: 350px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
    .title {
      margin: 0px auto 40px auto;
      text-align: center;
      color: #505458;
    }
    .remember {
      margin: 0px 0px 35px 0px;
    }
  }
</style>

