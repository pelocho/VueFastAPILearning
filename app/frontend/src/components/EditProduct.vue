<template>
  <div>
    <div class="container mt-20">
      <div class="card">
        <div class="card-header">
          <h3>Edit Product</h3>
        </div>
        <div class="card-body">
          <form v-on:submit.prevent="EditProduct">
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
              <input type="submit" class="btn btn-success" value="Edit Product"/>
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
                product: []
            };
        },
        created: function () {
            this.GetProduct();
        },
        methods: {
            EditProduct() {
                let url = 'http://localhost:8000/products/' + this.$route.params.id;
                this.axios.put(url, this.product)
                    .then(response => {
                        console.log(response.data);
                        this.$router.replace({name: 'home'})
                    })
            },
            GetProduct(){
                this.axios.get('http://localhost:8000/products/'+ this.$route.params.id)
                    .then(response => (this.product = response.data))
            }
        }
    }
</script>