<template>
  <div>
    <div class="sm:flex py-1 m-1 border border-gray-300 shadow-md rounded hover:shadow-xl">
      <div class style="flex-shrink-0 ;margin:auto 0; margin-right: 1vw;margin-left: 1vw">
        <div
          class="column is-hidden-mobile"
          style="display:flex;flex-direction:column;justify-content:center;align-items:center;"
        >
          <div style="max-width:50px" @click="changeVoteValue(1)">
            <img :src="imageArrowUp" />
          </div>
          <span class="mt-3 mb-3">2k3</span>
          <div style="max-width:50px" @click="changeVoteValue(-1)">
            <img :src="imageArrowDown" />
          </div>
        </div>
      </div>
      <!-- <div class="border-r-2 mr-2"></div> -->

      <div class="flex-shrink-0" style="margin: auto 0">
        <img
          class="rounded-lg sm:w-56"
          src="https://images.unsplash.com/photo-1545987796-200677ee1011?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80"
          alt="Woman paying for a purchase"
        />
      </div>
      <div class="mt-4 md:mt-0 ml-2">
        <div
          class="uppercase tracking-wide text-sm text-indigo-800 font-bold"
        >Artifical Intelligence</div>
        <a
          href="https://www.google.com"
          class="mt-1 text-md leading-tight font-semibold text-gray-900 hover:underline"
        >Finding customers for your new business</a>
        <p class="block mt-2 mr-1">
          Getting a new business off the ground is a lot of hard work. Here
          are five ideas you can use to find your first customers.
        </p>
        <div class="border-b-2 mt-1 mb-1 mr-2"></div>

        <div class="flex justify-between" style="max-width:300px">
          <span class="text-sm">12/09/12</span>
          <span class="text-sm">Youtube</span>
          <span class="text-sm">Alex</span>
        </div>
      </div>
    </div>
  </div>
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
      value: 0,
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

  computed: {
    // If Value 0 arrow is simple without color
    imageArrowUp() {
      let imageSrc = 'arrow-up.png'
      if (this.value === 1) imageSrc = 'arrow-up-color.png'
      return imageSrc
    },
    imageArrowDown() {
      let imageSrc = 'arrow-down.png'
      if (this.value === -1) imageSrc = 'arrow-down-color.png'
      return imageSrc
    }
  },
  methods: {
    // Change vote value, it will impact arrow colors
    changeVoteValue(value) {
      if (value === this.value) {
        this.value = 0
      } else {
        this.value = value
      }
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
