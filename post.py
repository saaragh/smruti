from fastapi import Body, FastAPI
app = FastAPI()
@app.post("/add")
def add(x,y):
    sum = int (x) + int(y) 
    return sum
 
 