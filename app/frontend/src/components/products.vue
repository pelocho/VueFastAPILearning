<template>
  <div>
    <div class="card mr-20 ml-20" v-for="product in products" :key="product.id">
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
                this.axios.get('/products')
                    .then(response => (this.products = response.data))
            }
        }
    };
</script>
