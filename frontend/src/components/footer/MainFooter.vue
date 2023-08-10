
<template>
  <el-row class="footer-conainter" :gutter="10">
    <el-col class="logo-link" :sm="24" :md="12" >
      <img class="footer-logoa" :src="require(`@/assets/title.png`)">
      <a href="https://github.com/xfactlab/kt-ai-challenge">
        <img class="icon" :src="require(`@/assets/github.png`)">
      </a>
    </el-col>
    <el-col class="name" :sm="24" :md="12">
      <div>Copyright 2023 xfact All rights reserved.</div>
      <div>[결선]2023 AI대학원 챌린지 with kt 믿:음 서비스 활용 Demo</div>
      <div>김상렬, 오필훈</div>
    </el-col>
</el-row>
</template>

<script>


export default {
  components : {

  },
  data(){
    return{

    }
  }

}
</script>

<style lang="scss">
.footer-container{

  background-color : #f4f6f8;
  border : 1px solid red;
}
.logo-link{
  display : flex;
  align-items: center;
}
.footer-logoa{
  width : 50px;
  margin-right : 10px;
}
.name{
  text-align:right;
}
.icon{
  width : 30px;
  height : 30px;
  margin-right : 10px;
}
</style>