from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    from_: str
    to: str
    date: str

@app.post("/query")
async def query_train(data: QueryRequest):
    # 这里只是模拟返回，你可以接入真正的 MCP Python 库
    return {
        "from": data.from,
        "to": data.to,
        "date": data.date,
        "trains": [
            {"no": "G123", "price": 450, "duration": "5h30m"},
            {"no": "G456", "price": 520, "duration": "4h55m"}
        ]
    }
