<template>
  <div>
    <form v-on:submit="handleSubmit">
      <input 
        @input="handleChange"
        placeholder="Name"
        :value="name"
        type="text"
        name="name"
      />
      <input 
        @input="handleChange"
        placeholder="Gift"
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
