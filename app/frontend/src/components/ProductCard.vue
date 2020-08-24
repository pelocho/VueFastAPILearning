<template>
  <div class="product-card shadow">
    <div class="row ml-5">
      <h4 class="mr-20">Name:</h4>
      <slot name="name"></slot>
    </div>
    <div class="row ml-5">
      <h5 class="mr-20">Status</h5>
      <slot name="status"></slot>
    </div>
    <div class="row ml-5">
      <h5 class="mr-20">Price</h5>
      <slot name="price"></slot>
    </div>
    <div class="row ml-5">
      <h5 class="mr-20">Location</h5>
      <slot name="location"></slot>
    </div>
  </div>
</template>

<script>
    export default {
        name: "ProductCard"
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
</style>