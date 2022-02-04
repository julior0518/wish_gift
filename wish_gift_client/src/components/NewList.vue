<template>
  <div >
    <form class="new" v-on:submit="handleSubmit">
      <input 
        @input="handleChange"
        placeholder="name"
        :value="name"
        type="text"
        name="name"
      />
      <input 
        @input="handleChange"
        placeholder="wish"
        :value="listItem"
        type="text"
        name="listItem"
      />
      <button :disabled="!name || !listItem">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'NewList',
  props: ['name', 'listItem'],
  methods: {
    handleChange(e) {
      this.$emit('handleFormChange', e.target.name, e.target.value)
    },
    handleSubmit(e) {
      e.preventDefault()
      this.$emit('handleSubmit')
    }
  }
}
</script>

<style>

.new {
  display: flex;
  flex-direction: column;
  width: 40%;

}
input {
  border: none;
  background: rgba(255, 0, 0, 0);
  padding: 10px 0;
}
input:hover {
  text-decoration: underline;
}

button {
  margin-top: 10px;
  width: 100px;
  border: none;
  font-size: 10;
  padding:4px 0;
  background-color: rgba(165, 42, 42, 0.185);
  border-radius: 25px;

}
button:hover {
  background-color: rgba(165, 42, 42, 0.329);

}
</style>