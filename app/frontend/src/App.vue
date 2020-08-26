<template>
  <div>
    <div class="mt-20 flex-container-center">
      <router-link :to="{name: 'create-product'}" v-on:click.native.prevent="showSidebar" class="btn btn-success">New
        Product
      </router-link>
    </div>
    <ProductCard v-for="product in products" :key="product.id_" :product="product" class="flex-container-center mt-20"
                 @click.native.prevent="showSidebar"></ProductCard>
    <Sidebar v-if="this.$store.state.sidevarOpen">
      <router-view></router-view>
    </Sidebar>
  </div>
</template>

<script>
    import Sidebar from './components/Sidebar.vue';
    import ProductCard from "./components/ProductCard";

    export default {
        components: {ProductCard, Sidebar},
        data() {
            return {
                products: [],
            };
        },
        created: function () {
            this.getProducts();
        },
        watch: {
          '$route': function () {
              this.getProducts();
              this.$store.state.sidevarOpen = false;
          }
        },
        methods: {
            getProducts() {
                this.axios.get('http://localhost:8000/products')
                    .then(response => (this.products = response.data))
            },
            showSidebar() {
                this.$store.commit('SHOW_SIDEVAR')
            }
        }
    };
</script>