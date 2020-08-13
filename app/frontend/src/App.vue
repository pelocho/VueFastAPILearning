<template>
  <div>
    <div class="mt-20 flex-container-center">
      <router-link :to="{name: 'create-product'}" v-on:click.native.prevent="showSidebar" class="btn btn-success">New Product</router-link>
    </div>
    <div class="mt-20 flex-container ml-20">
          <div class="card mr-20 align-start" v-for="product in products" :key="product.id_">
            <div class="card-header">
              {{ product.name }}
            </div>
            <div class="card-body">
              <h5 class="card-title">Status: </h5>
              <p class="card-text">{{ product.status }}</p>
              <h5 class="card-title">Price: </h5>
              <p class="card-text">{{ product.price }}</p>
              <h5 class="card-title">Location: </h5>
              <p class="card-text">{{ product.location }}</p>
              <hr>
              <router-link :to="{name: 'edit-product', params: {id: product.id_}}" v-on:click.native.prevent="showSidebar" class="btn btn-success">Edit
                Product
              </router-link>
              <button class="btn btn-danger ml-20" v-on:click="deleteProduct(product.id_)">Delete</button>
            </div>
        </div>
      <Sidebar v-if="this.showPanel">
        <router-view></router-view>
      </Sidebar>
    </div>
  </div>
</template>

<script>
    import Sidebar from './components/Sidebar.vue';

    export default {
        components: {Sidebar},
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
