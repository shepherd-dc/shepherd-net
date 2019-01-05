<template>
  <div class="publish">
    <el-row>
      <el-col
        :span="width > 1080 ? 18 : 24"
        :offset="width > 1080 ? 3 : 0">
        <el-card class="box-card">
          <div
            slot="header"
            class="clearfix publish-head">
            <span>发表文章</span>
          </div>
          <div class="item-body">
            <el-form
              ref="form"
              :model="form"
              label-width="80px">
              <el-form-item label="活动名称">
                <el-input v-model="form.name"></el-input>
              </el-form-item>
              <el-form-item label="活动形式">
                <quill-editor/>
                <!-- <el-input
                  v-model="form.desc"
                  type="textarea"></el-input> -->
              </el-form-item>
              <el-form-item label="活动区域">
                <el-select
                  v-model="form.region"
                  placeholder="请选择活动区域">
                  <el-option
                    label="区域一"
                    value="shanghai"></el-option>
                  <el-option
                    label="区域二"
                    value="beijing"></el-option>
                </el-select>
              </el-form-item>

              <el-form-item label="活动性质">
                <el-checkbox-group v-model="form.type">
                  <el-checkbox
                    label="美食/餐厅线上活动"
                    name="type"></el-checkbox>
                  <el-checkbox
                    label="地推活动"
                    name="type"></el-checkbox>
                  <el-checkbox
                    label="线下主题活动"
                    name="type"></el-checkbox>
                  <el-checkbox
                    label="单纯品牌曝光"
                    name="type"></el-checkbox>
                </el-checkbox-group>
              </el-form-item>
              <el-form-item label="特殊资源">
                <el-radio-group v-model="form.resource">
                  <el-radio label="线上品牌商赞助"></el-radio>
                  <el-radio label="线下场地免费"></el-radio>
                </el-radio-group>
              </el-form-item>

              <el-form-item>
                <el-button
                  type="primary"
                  @click="onSubmit">立即创建</el-button>
                <el-button>取消</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-col>
    </el-row>

  </div>
</template>

<script>
  import URL from '~/globalurl'
  import QuillEditor from '~/components/QuillEditor'

  export default {
    components: {
      QuillEditor
    },
    data() {
      return {
        width: '',
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
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
      onSubmit() {
        console.log('submit!')
      }
    }
  }
</script>

<style lang="less" scoped>
  .publish {
    padding-top: 60px;
    min-height: 92vh;
  }
  .box-card {
    margin-top: 30px;
    .publish-head {
      font-size: 18px;
      font-weight: bold;
      text-align: center;
    }
    .item-body {
      padding-right: 30px;
    }
  }
</style>
