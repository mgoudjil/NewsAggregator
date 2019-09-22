<template>
  <div>
    <!--
      1. div if Overview with html render
      2. div if Theory
      3. div if Application

    -->

    <div class="articleHeaderPicture"></div>

    <!-- Header -->
    <span
      class="box is has-text-centered dynamic-height"
      style="border-radius:1px;box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1)"
    >
      <h1 class="title is-1">Infinity Paradise</h1>
      <h1 class="headline is-3">
        We received applications from 119 countries, spanning 6 continents with
        projects ranging from environmental to humanitarian.
      </h1>
    </span>

    <!-- Stepper -->
    <div class="tabs is-centered is-toggle" style="margin-bottom:10px;">
      <ArticleStepper :active-stepper-id="activeStepperId" @update-stepperId="updateStepperId"></ArticleStepper>
    </div>
    <!--  -->
    <div style="max-width:1000px; margin-left: auto; margin-right: auto">
      <overview v-if="activeStepperId === 1"></overview>
      <theory v-else-if="activeStepperId === 2"></theory>
      <demonstrations v-else-if="activeStepperId === 3"></demonstrations>
      <applications v-else-if="activeStepperId === 4"></applications>
    </div>
  </div>
</template>

<script>
import ArticleStepper from '~/components/article/ArticleStepper.vue'

// Pages
import overview from './overview.vue'
import theory from './theory.vue'
import demonstrations from './demonstrations.vue'
import applications from './applications.vue'

export default {
  name: 'ArticleSlider',
  components: {
    ArticleStepper,
    overview,
    theory,
    demonstrations,
    applications
  },
  data() {
    return {
      activeStepperId: 1
    }
  },
  methods: {
    updateStepperId(newId) {
      this.activeStepperId = newId
    }
  }
}
</script>

<style lang="scss" scoped>
$url: 'https://images.unsplash.com/photo-1547809397-e2c7eea071fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80';
.articleHeaderPicture {
  height: 50vh;
  background: url($url) no-repeat center fixed;
}

.dynamic-height {
  -webkit-transform: translateY(-20%);
  transform: translateY(-20%);
  margin-bottom: 1vh;
  max-width: 40%;

  margin-left: auto;
  margin-right: auto;

  @media screen and (max-width: 768px) {
    max-width: 80%;
    margin-bottom: 1vh;
  }
  /* margin-bottom: -10vh; */
  /* margin-top: -50px; */
}
</style>
