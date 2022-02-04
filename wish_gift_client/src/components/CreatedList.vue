<template>
  <div class="created">
    <div>{{ createdList.owner }} you wished for:</div>
    <p>{{ createdList.listItem }}</p>
  </div>
</template>

<script>
export default {
  name: 'CreatedList',
  props: ['createdList']
}
</script>

<style>
.created {
  text-align: center;
}
p {
  font-family: 'Caveat';
  font-size: 18px;
}
</style>