<template>
  <div id="content">
    <div class="margin">
        <h2 >Content Placeholder</h2>
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


<style>
#content {
  border: 1px solid rgb(126, 126, 126);
  position: absolute;
  left:24vw;
  top:10%;
  width:50vw;
  background-color: whitesmoke;
  box-shadow: 20px 20px 35px rgba(0, 0, 0, 0.671);
}
#content:hover {
  box-shadow: 10px 10px 25px rgba(0, 0, 0, 0.671);
  color: black
  ;
}
.margin{
  border-left: 2px solid rgba(194, 47, 47, 0.39);
  padding-top:60px;
  height: 100vh;
  text-align: left;
  margin: 0 80px;
  text-indent: 20px;

}



</style>
