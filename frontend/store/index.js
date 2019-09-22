export const state = () => ({
  activeCategoryId: null,
  categoriesList: [
    {
      id: 1,
      name: 'Artificial Intelligence'
    },
    {
      id: 2,
      name: 'Machine Learning'
    },
    {
      id: 3,
      name: 'Neuroscience'
    },
    {
      id: 4,
      name: 'Advanced Statistics'
    },
    {
      id: 5,
      name: 'Cryptographie'
    },
    {
      id: 6,
      name: 'Physics'
    }
  ]
})

export const getters = {
  getToken: (state) => {
    return state.token
  },
  getLocale: (state) => {
    return state.locale
  },
  getEmail: (state) => {
    return state.email
  },
  getPassword: (state) => {
    return state.password
  }
}

export const mutations = {
  SET_ACTIVE_CATEGORY(state, newValue) {
    state.activeCategoryId = newValue
  }
}

export const actions = {
  logout({ commit }) {
    commit('SET_USER', null)
    commit('SET_EMAIL', '')
    commit('SET_PASSWORD', '')
    this.$router.push({
      path: '/business/login'
    })
  }
}
