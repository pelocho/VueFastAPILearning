new Vue({
    el: '#products-region',
    delimiters: ['[[', ']]'],
    data() {
        return {
            products: null
        }
    },
    mounted() {
        axios.get('/products')
            .then(response => (this.products = response.data))
    }
});