<template>
  <div>
    <h1>Demos</h1>
    <button class="btn btn-success">按钮</button>
    <p v-for="(item, index) in tasks" :key="index">{{item.title}}</p>
  </div>
</template>
<script>
// import { get } from '../utils/http'
export default {
  data () {
    return {
      tasks: []
    }
  },
  created () {
    // get('http://172.16.5.54:5050/api/test').then(data => {
    //   // console.log(data)
    //   this.tasks = data.tasks
    // }).catch(err => {
    //   console.log(err)
    // })
  },
  mounted () {
  }
}
</script>
