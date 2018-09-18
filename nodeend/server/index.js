const Koa = require('koa')
const views = require('koa-views')
const static = require('koa-static') 
const { resolve } = require('path')
const { connect } = require('./database/init')

const app = new Koa()

app.use(views(resolve(__dirname, './views'), {
    extension: 'ejs'
}))

app.use(static(resolve(__dirname, './static')))

app.use(async (ctx, next) => {
    await ctx.render('index', {
        msg: 'Hello world!~'
    })
})

;(async () => {
  await connect()
})()

app.listen(5566)
