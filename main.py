from fastapi import FastAPI
from app import routes

app = FastAPI()

# يمكن إضافة المزيد من الـ routes لاحقًا
app.include_router(routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
