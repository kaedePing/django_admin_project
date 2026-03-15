<template>
  <!--  <nav>-->
  <!--    <router-link to="/">Home</router-link> |-->
  <!--    <router-link to="/about">About</router-link>-->
  <!--  </nav>-->
  <router-view/>
</template>

<script setup>
import { watch } from 'vue'
import { useRoute } from 'vue-router'
import store from '@/store'

const route = useRoute()

watch(route, (to, from) => {
  console.log(to.name, to.path)
  if (to.name === '个人中心') { // 注意：这里通常路径应该是 '/personal' 这类，'个人中心' 更像 name 或标题
    let obj = {
      name: to.name,
      path: to.path
    }
    store.commit('ADD_TABS', obj)
  }
}, { deep: true, immediate: true })
</script>

<style>
html, body, #app {
  height: 100%;
}

.app-container {
  padding: 20px;
}
</style>
