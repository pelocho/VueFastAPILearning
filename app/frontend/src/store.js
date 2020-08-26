import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        sidevarOpen: true,
    },
    mutations: {
        SHOW_SIDEVAR(state) {
            state.sidevarOpen = !state.sidevarOpen
        }
    },
    actions: {},
    getters: {}
})

