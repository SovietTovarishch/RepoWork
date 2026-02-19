from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/products", tags=["products"])

products = [
    {
        "name": "Корм для собак",
        "category": "Food",
        "price": 102,
        "animal": "dog"
    },
    {
        "name": "Корм для котов",
        "category": "Food",
        "price": 91,
        "animal": "cat"
    },
    {
        "name": "Жевательная кость",
        "category": "Toys",
        "price": 298,
        "animal": "dog"
    },
    {
        "name": "Шампунь от блох",
        "category": "Hygiene",
        "price": 165,
        "animal": "dog"
    },
    {
        "name": "Ошейник",
        "category": "Accessories",
        "price": 100,
        "animal": "dog"
    },
    {
        "name": "Аквариум",
        "category": "Essentials",
        "price": 120,
        "animal": "aquatic"
    },
    {
        "name": "Клетка для птиц",
        "category": "Essentials",
        "price": 150,
        "animal": "bird"
    }
]

# Получить список всех продуктов
@router.get("/default")
async def get_products(sorting: str = None):
    products_list = products.copy()

    # Применяем сортировку, если указан параметр
    if sorting:
        if sorting.lower() == "asc":
            products_list.sort(key=lambda x: x["name"].lower())
        elif sorting.lower() == "desc":
            products_list.sort(key=lambda x: x["name"].lower(), reverse=True)
        else:
            raise HTTPException(
                status_code=400,
                detail="Параметр sorting должен быть 'asc' или 'desc'"
            )

    return {
        "products": products_list,
        "total": len(products_list),
        "sorting": sorting if sorting else "not applied"
    }
@router.get("/animal/{animal}")
async def get_products_for_animal(animal):
    filtered_products = []
    for product in products:
        if(product.get("animal") == animal):
            filtered_products.append(product)

    return {
        "products": filtered_products,
        "total": len(filtered_products)
    }