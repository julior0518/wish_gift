<template>
  <div>
    <div>Created List Placeholder</div>
    <p>{{ createdList.owner }}</p>
    <p>{{ createdList.listItem }}</p>
  </div>
</template>

<script>
export default {
  name: 'CreatedList',
  props: ['createdList']
}
</script>
