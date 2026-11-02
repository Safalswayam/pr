from fastapi import FastAPI
app = FastAPI(title="MyHello World", description="Demo")

@app.get("/")
def hello_world():
    return("message", "hello, world!")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)

