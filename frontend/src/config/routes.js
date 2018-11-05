export default [
    {
      path: '/',
      redirect: '/app'
    },
    {
      // path: '/app/:id', // /app/xxx
      path: '/app',
      props: true,
      // props: (route) => ({ id: route.query.b }),
      component: () => import('../views/HomePage.vue'),
      // component: Todo,
      name: 'app',
      meta: {
        title: 'this is app',
        description: 'asdasd'
      },
      beforeEnter (to, from, next) {
        console.log('app route before enter')
        next()
      }
      // children: [
      //   {
      //     path: 'test',
      //     component: Login
      //   }
      // ]
    }
    // {
    //   path: '/login',
    //   component: () => import(/* webpackChunkName: "login-view" */ '../views/login/login.vue')
    //   // component: Login
    // }
  ]
  