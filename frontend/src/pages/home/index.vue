<template>
  <div class="main">
    <el-row>
      <el-col :span="16">
        <div class="df-companyList">
          <h1><el-tag type='success'>最近更新企业信息</el-tag></h1>
          <div class="box" v-for="(company, index) in companies" :key="index">
            <div class="main">
              <router-link class='' :to="{ path: company.companyView }">{{ company.company_name }}</router-link>
              <div class="meta">
                <div>
                  电子邮箱:<span>{{ company.company_email }}</span>
                </div>
                <div>
                  企业地址:<span>{{ company.business_address }}</span>
                </div>
                 <div>
                  注册时间:<span>{{ company.approval_date }}</span>
                </div>
                 <div>
                  法人代表:<span>{{ company.legal_representative }}</span>
                </div>
                <div v-if="company.avatar">
                  <img :src="company.avatar" alt="avatar" class="avatar">
                </div>
              </div>
            </div>
          </div>
          <page-view></page-view>
        </div>
      </el-col>
      <el-col :span="6">
        <h3><i class="fa fa-users"></i>爬虫任务列表</h3>
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
