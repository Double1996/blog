<template>
  <div id="app">
    <div id="main">
      <app-header></app-header>
      <transition name="router-fade">
        <router-view/>
      </transition>
    </div>
  </div>
</template>

<script>
  import AppHeader from './components/header'
  import AppFooter from './components/footer'

  export default {
    name: 'app',
    components: {
      AppHeader,
      AppFooter
    }
  }
</script>

<style lang="scss">
  @import "style/minireset";
</style>
