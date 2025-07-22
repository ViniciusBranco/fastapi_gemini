from fastapi import FastAPI

# 1. Cria uma instância da aplicação FastAPI
app = FastAPI()

# 2. Define um "path operation decorator"
@app.get("/")
# 3. Define a "path operation function"
async def root():
    return {"message": "Hello World"}