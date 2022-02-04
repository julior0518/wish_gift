<template>
  <div>
    <div>Content Placeholder</div>
    <About/>
    <div v-if="!previousList && !createdList">
      <NewList
        :name='name'
        :listItem='listItem'
        @handleFormChange="handleFormChange"
        @handleSubmit="handleSubmit"
      />
    </div>
    <div v-else>
      <CreatedList/>
    <PreviousList/>
    </div>
    
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
  },
  data: () => ({
    previousList: null,
    createdList: null,
    name: '',
    listItem: ''
  }),
  methods: {
    handleFormChange(name, value) {
      this[name] = value
    },
    handleSubmit() {
      // TODO
      // api call here to assign previousList and createdList
      alert('Form Submitted')

      // TODO
      this.previousList = {placeholder: 'placeholder'}
      this.createdList = {placeholder: 'placeholder'}

    }
  }
}
</script>
