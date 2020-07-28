<template>
  <div>
    <div class="container mt-20">
      <div class="card">
        <div class="card-header">
          <h3>New Product</h3>
        </div>
        <div class="card-body">
          <form v-on:submit.prevent="CreateProduct">
            <div class="form-group">
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
              <label class="mr-20">Status:</label>
              <select v-model="product.status">
                <option value="New">New</option>
                <option value="Semi-new">Semi-new</option>
                <option value="Bad">Bad</option>
              </select>
            </div>
            <div class="form-group">
              <input type="submit" class="btn btn-success" value="Create Product"/>
            </div>
          </form>
        </div>
      </div>
    </div>
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
                    this.$router.replace({name: 'home'})
                })
            }
        }
    }
</script>

<style scoped>

</style>