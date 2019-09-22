<template>
  <ul>
    <li v-for="stepper in stepperList" :key="stepper.id" @click="updateStepperId(stepper.id)">
      <a>
        <span :class="{ 'is-myblue': isThisStepperActive(stepper.id) }">{{ stepper.name }}</span>
      </a>
    </li>
  </ul>
</template>

<script>
export default {
  props: {
    activeStepperId: {
      default: 1,
      type: Number
    }
  },

  data() {
    return {
      stepperList: [
        {
          id: 1,
          name: '1. Overview'
        },
        {
          id: 2,
          name: '2. Theory'
        },
        {
          id: 3,
          name: '3. Application'
        }
      ]
    }
  },
  methods: {
    isThisStepperActive(stepperId) {
      if (stepperId === this.activeStepperId) return true
      return false
    },
    updateStepperId(newId) {
      this.$emit('update-stepperId', newId)
    }
  }
}
</script>

<style lang="scss" scoped>
.is-myblue {
  // background-color: rgb(228, 240, 245);
  color: rgb(20, 20, 138);
  // background-image: $gradient;
}
</style>
