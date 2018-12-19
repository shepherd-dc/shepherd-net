<template>
  <div class="login">
    <el-row>
      <el-col
        :span="width > 1080 ? 6 : 24"
        :offset="width > 1080 ? 9 : 0">
        <el-card class="box-card">
          <div
            slot="header"
            class="clearfix login-head">
            <span>注册</span>
          </div>
          <div class="text item">
            <el-form
              ref="ruleForm2"
              :model="ruleForm2"
              :rules="rules2"
              status-icon
              label-width="100px"
              class="demo-ruleForm">
              <el-form-item
                label="用户名"
                prop="user">
                <el-input v-model="ruleForm2.user"></el-input>
              </el-form-item>
              <el-form-item
                label="密码"
                prop="pass">
                <el-input
                  v-model="ruleForm2.pass"
                  type="password"
                  autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item
                label="确认密码"
                prop="checkPass">
                <el-input
                  v-model="ruleForm2.checkPass"
                  type="password"
                  autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button
                  type="success"
                  @click="submitForm('ruleForm2')">提交</el-button>
                <el-button @click="resetForm('ruleForm2')">重置</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>

      </el-col>
    </el-row>

  </div>
</template>

<script>
  export default {
    data() {
      var checkUser = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('用户名不能为空'));
        }
      }
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.ruleForm2.checkPass !== '') {
            this.$refs.ruleForm2.validateField('checkPass');
          }
          callback();
        }
      }
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.ruleForm2.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      }
      return {
        width: '',
        ruleForm2: {
          pass: '',
          checkPass: '',
          user: ''
        },
        rules2: {
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { validator: validatePass2, trigger: 'blur' }
          ],
          user: [
            { validator: checkUser, trigger: 'blur' }
          ]
        }
      }
    },
    watch: {
      width () {
        this.width = window.innerWidth
      }
    },
    mounted() {
      let width = window.innerWidth
      this.width = width
      // console.log(this.menus)
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>

<style lang="less" scoped>
  .login {
    padding-top: 60px;
    min-height: 92vh;
  }
  .box-card {
    margin-top: 60px;
    .login-head {
      font-size: 18px;
      font-weight: bold;
      text-align: center;
    }
  }
</style>
