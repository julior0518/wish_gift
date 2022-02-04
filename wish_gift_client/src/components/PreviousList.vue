<template>
  <div>
    <div>Previous List Placeholder</div>
    <p>{{ previousList.owner }}</p>
    <p>{{ previousList.listItem }}</p>
  </div>
</template>

<script>
export default {
  name: 'PreviousList',
  props: ['previousList']
}
</script>
