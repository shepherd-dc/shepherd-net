<template>
  <div>
    <sub-list
      :column_data="column_data"
      :articles_data="articles_data"/>
  </div>
</template>
<script>
  import URL from '~/globalurl'
  import SubList from '~/components/SingleColumn'
  export default {
    components: {
      SubList
    },
    async asyncData ( context ) {
      let column = await context.$axios.get(`${URL}/menu/sublist/${context.params.item}`)
      let column_id = column.data.id
      let { data } = await context.$axios.get(`${URL}/article?column_id=${column_id}`)
      return {
        column_data: column.data,
        articles_data: data
      }
    }
  }
</script>
