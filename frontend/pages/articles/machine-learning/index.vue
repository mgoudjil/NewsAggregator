<template>
  <div style="margin-top:2vh">
    <div style="width: 90%;max-width: 1240px;margin: 0 auto;margin-bottom:15px">
      <span class="title is-3 text-center" style="margin-bottom:5px">Machine Learning</span>
      <p class="text-center" style="width:80%;margin:0 auto">
        “The future is ours to shape. I feel we are in a race that we need to win.
        It’s a race between the growing power of the technology and the growing
        wisdom we need to manage it.” Max Tegmark
      </p>
    </div>
    <div class="band">
      <div v-for="article in $options.articles.slice(0,1)" :key="article.id" :class="'item-1'">
        <nuxt-link :to="'/articles/' + article.link" class="card" no-prefetch>
          <div class="thumb" :style="' background-image: url(' + article.pictureUrl + ');'"></div>
          <article>
            <span style="position:relative;  margin: 0 0 0 0;">
              {{
              article.date
              }}
            </span>
            <h1>{{ article.title }}</h1>
            <p>{{ article.description }}</p>
            <span>{{ article.categoryName }}</span>
          </article>
        </nuxt-link>
      </div>

      <div v-for="article in $options.articles.slice(1,)" :key="article.id" :class="'item-2'">
        <nuxt-link :to="'/articles/' + article.link" class="card" no-prefetch>
          <div class="thumb" :style="' background-image: url(' + article.pictureUrl + ');'"></div>
          <article>
            <span style="position:relative;  margin: 0 0 0 0;">
              {{
              article.date
              }}
            </span>
            <h1>{{ article.title }}</h1>
            <p>{{ article.description }}</p>
            <span>{{ article.categoryName }}</span>
          </article>
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
import articles from '~/static/articles.js'

const articles_filtered = articles.filter(
  object => object.categoryName.toLowerCase() == 'machine learning'
)
export default {
  // validate({ params }) {
  //   // Must be a number
  //   return false // /^\d+$/.test(params.id)
  // },
  articles: articles_filtered.reverse(),
  component: {},
  data() {
    return {}
  },
  computed: {
    // articles() {
    //   let list = this.articlesBrut // All articles
    //   if (this.$store.state.activeCategoryId != null) {
    //     list = this.articlesBrut.filter(
    //       v => v.categoryId === this.$store.state.activeCategoryId
    //     )
    //   }
    //   return list
    // }
  }
}
</script>

<style scoped>
/* html {
  background: #f5f7f8;
  font-family: 'Roboto', sans-serif;
  -webkit-font-smoothing: antialiased;
  padding: 20px 0;
} */

.band {
  width: 90%;
  max-width: 1240px;
  margin: 0 auto;

  display: grid;

  grid-template-columns: 1fr;
  grid-template-rows: auto;
  grid-gap: 20px;
}

@media only screen and (min-width: 500px) {
  .band {
    grid-template-columns: 1fr 1fr;
  }
  .item-1 {
    grid-column: 1 / span 2;
  }
  .item-1 h1 {
    font-size: 26px;
  }
  .item-2 h1 {
    font-size: 22px;
  }
}

@media only screen and (min-width: 850px) {
  .band {
    grid-template-columns: 1fr 1fr 1fr 1fr;
  }
}

/* card */

.card {
  min-height: 100%;
  background: white;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: #444;
  position: relative;
  top: 0;
  transition: all 0.1s ease-in;
}

.card:hover {
  top: -2px;
  box-shadow: 0 4px 5px rgba(0, 0, 0, 0.2);
}

.card article {
  padding: 20px;
  display: flex;

  flex: 1;
  justify-content: space-between;
  flex-direction: column;
}
.card .thumb {
  padding-bottom: 60%;
  background-size: cover;
  background-position: center center;
}

.card p {
  flex: 1; /* make p grow to fill available space*/
  margin-top: 10px;
  line-height: 1.5;
  font-size: 13px;
}

/* typography */
h1 {
  font-size: 18px;
  font-weight: 500;
  margin: 0;

  /* color: #333; */
}

.card span {
  font-size: 12px;
  font-weight: bold;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin: 2em 0 0 0;
}
</style>