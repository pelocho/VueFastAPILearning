<template>
  <div class="col-lg-12">
    <div class="row mt-20 flex-container-center">
      <router-link :to="{name: 'create-product'}" class="btn btn-success">New Product</router-link>
    </div>
    <div class="row mt-20 flex-container-center">
      <div class="card mr-20" v-for="product in products" :key="product.id_">
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
          <router-link :to="{name: 'edit-product', params: {id: product.id_}}" class="btn btn-success">Edit Product</router-link>
          <button class="btn btn-danger ml-20" v-on:click="deleteProduct(product.id_)">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        data() {
            return {
                products: []
            };
        },
        created: function() {
            this.getProducts();
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
            }
        }
    };
</script>
