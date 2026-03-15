<template>
  <div class="button-example">

      <el-button type="primary" @click="handlelogin">测试登录</el-button>
      <el-button type="success" @click="handleuserlist">测试获取用户信息列表</el-button>

  </div>
</template>

<script  setup>
import request from "@/util/request";

const handlelogin=async ()=>{
  let result=await request.get("user/jwt_test")
  let data=result.data;
  if(data.code==200){
    const token=data.token;
    console.log("登录成功，token="+token)
    window.sessionStorage.setItem("token",token)
  }else{
    console.log("登录出错")
  }

}

const handleuserlist=async ()=>{
  let result=await request.get("user/test")
  let data=result.data;
  if(data.code==200){
    console.log("获取成功，data="+data.data)
  }else{
    console.log("获取失败")
  }
}


</script>

<style scoped>
.button-example {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.button-row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: center;
}

.button-row > * {
  margin: 0;
}
</style>
