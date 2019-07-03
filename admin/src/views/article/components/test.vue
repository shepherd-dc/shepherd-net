<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules" class="form-container">

      <div class="createPost-main-container">
        <el-row>

          <el-col :span="24">
            <el-form-item style="margin-bottom: 40px;" prop="title">
              <MDinput v-model="postForm.title" :maxlength="100" name="name" required>
                标题
              </MDinput>
            </el-form-item>

            <div class="postInfo-container">
              <el-row>
                <el-col :span="8">
                  <el-form-item label="版块栏目:">
                    <el-select
                      v-model="postForm.column_id"
                      placeholder="请选择栏目"
                      clearable>
                      <el-option-group
                        v-for="group in menus"
                        :key="group.id"
                        :label="group.menu_name">
                        <el-option
                          v-for="item in group.submenu"
                          :key="item.id"
                          :label="item.name"
                          :value="item.id"/>
                      </el-option-group>
                    </el-select>
                  </el-form-item>
                </el-col>
                <el-col :span="8">
                  <span class="author">作者：</span>
                  <el-autocomplete
                    v-model="postForm.author"
                    :fetch-suggestions="querySearchAsync"
                    placeholder="请输入作者"
                    @select="handleSelect"
                  />
                </el-col>

                <el-col :span="8">
                  <el-form-item label-width="80px" label="发布时间:" class="postInfo-container-item">
                    <el-date-picker v-model="postForm.create_time" type="datetime" format="yyyy-MM-dd HH:mm:ss" value-format="yyyy-MM-dd HH:mm:ss" placeholder="选择日期时间"/>
                  </el-form-item>
                </el-col>

                <!-- <el-col :span="6">
                  <el-form-item label-width="60px" label="推荐:" class="postInfo-container-item">
                    <el-rate
                      v-model="postForm.importance"
                      :max="5"
                      :colors="['#99A9BF', '#F7BA2A', '#FF9900']"
                      :low-threshold="1"
                      :high-threshold="3"
                      style="margin-top:8px;"/>
                  </el-form-item>
                </el-col> -->
              </el-row>
            </div>
          </el-col>
        </el-row>

        <!-- <el-form-item style="margin-bottom: 40px;" label-width="45px" label="摘要:">
          <el-input :rows="3" v-model="postForm.content_short" type="textarea" class="article-textarea" autosize placeholder="请输入内容"/>
          <span v-show="contentShortLength" class="word-counter">{{ contentShortLength }}字</span>
        </el-form-item> -->

        <el-form-item class="quill-editor" prop="content">
          <quill-editor :is-edit="isEdit" @deliverContent="handleContent"/>
        </el-form-item>

        <!-- <el-form-item prop="image_uri" style="margin-bottom: 30px;">
          <Upload v-model="postForm.image_uri" />
        </el-form-item> -->
        <el-form-item>
          <el-button
            type="success"
            @click="submitForm">发表</el-button>
          <el-button @click="resetForm">重置</el-button>
        </el-form-item>
      </div>
    </el-form>

  </div>
</template>

<script>
import QuillEditor from '@/components/Quilleditor/QuillEditor'
import MDinput from '@/components/MDinput'
import { fetchMenu } from '@/api/menu'
import { fetchArticle, createArticle, editArticle } from '@/api/article'
import { fetchUserList } from '@/api/user'

const defaultForm = {
  status: 'draft',
  title: '',
  column_id: undefined,
  author: '',
  author_id: undefined,
  user_id: undefined,
  create_time: undefined,
  content: '',
  id: undefined
}

