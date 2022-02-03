<template>
  <div>
    <div>Content Placeholder</div>
    <About/>
    <NewList/>
    <CreatedList/>
    <PreviousList/>
  </div>
</template>

<script>
import About from '../components/About.vue'
import CreatedList from '../components/CreatedList.vue'
import NewList from '../components/NewList.vue'
import PreviousList from '../components/PreviousList.vue'

export default {
  name: 'Content',
  components: {
    About,
    CreatedList,
    NewList,
    PreviousList,
  }
}
</script>
