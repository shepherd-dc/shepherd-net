const article = {
  state: {
    article: {
      content: ''
    }
  },
  mutations: {
    FetchArticle: (state, payload) => {
      console.log(payload.content)
      state.article.content = payload.content
    }
  }
}

export default article