export default {
  name: 'ArticleDetail',
  components: { QuillEditor, MDinput },
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    const validateRequire = (rule, value, callback) => {
      if (value === '') {
        this.$message({
          message: rule.field + '为必传项',
          type: 'error'
        })
        callback(new Error(rule.field + '为必传项'))
      } else {
        callback()
      }
    }
    return {
      postForm: Object.assign({}, defaultForm),
      loading: false,
      userListOptions: [],
      state: '',
      listQuery: {
        page: 1,
        limit: 20,
        kw: ''
      },
      rules: {
        title: [{ validator: validateRequire }],
        content: [{ validator: validateRequire }]
      },
      tempRoute: {},
      menus: []
    }
  },
  computed: {
    // contentShortLength() {
    //   return this.postForm.content_short.length
    // }
    // article_content() {
    //   return this.$store.getters.content
    // }
  },
  watch: {
    postForm() {
      return this.postForm
    }
  },
  created() {
    if (this.isEdit) {
      const id = this.$route.params && this.$route.params.id
      this.fetchData(id)
    } else {
      this.postForm = Object.assign({}, defaultForm)
    }

    var test = localStorage.getItem('menus')
    if (!test) {
      this.fetchMenu()
    }
    this.menus = JSON.parse(test)

    // Why need to make a copy of this.$route here?
    // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
    // https://github.com/PanJiaChen/vue-element-admin/issues/1221
    // this.tempRoute = Object.assign({}, this.$route)
  },
  mounted() {
    // console.log(this.article_content)
  },
  methods: {
    async fetchMenu() {
      const { data } = await fetchMenu('nav')
      localStorage.setItem('menus', JSON.stringify(data))
      this.menus = data
    },
    async fetchData(id) {
      const response = await fetchArticle(id)
      this.postForm = response.data
      this.$store.commit('FetchArticle', this.postForm)

      // Just for test
      // this.postForm.title += `   Article Id:${this.postForm.id}`
      // this.postForm.content_short += `   Article Id:${this.postForm.id}`

      // Set tagsview title
      // this.setTagsViewTitle()
    },
    // setTagsViewTitle() {
    //   const title = this.lang === 'zh' ? '编辑文章' : 'Edit Article'
    //   const route = Object.assign({}, this.tempRoute, { title: `${title}-${this.postForm.id}` })
    //   this.$store.dispatch('updateVisitedView', route)
    // },
    submitForm() {
      // this.postForm.create_time = parseInt(this.create_time / 1000)
      this.$refs.postForm.validate(async(valid) => {
        if (valid) {
          this.loading = true
          // console.log(this.postForm)
          if (this.postForm.id) {
            var data = await editArticle(this.postForm)
          } else {
            data = await createArticle(this.postForm)
          }

          // console.log(this.postForm)
          if (data.error_code === 0) {
            this.$notify({
              title: '成功',
              message: '操作成功',
              type: 'success',
              duration: 2000
            })
            // this.postForm.status = 'published'
            this.loading = false
            this.$router.replace({
              path: `/article/index`
            })
          }
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm() {
      this.postForm = {}
    },
    draftForm() {
      // if (this.postForm.title.length === 0) {
      //   this.$message({
      //     message: '请填写必要的标题和内容',
      //     type: 'warning'
      //   })
      //   return
      // }
      // this.$message({
      //   message: '保存成功',
      //   type: 'success',
      //   showClose: true,
      //   duration: 1000
      // })
      // this.postForm.status = 'draft'
    },
    async querySearchAsync(queryString, cb) {
      this.listQuery.kw = queryString
      const listQuery = Object.assign({}, this.listQuery)
      const data = await fetchUserList(listQuery)
      const userListOptions = []
      if (data.error_code === 0) {
        data.data.map((v) => {
          userListOptions.push(
            Object.assign({}, v, { value: v.nickname })
          )
        })
      }
      var results = queryString ? userListOptions.filter(this.createStateFilter(queryString)) : userListOptions

      cb(results)
    },
    createStateFilter(queryString) {
      return (state) => {
        return (state.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0)
      }
    },
    handleSelect(item) {
      // console.log(item)
      this.postForm.author = item.value
      if (item.id) {
        this.postForm.author_id = item.id
      }
    },
    handleContent(html) {
      // console.log(html)
      this.postForm.content = html
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
@import "~@/styles/mixin.scss";
.createPost-container {
  position: relative;
  .createPost-main-container {
    padding: 0 45px 20px 50px;
    .postInfo-container {
      position: relative;
      @include clearfix;
      margin-bottom: 10px;
      .postInfo-container-item {
        float: left;
      }
    }
  }
  .word-counter {
    width: 40px;
    position: absolute;
    right: -10px;
    top: 0px;
  }

  .author {
    color:#606266;
    font-size: 14px;
    font-weight: 700;
    font-family: "Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB, Microsoft YaHei, Arial, sans-serif";
  }
}
</style>

