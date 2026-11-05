from fastapi import FastAPI

from ai_portfolio.router import user_router

app = FastAPI()

app.include_router(user_router.router)


@app.get("/test")
def read_root():
    return {"Hello": "Test World"}
