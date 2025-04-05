from fastapi import FastAPI

from api.routes import claims
from database.session import Base, engine


app = FastAPI(title="Insurance Claims Application")

Base.metadata.create_all(bind=engine)

app.include_router(claims.router, prefix='/api')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port="8000")