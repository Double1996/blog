<template lang="html">
  <el-menu class="df-header" default-active="1" mode="horizontal" :router="true">
    <el-row justify="space-around" type="flex">
      <el-col class="nav" :span="8">
        <el-menu-item index="1" :route="{ name:'home' }">首页</el-menu-item>
        <el-menu-item index="2" :route="{ name:'poem' }">分类</el-menu-item>
        <el-menu-item index="4" :route="{ name:'apprec' }">ABOUT ME</el-menu-item>
      </el-col>
      <el-col class="searchbar-wrapper" :span="7">
        <el-input
          class="searchbar c-form"
          icon="search"
          placeholder="搜索您感兴趣的博文"
        ></el-input>
      </el-col>
       <el-menu-item index="6" :route="{ name:'login' }">登录</el-menu-item>
    </el-row>
  </el-menu>
</template>

<script>
export default {
  name: 'header'
}
</script>

<style lang="scss">
  .searchbar-wrapper{
    width: 15%;
    font-size: 2em
  }
</style>
