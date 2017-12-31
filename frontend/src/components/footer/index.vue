<template lang="html">
  <footer class="df-footer">
    <span>&copy;  声连网支持中心 {{ date }}. All Rights Reserved.</span>
 		<div class="beian">
      <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33030202000623">
        <span>福建网安备 33030202000623号</span>
      </a>
      <a href="http://www.miitbeian.gov.cn/" target="_blank">闽ICP备17006153号-1</a>
 		</div>
    <button class="admin-login" @click="adminLogin" :disabled="adminLoginVisible"></button>
  </footer>

</template>

<script>
export default {
  name: 'footer',
  data () {
    return {
      adminLoginVisible: false
    }
  },
  computed: {
    date () {
      return new Date().getFullYear()
    }
  },
  methods: {
  }
}
</script>

<style lang="stylus" scoped>

.df-footer
  position absolute
  bottom 0
  width 100%
  padding 20px 0
  border-top 1px solid Light-Grey
  font(.7em,Light-Silver)
  text-align center
  .beian
    margin-top 10px
    a
      text-decoration none
      color Light-Silver
  .admin-login
    position absolute
    bottom 0
    right 0
    wh(40px,40px)
    outline none
    border 0
    background-color inherit
</style>
