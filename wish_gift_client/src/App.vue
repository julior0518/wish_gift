<template>
  <div id="app" class="app">
    <Content/>
  </div>
</template>

<script>
import Content from './pages/Content.vue'
export default {
  name: 'App',
  components: {
    Content,
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap');

#app {
  font-family: 'Permanent Marker', cursive;
  text-align: center;
  padding: 0;
  margin: 0;
  height: 100vh;
  color:rgb(100, 100, 100)
}

</style>
