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
import axios from 'axios'
import { BASE_URL } from '../globals'
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
      this.handleAPICalls()

    },
    async handleAPICalls() {
      const allLists = await axios.get(`${BASE_URL}`)
      this.previousList = allLists.data[allLists.data.length - 1]
      const newList = await axios.get(`${BASE_URL}lists/new/${this.name}/${this.listItem}`)
      this.createdList = newList.data[newList.data.length - 1]
    }
  }
}
</script>
