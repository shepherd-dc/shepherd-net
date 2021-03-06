<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.title" placeholder="标题" style="width: 226px;" class="filter-item" @keyup.enter.native="handleFilter"/>
      <el-select ref="menu" v-model="listQuery.menu_id" placeholder="主栏目" clearable class="filter-item" style="width: 216px" @change="handleFilter">
        <el-option v-for="item in menuOptions" :key="item.id" :label="item.menu_name" :value="item.id"/>
      </el-select>
      <el-select v-model="listQuery.column_id" placeholder="子栏目" clearable class="filter-item" style="width: 216px" @change="handleFilter">
        <el-option-group v-for="group in menuOptions" :key="group.id" :label="group.menu_name">
          <el-option v-for="item in group.submenu" :key="item.id" :label="item.name" :value="item.id+'-'+item.path"/>
        </el-option-group>
      </el-select>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">搜索</el-button>
    </div>

    <el-table
      v-loading="listLoading"
      :key="tableKey"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      @sort-change="sortChange">
      <el-table-column label="ID" prop="id" sortable="custom" align="center" width="65">
        <template slot-scope="scope">
          <span>{{ scope.row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="时间" prop="time" sortable="custom" width="160px" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.create_time }}</span>
        </template>
      </el-table-column>
      <el-table-column label="主栏目" width="110px" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.menu_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="子栏目" width="110px" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.column_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="标题">
        <template slot-scope="scope">
          <span>{{ scope.row.title }}</span>
        </template>
      </el-table-column>
      <el-table-column label="作者" width="110px" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.author }}</span>
        </template>
      </el-table-column>
      <el-table-column label="推荐" class-name="status-col" width="110px" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.recommend | statusFilter">{{ scope.row.status === 1 ? '是' : '否' }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center" width="230" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button type="primary" size="mini" @click="handleUpdate(scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="70px" style="width: 80%; margin-left:50px;">
        <el-form-item label="主菜单" prop="menu_id">
          <el-select v-model="temp.menu_id" class="filter-item" placeholder="Please select" style="width: 100%;">
            <el-option v-for="item in menuOptions" :key="item.id" :label="item.menu_name" :value="item.id"/>
          </el-select>
        </el-form-item>
        <el-form-item label="栏目名" prop="name">
        <el-input v-model="temp.name"/></el-form-item>
        <el-form-item label="官网" prop="official_doc">
          <el-input v-model="temp.official_doc"/>
        </el-form-item>
        <el-form-item label="简介" prop="description">
          <el-input :autosize="{ minRows: 2, maxRows: 10}" v-model="temp.description" type="textarea"/>
        </el-form-item>
        <el-form-item label="图片">
          <el-upload
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :file-list="fileList2"
            class="upload-demo"
            action="https://jsonplaceholder.typicode.com/posts/"
            list-type="picture">
            <el-button size="small" type="primary">点击上传</el-button>
          </el-upload>
        </el-form-item>
        <el-form-item label="路由">
          <el-input v-model="temp.path" :disabled="true"/>
        </el-form-item>
        <el-form-item label="状态">
          <el-select v-model="temp.status" class="filter-item" placeholder="Please select">
            <el-option v-for="item in statusOptions" :key="item" :label="item===1?'启用':'禁用'" :value="item"/>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">确定</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
import { fetchList } from '@/api/article'
import { menuList } from '@/api/column'
import waves from '@/directive/waves' // Waves directive
import Pagination from '@/components/Pagination' // Secondary package based on el-pagination

