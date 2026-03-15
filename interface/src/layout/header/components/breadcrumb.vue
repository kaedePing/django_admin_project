<template>
  <el-icon>
    <HomeFilled/>
  </el-icon>
  <el-breadcrumb separator="/">
    <el-breadcrumb-item v-for="(item, index) in breadcrumbList" :key="index">
      <span>{{ item.name }}</span>
    </el-breadcrumb-item>
  </el-breadcrumb>
</template>


<script setup>
import { HomeFilled } from '@element-plus/icons-vue'
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const breadcrumbList = ref([])

const initBreadcrumbList = () => {
  breadcrumbList.value = route.matched
}

initBreadcrumbList()

import { watch } from 'vue'

// 监听路由变化
watch(route, () => {
  initBreadcrumbList()
}, { deep: true, immediate: true })

</script>

<style  scoped>

</style>