<template>
  <div class="previous">
    <div>and</div>
    <p>{{ previousList.owner }} wished for {{ previousList.listItem }} </p>
  </div>
</template>

<script>
export default {
  name: 'PreviousList',
  props: ['previousList']
}
</script>

<style>
.previous {
  text-align: center;
}

</style>