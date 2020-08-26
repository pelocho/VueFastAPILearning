<template>
  <div>
    <button type="button" v-on:click="GoToHome" class="btn btn-outline-dark mb-20">X</button>
    <h3 class="flex-container-center">New Product</h3>
    <form v-on:submit.prevent="CreateProduct">
      <div class="form-group mt-20">
        <label>Name:</label>
        <input type="text" class="form-control" v-model="product.name">
      </div>
      <div class="form-group">
        <label>Price:</label>
        <input type="text" class="form-control" v-model="product.price">
      </div>
      <div class="form-group">
        <label>Location:</label>
        <input type="text" class="form-control" v-model="product.location">
      </div>
      <div class="form-group">
        <label>Picture:</label>
        <input type="text" class="form-control" v-model="product.picture">
      </div>
      <div class="form-group">
        <label class="mr-20 mb-20">Status:</label>
        <select v-model="product.status">
          <option value="New">New</option>
          <option value="Semi-new">Semi-new</option>
          <option value="Bad">Bad</option>
        </select>
      </div>
      <div class="form-group mt-20 flex-container-center">
        <input type="submit" class="btn button-color" value="Create Product"/>
      </div>
    </form>
  </div>
</template>

<script>
    export default {
        data() {
            return {
                product: {}
            }
        },
        methods: {
            CreateProduct(){
                let url = 'http://localhost:8000/products';
                this.axios.post(url, this.product)
                .then(response => {
                    console.log(response.data);
                    this.$router.push({path: '/'});
                })
            },
            GoToHome() {
                this.$store.commit('SHOW_SIDEBAR');
                this.$router.push({path: '/'});
            }
        }
    }
</script>

<style scoped>

</style>