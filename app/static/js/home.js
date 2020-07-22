new Vue({
    el: '#products-region',
    delimiters: ['[[', ']]'],
    data: {
        products: [{
            product_name: 'Product1',
            product_status: 'New',
            product_price: 150,
            product_picture: 'picture',
            product_location: 'Malaga'
        },{
            product_name: 'Product2',
            product_status: 'Semi-New',
            product_price: 50,
            product_picture: 'picture',
            product_location: 'Marbella'
        },{
            product_name: 'Product3',
            product_status: 'Bad',
            product_price: 250,
            product_picture: 'picture',
            product_location: 'Benalmadena'
        }]
    }
});