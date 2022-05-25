from unittest import result
from fastapi import Body, FastAPI
from pydantic import BaseModel

class Numbers(BaseModel):
    fst_no: int
    sec_no: int
    sum:int
app = FastAPI()
@app.post("/add")
async def add(fst_no,sec_no):
    sum=fst_no+sec_no
    return sum
 
 