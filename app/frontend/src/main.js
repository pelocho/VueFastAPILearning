import Vue from 'vue'
import VueRouter from 'vue-router'
import VueAxios from 'vue-axios'
import axios from 'axios'
import NProgress from 'nprogress'

import Home from './components/products.vue'
import App from './home'

import 'bootstrap/dist/css/bootstrap.css'
import '../public/common.css'

Vue.use(VueRouter);
Vue.use(VueAxios, axios);

Vue.config.productionTip = false;

const routes = [
    {
        name: 'home',
        path: '/',
        component: Home
    }
];

const router = new VueRouter({mode: 'history', routes: routes});

router.beforeResolve((to, from, next) =>{
    if (to.name) {
        NProgress.start();
    }
    next();
});

router.afterEach(() => {
    NProgress.done();
});

new Vue({
    render: h => h(App),
    router
}).$mount('#products-region');