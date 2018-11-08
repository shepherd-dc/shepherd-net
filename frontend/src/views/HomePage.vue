<template>
  <div>
    <h1>Demos</h1>
    <button class="btn btn-success">按钮</button>
    <p v-for="(item, index) in tasks" :key="index">{{item.title}}</p>
  </div>
</template>
<script>
import { get } from '../utils/http'
export default {
  metaInfo: {
    title: 'Shepherd network'
  },
  data () {
    return {
      tasks: []
    }
  },
  created () {
    get('https://shepherdnet.top/api/test').then(data => {
      // console.log(data)
      this.tasks = data.tasks
    }).catch(err => {
      console.log(err)
    })
  },
  mounted () {
  }
}
</script>
