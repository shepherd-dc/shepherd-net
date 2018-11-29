<template>
  <div class="header">
    <div class="logo">
      Shepherd Net
    </div>
    <nav>
      <li>My blog</li>
      <li>About us</li>
    </nav>
  </div>
</template>
<style lang="less" scoped>
  .header {
    background-color: #333;
    color:#fff;
    display:flex;
    .logo {
      padding:20px;
      border-right:1px #fff solid;
    }
    nav {
      flex:1;
      display: flex;
      justify-content: flex-end;
      li {
        padding: 20px;
      }
    }
  }
</style>

