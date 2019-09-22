<template>
  <div id="app">
    <nav class="header__nav">
      <ul class="header__navbar">
        <li class="header__item">
          <a href="#" class="header__link">
            <transition name="slide-fade">
              <button v-if="show" key="on" class="header--btn" @click="show = false">
                <svg viewBox="0 0 24 24" class="header--icon">
                  <title>Close</title>
                  <path
                    d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"
                  />
                </svg>
              </button>
              <button v-else key="off" class="header--btn" @click="show = true">
                <svg viewBox="0 0 24 24" class="header--icon">
                  <title>Navigation Menu</title>
                  <path
                    d="M4 8h4V4H4v4zm6 12h4v-4h-4v4zm-6 0h4v-4H4v4zm0-6h4v-4H4v4zm6 0h4v-4h-4v4zm6-10v4h4V4h-4zm-6 4h4V4h-4v4zm6 6h4v-4h-4v4zm0 6h4v-4h-4v4z"
                  />
                </svg>
              </button>
            </transition>
          </a>
          <transition name="dropdown">
            <div v-if="show" class="header__dropdown-menu" :class="{ active: show }">
              <ul class="header__dropdown-menu-nav">
                <li @click="show = false" class="header__dropdown-menu-item">
                  <nuxt-link to="/" class="header__dropdown-menu-link" title="Account">
                    <div class="header__dropdown-menu-text">RESEARCH</div>
                  </nuxt-link>
                </li>
                <hr />
                <li @click="show = false" class="header__dropdown-menu-item">
                  <nuxt-link
                    to="/articles"
                    href="#"
                    class="header__dropdown-menu-link"
                    title="Personal info"
                  >
                    <div class="header__dropdown-menu-text">ARTICLES</div>
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </transition>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
// https://codepen.io/berikidis/pen/dweNVp
export default {
  data() {
    return {
      show: false
    }
  }
}
</script>

<style lang="scss" scoped>
ul {
  margin: 0;
  padding: 0;
}

h1 {
  margin: 0;
}
li {
  list-style: none;
}
a {
  text-decoration: none;
}

hr {
  border: 0;
  height: 0;
  margin: 2rem 0;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

.header {
  padding: 2rem 5rem 2rem 5rem;
  &__nav {
    position: relative;
  }
  &__navbar {
    display: flex;
    align-items: center;
    flex-direction: row;
    justify-content: flex-end;
  }
  &__item {
    padding: 1rem;
    position: relative;
  }
  &__link {
    .header--icon {
      color: gray;
    }
    .header--btn {
      top: 0;
      right: 0;
      position: absolute;
      &:focus {
        outline: 0;
      }
    }
  }
  &--icon {
    fill: currentcolor;
    width: 1.65rem;
    height: 1.65rem;
    display: inline-flex;
  }
  &--btn {
    cursor: pointer;
    padding: 0;
    display: inline-block;
    border: 1px solid transparent;
    background-color: transparent;
    appearance: none;
    user-select: none;
  }
  &__dropdown-menu {
    position: absolute;
    top: 100%;
    right: 0;
    height: 11rem;
    min-width: 80px;
    overflow-y: auto;
    padding: 2rem 0 0 0;
    margin-top: 1rem;
    border-radius: 8px;
    background-color: white;
    border: 1px solid #dadce0;
    background-clip: padding-box;
  }
  &__dropdown-menu-link {
    display: flex;
    align-items: center;
    flex-direction: row;
    justify-content: flex-start;
    line-height: 0;
    color: #3c4043;
    padding: 0.6rem 1.5rem 0.6rem 1.5rem;
    margin-bottom: 0.4rem;
    border-radius: 0 50px 50px 0;
    &:hover {
      background-color: rgba(0, 0, 0, 0.039);
    }
  }
  &__dropdown-menu-svg {
    padding-right: 16px;
    .header--icon {
      width: 1.4rem;
      height: 1.4rem;
    }
  }
}

// Animation slide button
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.6s;
}
.slide-fade-enter,
.slide-fade-leave-active {
  opacity: 0;
}
.slide-fade-enter {
  transform: translateX(31px);
}
.slide-fade-leave-active {
  transform: translateX(-31px);
}

// Dropdown animation
.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 1s;
}
.dropdown-enter,
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(30px);
}

.wrapper {
  height: 70vh;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  .social {
    margin-top: 1rem;
  }
  a {
    padding: 0.6rem;
  }
  h1 {
    color: #42b983;
    font-size: 2rem;
    font-weight: 300;
  }
  p {
    color: #7f8c8d;
    font-weight: 100;
  }
  svg {
    fill: currentcolor;
    color: #b8c2cc;
    width: 1.65rem;
    height: 1.65rem;
    display: inline-flex;
  }
}
</style>
