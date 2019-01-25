<template>
  <div>
    <list
      :card_data="card_data"
      :articles_data="articles_data"/>
  </div>
</template>
<script>
  import list from '~/components/CommonList'
  import URL from "~/globalurl"
  export default {
    components: {
      list
    },
    async asyncData(context) {
      let menu = await context.$axios.get(`${URL}/menu/list/frontend`)
      let menu_id = menu.data.id
      let { data } = await context.$axios.get(`${URL}/article?menu_id=${menu_id}`)
      // console.log(data)
      return {
        card_data: menu.data,
        articles_data: data
      }
    }
  }
</script>
