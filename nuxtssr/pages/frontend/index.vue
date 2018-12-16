<template>
  <div>
    <list :en_name="en_name"/>
  </div>
</template>
<script>
  import list from '~/components/CommonList'
  export default {
    components: {
      list
    },
    data () {
      return {
        en_name: 'frontend'
      }  
    }
  }
</script>
