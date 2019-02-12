<template>
  <div class="app-container">

    <el-table v-loading="listLoading" :data="list" border fit highlight-current-row style="width: 100%">

      <el-table-column align="center" label="ID" width="80">
        <template slot-scope="scope">
          <span>{{ scope.row.id }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="英文名">
        <template slot-scope="scope">
          <span>{{ scope.row.en_name }}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="300px" label="菜单名">
        <template slot-scope="scope">
          <template v-if="!scope.row.status">
            <el-input v-model="scope.row.menu_name" class="edit-input" size="small"/>
            <el-button class="cancel-btn" size="small" icon="el-icon-refresh" type="warning" @click="cancelEdit(scope.row)">取消</el-button>
          </template>
          <span v-else>{{ scope.row.menu_name }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="操作" width="200">
        <template slot-scope="scope">
          <el-button v-if="!scope.row.status" type="success" size="small" icon="el-icon-circle-check-outline" @click="confirmEdit(scope.row)">确定</el-button>
          <el-button v-else type="primary" size="small" icon="el-icon-edit" @click="scope.row.status=!scope.row.status">编辑</el-button>
          <el-button size="mini" type="danger" icon="el-icon-delete" @click="handleDelete(scope.row)">删除</el-button>
        </template>
      </el-table-column>

    </el-table>

    <el-button size="small" icon="el-icon-plus" type="success" class="add-btn" @click="handleCreate">添加</el-button>

    <el-dialog :visible.sync="dialogFormVisible" title="添加菜单">
      <el-form ref="dataForm" :model="form" :rules="rules">
        <el-form-item :label-width="formLabelWidth" label="菜单名称" prop="menu_name" style="width:96%">
          <el-input v-model="form.menu_name"/>
        </el-form-item>
        <el-form-item :label-width="formLabelWidth" label="英文名称" prop="en_name" style="width:96%">
          <el-input v-model="form.en_name"/>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer" style="width:96%">
        <el-button @click="resetForm">重 置</el-button>
        <el-button type="primary" @click="createData">确 定</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
import { menuList, addMenu, editMenu, deleteMenu } from '@/api/column'

export default {
  name: 'InlineEditTablemenu',
  data() {
    return {
      list: null,
      listLoading: false,
      listQuery: {
        page: 1,
        limit: 10
      },
      dialogFormVisible: false,
      form: {
        menu_name: '',
        en_name: ''
      },
      formLabelWidth: '100px',
      rules: {
        menu_name: [{ required: true, message: '请输入菜单名称', trigger: 'blur' }],
        en_name: [{ required: true, message: '请输入英文名称', trigger: 'blur' }]
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    async getList() {
      this.listLoading = true
      const { data } = await menuList()
      this.list = data
      this.listLoading = false
    },
    cancelEdit(row) {
      row.status = 1
      this.$message({
        message: '取消修改',
        type: 'warning'
      })
    },
    async confirmEdit(row) {
      const data = await editMenu({
        id: row.id,
        menu_name: row.menu_name
      })
      if (data.error_code === 0) {
        row.status = 1
        this.$message({
          message: '修改成功',
          type: 'success'
        })
      }
    },
    handleCreate() {
      this.resetTemp()
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs['dataForm'].validate(async(valid) => {
        if (valid) {
          const data = await addMenu(this.form)
          if (data.error_code === 0) {
            this.temp = data.data
            this.list.unshift(this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
          }
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetTemp() {
      this.form = {}
    },
    resetForm() {
      this.$refs['dataForm'].resetFields()
    },
    handleDelete(row) {
      this.$confirm('此操作将删除该菜单, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(async() => {
        await deleteMenu({ id: row.id })
        const index = this.list.indexOf(row)
        this.list.splice(index, 1)
        this.$notify({
          title: '成功',
          message: '删除成功',
          type: 'success',
          duration: 2000
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    }
  }
}
</script>

<style scoped>
.edit-input {
  padding-right: 100px;
}
.cancel-btn {
  position: absolute;
  right: 15px;
  top: 10px;
}
.add-btn {
  margin: 20px;
  float: right;

}
</style>
