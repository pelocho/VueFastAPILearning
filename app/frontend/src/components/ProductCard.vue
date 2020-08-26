<template>
  <router-link class="product-link" :to="{name: 'edit-product', params: {id: product.id_}}">
    <div class="product-card shadow">
      <div class="row ml-5">
        <h4 class="mr-20">Name:</h4>
        <h4>{{ product.name }}</h4>
      </div>
      <div class="row ml-5">
        <h5 class="mr-20">Status:</h5>
        <h5>{{ product.status }}</h5>
      </div>
      <div class="row ml-5">
        <h5 class="mr-20">Price:</h5>
        <h5>{{ product.price }}</h5>
      </div>
      <div class="row ml-5">
        <h5 class="mr-20">Location:</h5>
        <h5>{{ product.location }}</h5>
      </div>
      <button class="btn btn-danger mt-20 ml-5" v-on:click="deleteProduct(product.id_)">Delete</button>
    </div>
  </router-link>
</template>

<script>
    export default {
        name: "ProductCard",
        props: {
            product: Object
        },
        methods: {
            deleteProduct(id) {
                let url = `http://localhost:8000/products/${id}`;
                this.axios.delete(url)
                    .then(this.$router.go());
            }
        }
    }
</script>

<style scoped>
  .product-card {
    padding: 20px;
    margin-bottom: 24px;
    transition: all 0.2s linear;
    cursor: pointer;
    width: 500px;
  }

  .product-card:hover {
    transform: scale(1.01);
    box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2), 0 1px 15px 0 rgba(0, 0, 0, 0.19);
  }

  .product-link {
    color: black;
    text-decoration: none;
    font-weight: 100;
  }
</style>