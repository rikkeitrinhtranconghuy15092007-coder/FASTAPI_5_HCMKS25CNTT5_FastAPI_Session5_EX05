from fastapi import FastAPI, HTTPException, Path, status

app = FastAPI()

products = [
    {"id": 1, "code": "SP001", "name": "Keyboard", "price": 500000, "is_active": True},
    {"id": 2, "code": "SP002", "name": "Mouse", "price": 300000, "is_active": True},
    {"id": 3, "code": "SP003", "name": "Monitor", "price": 2500000, "is_active": False}
]


@app.get("/products")
def get_products():
    return products


@app.delete("/products/{product_id}")
def deactivate_product(product_id: int = Path(..., description="ID của sản phẩm cần ngừng kinh doanh")):
    for item in products:
        if item["id"] == product_id:
            if not item["is_active"]:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Product already inactive"
                )
            
            item["is_active"] = False
            return {
                "message": "Ngừng kinh doanh sản phẩm thành công",
                "product": item
            }
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Product not found"
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)