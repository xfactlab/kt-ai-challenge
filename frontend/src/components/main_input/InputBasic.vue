<template>
<div class="input-basic">
  <h1 class="input-title">주제 : 설명가능 하고, 개인맞춤 가능한 멀티 홉 질의응답</h1>
  <h2>질문</h2>
  <el-tooltip :content="basic_info" placement="top" effect="light">
    <i class="el-icon-info"></i>
  </el-tooltip>
  <el-input class="input-form" placeholder="질문을 입력하세요" v-model="question">
    <template slot="prepend">Q </template>
  </el-input>
  <h3>추론 옵션</h3>
    <el-checkbox v-model="stqa">Ko-StrategyQA</el-checkbox>
    <el-checkbox v-model="cot">Zeroshot CoT</el-checkbox>
    <el-checkbox v-model="kb">외부지식을 활용한 질의응답</el-checkbox>
    
  <el-divider></el-divider> 
  <h2>용어 설명</h2>
    <el-tooltip :content="def_info" placement="top" effect="light">
      <i class="el-icon-info"></i>
    </el-tooltip>
    <div class="definition">
      <el-input class="input-form" placeholder="질문을 입력하세요" v-model="definition">
        <template slot="prepend">용어설명</template>
      </el-input>
    </div>
  <h2>사실 목록</h2>
    <el-tooltip :content="fact_info" placement="top" effect="light">
      <i class="el-icon-info"></i>
    </el-tooltip>

      <el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="120px" class="demo-dynamic" label-position="left">
        <el-form-item
          v-for="(domain, index) in dynamicValidateForm.domains"
          :label="'사실목록 ' + index"
          :key="domain.key"
          :prop="'domains.' + index + '.value'"
          :rules="{
            required: false, message: 'domain can not be null', trigger: 'blur'
          }"
        >
        <el-input v-model="domain.value"></el-input><el-button @click.prevent="removeDomain(domain)">지우기</el-button>
        </el-form-item>
        <el-form-item>
          <!-- <el-button type="primary" @click="submitForm('dynamicValidateForm')">Submit</el-button> -->
          <el-button @click="addDomain">+ 새 사실목록</el-button>
        </el-form-item>
      </el-form>
  <el-divider></el-divider>
  <h2>외부 지식을 활용한 질의 응답</h2>
    <el-tooltip :content="kb_info" placement="top" effect="light">
      <i class="el-icon-info"></i>
    </el-tooltip>
    <el-upload
      class="upload-demo"
      drag
      action="https://jsonplaceholder.typicode.com/posts/"
      accept="txt"
      :file-list="fileList"
      :on-success="readTxt"
      >
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">Drop file here or <em>click to upload</em></div>
      <div class="el-upload__tip" slot="tip">only txt files allowed</div>
    </el-upload>
  
  <div class="sub">
    <el-button type="primary" :loading=loading @click="doSubmit()"> 결과 확인하기(inference)</el-button>
  </div>

  <el-divider></el-divider>
  <h2>결과 </h2>
  <div class="result-section">
    {{result}}
  </div>

</div>
</template>
<script>
import Api from '@/api/api'

export default {
  data(){
    return {
      cot : false,
      kb : false,
      stqa : false,
      result:"추론을 진행해주세요",
      checked : false,
      question : "",
      definition : "",
      content : "",
      textFile : null,
      dynamicValidateForm: {
        domains: []
      },
      fileList: [],
      reqText : "",
      basic_info : "모델에게 물어보고 싶은 질문을 입력합니다.",
      def_info : "질문에 포함된 모델에게 추가하고 싶은 개념을 다음 템플릿에 맞추어 입력합니다 => [용어] : [설명]",
      fact_info : "질문이 멀티 홉 형태일 경우 관련된 사실 추가가 모델 추론에 도움이 될 수 있습니다.",
      kb_info : "모델에 학습되지 않은 지식들을 prompt에 첨부해 모델의 설명력을 이용, 답을 추론할 수 있습니다.\n 추가적으로 믿:음 모델의 Embedding Vector를 활용할 수 있게 되면 \
      외부 Vector Database들을 이용해 외부 지식들을 저장하고 이를 활용할 수 있습니다. 여기에서는 Plain Text Chunks들을 가지고 질의응답을 진행해보겠습니다."
    }
  },
  methods : {
    addDomain(){
      this.dynamicValidateForm.domains.push({
        key : Date.now(),
        value : ''
      });
    },
    removeDomain(item){
      var index = this.dynamicValidateForm.domains.indexOf(item);
      if(index !== -1){
        this.dynamicValidateForm.domains.splice(index, 1);
      }
    },
    readTxt(res, file){

      var doc = file.raw
      const reader = new FileReader();
      reader.readAsText(doc)
      reader.onload = () => {
        this.content = reader.result;
        this.textFile = null;
      }

    },
    makePrompt(){
      let q = this.question
      let def = this.definition
      let prompt =  `질문 : ${q}. `
      // console.log(this.content)
      // console.log(this.content.split("\n"))
      // console.log(this.content.split("\n").toString())
      if(this.kb){
        prompt += "아래 문장목록들을 읽고 '질문'에 가장 알맞는 답변을 선택하세요. 그리고 문장목록에서 답변의 근거가 되는 문장을 출력하세요. "
        prompt +=  "문장목록 : "
        prompt += this.content.split("\n").toString()
      }else{
        if(def != ""){
          prompt += `용어설명 : ${def} `
          }
        if(this.dynamicValidateForm.domains.length != 0){
          let getValues = (objects, property) => objects.map(obj => obj[property]);
          let facts = getValues(this.dynamicValidateForm.domains, 'value');
          prompt += `사실목록 : [${facts}].`
        }
        if(this.stqa){
          prompt += "용어설명과 사실목록을 바탕으로 질문의 답변으로 사실 또는 거짓 둘 중 하나를 선택하세요. "
        }
        if(this.cot){
          prompt += "단계별로 차근차근 생각해서 답변을 선택하세요. "
        }

        prompt += "답변 :"
      }
      
      console.log(prompt)
      return prompt
    },
    doSubmit(){
      this.loading = true
      let prompt = this.makePrompt()
      let bodyData = {
        "serviceInstanceId" : "dd4citvg",
        "nluType" : "009",
        "apiType" : "002",
        "utterance" : prompt,
      }
      this.result = "답변 기다리는중....."
      Api.sendData(bodyData)
      .then((res)=>{
        this.loading = false
          this.$notify({
            title: '성공',
            message: `모델로 부터 응답이 도착했습니다.`,
            type: 'success'
          });
        let result = res.data.data[0]["result"][0]
        this.result = result
      })
      .catch((err)=>{
        this.loading = false
        this.$notify({
          title: '실폐',
          message: `서버 전송에 실패 하였습니다.`,
          type: 'failure'
        });
      this.result= "서버 전송에 실패 하였습니다."
      })
    },
  },
  mounted(){
  }
}
</script>

<style lang="scss">
.input-title{
  text-align: center;
}
.input-basic{
  margin : 0 0 20px 0;
  h2{
    display : inline-block;
  }
  i{
    margin : 0 5px;
  }
  .upload-demo{
    text-align: center;
  }
}
.sub{
  display:flex;
  justify-content: flex-end;
}
.result-section{
  border-radius : 15px;
  background-color : #e4edf2;
  min-height : 100px;
  padding : 10px;
  font-weight:bold;
}
.el-divider{
  margin : 8px 0 !important;
}
</style>