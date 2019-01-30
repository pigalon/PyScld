<template>
  <div id="app" class="flyout">
    <mdb-navbar dark position="top" class="default-color" scrolling :scrollingOffset="20">
      <mdb-navbar-brand to="/" waves style="font-weight: bolder;">
        MDB Vue
      </mdb-navbar-brand>
      <mdb-navbar-toggler>
        <mdb-navbar-nav right>
          <mdb-nav-item exact to="/" waves-fixed>Home</mdb-nav-item>
          <mdb-nav-item to="/css" waves-fixed>CSS</mdb-nav-item>
          <mdb-nav-item to="/components" waves-fixed>Components</mdb-nav-item>
          <mdb-nav-item to="/advanced" waves-fixed>Advanced</mdb-nav-item>
          <mdb-nav-item to="/navigation" waves-fixed>Navigation</mdb-nav-item>
          <mdb-nav-item to="/forms" waves-fixed>Forms</mdb-nav-item>
          <mdb-nav-item to="/tables" waves-fixed>Tables</mdb-nav-item>
          <mdb-nav-item to="/modals" waves-fixed>Modals</mdb-nav-item>
          <mdb-nav-item to="/plugins" waves-fixed>Plugins & addons</mdb-nav-item>
        </mdb-navbar-nav>
      </mdb-navbar-toggler>
    </mdb-navbar>
    <main :style="{marginTop: '60px'}">
      <router-view></router-view>
    </main>
    <mdb-footer color="default-color">
      <p class="footer-copyright mb-0 py-3 text-center">
        &copy; {{new Date().getFullYear()}} Copyright: <a href="https://mdbootstrap.com/docs/vue/?utm_source=DemoApp&utm_medium=MDBVue"> MDBootstrap.com</a>
      </p>
    </mdb-footer>
  </div>
</template>



<script>

import { mdbNavbar, mdbNavItem, mdbNavbarNav, mdbNavbarToggler, mdbNavbarBrand, mdbFooter } from 'mdbvue';

export default {
  name: 'app',
  components: {
    mdbNavbar,
    mdbNavItem,
    mdbNavbarNav,
    mdbNavbarToggler,
    mdbNavbarBrand,
    mdbFooter
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 100px;
}
</style>