export default {
  name: 'ComplexTable',
  components: { Pagination },
  directives: { waves },
  filters: {
    statusFilter(status) {
      const statusMap = {
        1: 'success',
        0: 'danger'
      }
      return statusMap[status]
    }
    // typeFilter(type) {
    //   return calendarTypeKeyValue[type]
    // }
  },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 5,
        menu_id: undefined,
        column_id: undefined,
        title: undefined,
        order: 1
      },
      menuOptions: [],
      importanceOptions: [1, 2, 3],
      statusOptions: [1, 0],
      temp: {
        id: undefined,
        menu_id: '',
        name: '',
        description: '',
        official_doc: '',
        pic: '',
        path: '',
        status: 1
      },
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
      rules: {
        menu_id: [{ required: true, message: '请选择主菜单', trigger: 'change' }],
        name: [{ required: true, message: '请输入栏目名', trigger: 'blur' }],
        description: [{ required: true, message: 'title is required', trigger: 'blur' }],
        official_doc: [{ required: true, message: 'title is required', trigger: 'blur' }],
        pic: [{ required: true, message: 'title is required', trigger: 'blur' }]
      },
      downloadLoading: false,
      fileList2: [{ name: 'food.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100' }]

    }
  },
  async created() {
    await this.getMenu()
    await this.getList()
  },
  methods: {
    async getList() {
      this.listLoading = true
      const { data } = await fetchList(this.listQuery)
      this.list = data.data
      this.total = data.total
      this.listLoading = false
      // // Just to simulate the time of the request
      // setTimeout(() => {
      //   this.listLoading = false
      // }, 1.5 * 1000)
    },
    async getMenu() {
      this.listLoading = true
      const { data } = await menuList()
      this.menuOptions = data
      this.listLoading = false
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    sortChange(data) {
      const { prop, order } = data
      if (prop === 'id' || prop === 'time') {
        this.sortByID(order)
      }
    },
    sortByID(order) {
      if (order === 'ascending') {
        this.listQuery.order = 0
      } else {
        this.listQuery.order = 1
      }
      this.handleFilter()
    },
    resetTemp() {
      this.temp = {
        id: undefined,
        menu_id: '',
        name: '',
        description: '',
        official_doc: '',
        pic: '',
        path: '',
        status: 1
      }
    },
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    // createData() {
    //   this.$refs['dataForm'].validate(async(valid) => {
    //     if (valid) {
    //       this.temp.pic = '/card.jpg'
    //       const { data } = await saveSubmenu(this.temp)
    //       this.temp = data
    //       this.list.unshift(this.temp)
    //       this.dialogFormVisible = false
    //       this.$notify({
    //         title: '成功',
    //         message: '创建成功',
    //         type: 'success',
    //         duration: 2000
    //       })
    //     }
    //   })
    // },
    // async setPath() {
    //   if (this.temp.menu_id) {
    //     const { data } = await menuDetail({ id: this.temp.menu_id })
    //     this.temp.path = `${data.en_name}/${this.temp.name}`
    //   }
    // },
    // handleUpdate(row) {
    //   this.temp = Object.assign({}, row) // copy obj
    //   this.dialogStatus = 'update'
    //   this.dialogFormVisible = true
    //   this.$nextTick(() => {
    //     this.$refs['dataForm'].clearValidate()
    //   })
    // },
    // updateData() {
    //   this.$refs['dataForm'].validate((valid) => {
    //     if (valid) {
    //       const tempData = Object.assign({}, this.temp)
    //       saveSubmenu(tempData).then(() => {
    //         for (const v of this.list) {
    //           if (v.id === this.temp.id) {
    //             const index = this.list.indexOf(v)
    //             this.list.splice(index, 1, this.temp)
    //             break
    //           }
    //         }
    //         this.dialogFormVisible = false
    //         this.$notify({
    //           title: '成功',
    //           message: '更新成功',
    //           type: 'success',
    //           duration: 2000
    //         })
    //       })
    //     }
    //   })
    // },
    // async handleDelete(row) {
    //   await deleteSubmenu({ id: row.id })
    //   this.$notify({
    //     title: '成功',
    //     message: '删除成功',
    //     type: 'success',
    //     duration: 2000
    //   })
    //   const index = this.list.indexOf(row)
    //   this.list.splice(index, 1)
    // },
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePreview(file) {
      console.log(file)
    }
  }
}
</script>

<style>
  .filter-container {
    margin-bottom: 20px;
  }
</style>
