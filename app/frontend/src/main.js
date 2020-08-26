import Vue from 'vue'
import VueRouter from 'vue-router'
import VueAxios from 'vue-axios'
import axios from 'axios'
import NProgress from 'nprogress'

import CreateProduct from './components/CreateProduct.vue'
import EditProduct from './components/EditProduct.vue'
import App from './App.vue'
import store from './store'

import 'bootstrap/dist/css/bootstrap.css'
import '../public/common.css'

Vue.use(VueRouter);
Vue.use(VueAxios, axios);

Vue.config.productionTip = false;

const routes = [
    {
        name: 'create-product',
        path: '/product/create',
        component: CreateProduct
    },
    {
        name: 'edit-product',
        path: '/product/edit/:id',
        component: EditProduct
    },
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
    store,
    router
}).$mount('#products-region');