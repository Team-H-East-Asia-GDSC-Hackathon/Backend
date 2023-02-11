import json

from fastapi import FastAPI, File, UploadFile, APIRouter
from fastapi.responses import FileResponse,Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
router = APIRouter()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def Hello():
    return {"Hello":"Vegan!"}

@app.get(path="/diet/info/")
async def get_info(date:str,time:str):
    f = open('menu.json', 'r')
    json_dict = json.load(f)
    for i in range(len(json_dict)):
        if str(date) == json_dict[i]['date']  and str(time) == json_dict[i]['time']:
            return json.dumps(json_dict[i])