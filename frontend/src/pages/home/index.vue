<template>
  <div class="main">
    <el-row>
      <el-col :span="16">
      </el-col>
      <el-col :span="6">
      </el-col>
    </el-row>
  </div>
</template>


<script>
  import PageView from '../../components/pageView'

  export default {
    data () {
      return {
        filters: {
          name: ''
        },
        companies: [],
        total: 0,
        page: 1,
        listLoading: false
      }
    },
    components: {
      PageView
    },
    methods: {
    },
    created () {
    }
  }
</script>

<style lang="scss" scoped>
  .main {
    padding-left: 120px;
  }
  .df-companyList {
    padding: 30px;
    .box {
      -webkit-border-radius: 5px;
      border-radius: 5px;
      -moz-border-radius: 5px;
      background-clip: padding-box;
      margin: 20px auto;
      padding: 35px 0px 35px 0px;
      background: #fff;
      border: 1px solid #eaeaea;
      box-shadow: 0 0 25px #cac6c6;
      span {
        padding-left: 20px;
      }
    }
  }

</style>
