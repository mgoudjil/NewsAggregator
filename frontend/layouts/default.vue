<template>
  <div>
    <section class="shadow-md">
      <!-- Hero head: will stick at the top -->
      <nav class="navbar">
        <div class="container">
          <div class="navbar-brand" style="margin-left:-2vw">
            <nuxt-link to="/">
              <div class="w-1/2 p-4 btn btn-1">
                <svg class>
                  <rect x="0" y="0" fill="none" width="100%" height="100%" />
                </svg>
                DisruptKnowledge
              </div>
            </nuxt-link>

            <a class="dropdown-display">
              <DropdownMenu />
            </a>
          </div>
          <div id="navbarMenuHeroA" class="navbar-menu">
            <div class="navbar-end">
              <nuxt-link to="/" class="header__link p-4" style="color:grey">Research</nuxt-link>
              <nuxt-link to="/articles" class="header__link p-4" style="color:grey">Articles</nuxt-link>
            </div>
          </div>
        </div>
      </nav>
    </section>

    <nuxt />
  </div>
</template>

<script>
import DropdownMenu from '~/components/DropdownMenu.vue'

export default {
  components: {
    DropdownMenu
  }
}
</script>


<style lang="scss">
/* DROPDOWN */

.dropdown-display {
  display: none;

  @media screen and (max-width: 1023px) {
    display: block;

    // margin-right: 20px;
    margin-left: auto;

    margin-top: 15px;
    margin-bottom: auto;
  }
}

/* */
html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}

.header__link:hover {
  font-weight: 500;
  border-bottom: 2px solid rgb(34, 59, 206);
  padding-bottom: 10px;
}

.navbar {
  width: 90%;
  max-width: 1240px;
  margin: 0 auto;
  height: 56px;
}

.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}

.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}

.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}

.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}

/*/////////////////////////////
//button one 
/////////////////////////// */

//default button
.btn {
  color: rgb(10, 3, 49);
  cursor: pointer;
  letter-spacing: 1px;

  display: block;
  font-size: 16px;
  font-weight: 400;
  // line-height: 25px;
  margin: 0 0 0;
  max-width: 160px;
  position: relative;
  text-decoration: none;
  // text-transform: uppercase;
  height: 50px;
  width: 100%;

  //   @media(min-width: 400px) {
  //     display: inline-block;
  //     margin-right: 2.5em;

  //     &:nth-of-type(even) {
  //       margin-right: 0;
  //     }
  //   }

  @media (min-width: 600px) {
    margin: 0 1em 2em;

    //     &:nth-of-type(even) {
    //       margin-right: 2.5em;
    //     }

    //     &:nth-of-type(5) {
    //       margin-right: 0;
    //     }
  }

  &:hover {
    text-decoration: none;
  }
}

.btn-1 {
  // background: white;
  // font-weight: 100;

  svg {
    height: 50px;
    // left: 0;
    position: absolute;
    top: 0;
    width: 100%;
  }

  rect {
    fill: none;
    // stroke: rgb(38, 39, 85);
    stroke-width: 2;
    stroke-dasharray: 422, 220;
    transition: all 0.35s linear;
  }
}

.btn-1:hover {
  background: white;
  font-weight: 500;
  letter-spacing: 1px;

  rect {
    stroke: rgb(10, 12, 153);

    stroke-width: 3;
    stroke-dasharray: 15, 235;
    stroke-dashoffset: 50;
    transition: all 2.35s cubic-bezier(0.19, 1, 0.22, 1);
  }
}
</style>
