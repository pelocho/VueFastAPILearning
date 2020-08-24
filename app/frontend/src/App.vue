<template>
  <div>
    <div class="mt-20 flex-container-center">
      <router-link :to="{name: 'create-product'}" v-on:click.native.prevent="showSidebar" class="btn btn-success">New Product</router-link>
    </div>
      <div v-for="product in products" :key="product.id_" class="flex-container-center mt-20">
        <router-link class="product-link" :to="{name: 'edit-product', params: {id: product.id_}}" v-on:click.native.prevent="showSidebar">
          <ProductCard>
            <h4 slot="name">{{ product.name }}</h4>
            <h5 slot="status">{{ product.status }}</h5>
            <h5 slot="price">{{ product.price }}</h5>
            <h5 slot="location">{{ product.location }}</h5>
          </ProductCard>
          <button class="btn btn-danger ml-20" v-on:click="deleteProduct(product.id_)">Delete</button>
        </router-link>
      </div>
      <Sidebar v-if="this.showPanel">
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
                showPanel: false
            };
        },
        created: function () {
            this.getProducts();
        },
        watch: {
          '$route': function () {
              this.getProducts();
              this.showPanel = false;
          }
        },
        methods: {
            getProducts() {
                this.axios.get('http://localhost:8000/products')
                    .then(response => (this.products = response.data))
            },
            deleteProduct(id) {
                let url = `http://localhost:8000/products/${id}`;
                this.axios.delete(url)
                    .then(this.$router.go());
            },
            showSidebar() {
                this.showPanel =  !this.showPanel
            }
        }
    };
</script>

<style scoped>
.product-link {
  color: black;
  text-decoration: none;
  font-weight: 100;
}
</style>