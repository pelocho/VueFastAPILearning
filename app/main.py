from fastapi import FastAPI

app = FastAPI()


@app.get("/products/")
async def get_all_products():
    """
    Get all the products on sale
    """
    fake_products = [
        {
            'product_name': 'White table',
            'price': 250,
            'seller': 'Pepe'
        },
        {
            'product_name': 'Desktop chair',
            'price': 200,
            'seller': 'Paco'
        },
        {
            'product_name': '4k Monitor',
            'price': 300,
            'seller': 'Manolo'
        }
    ]
    return fake_products
