<template>
  <div>
    <button type="button" v-on:click="GoToHome" class="btn btn-outline-dark mb-20">X</button>
    <h3 class="flex-container-center">Edit Product</h3>
    <form v-on:submit.prevent="EditProduct">
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
        <input type="submit" class="btn button-color" value="Edit Product"/>
      </div>
    </form>
  </div>
</template>

<script>
    import store from "../store";

    export default {
        data() {
            return {
                product: []
            };
        },
        beforeRouteEnter(routeTo, routeFrom, next) {
            if (store.state.sidebarOpen === false) {
                store.commit('SHOW_SIDEBAR');
                next()
            } else {
                next()
            }
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
                        this.$router.push({path: '/'});
                    })
            },
            GetProduct() {
                this.axios.get('http://localhost:8000/products/' + this.$route.params.id)
                    .then(response => (this.product = response.data))
            },
            GoToHome() {
                this.$store.commit('SHOW_SIDEBAR');
                this.$router.push({path: '/'});
            }
        }
    }
</script>