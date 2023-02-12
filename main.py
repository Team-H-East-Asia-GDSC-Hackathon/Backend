import json
from fastapi import FastAPI,  HTTPException

app = FastAPI()

@app.get("/")
async def Hello():
    return {"Hello":"Vegan!"}

@app.post(path="/diet/info/", status_code=200)
async def get_info(date:str,time:str):
    f = open('menu.json', 'r')
    json_dict = json.load(f)
    for i in range(len(json_dict)):
        if str(date) == json_dict[i]['date']  and str(time) == json_dict[i]['time']:
            return json.dumps(json_dict[i])
        else:
            raise HTTPException(status_code=400, detail="Model not found.")