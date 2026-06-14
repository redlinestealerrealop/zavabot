from fastapi import FastAPI
import pathlib
import json
from fastapi.responses import (
    JSONResponse,
)
import aiofiles
from pydantic import BaseModel

backend = FastAPI()
path = pathlib.Path()

class Register(BaseModel):
    username_command: str # userexec
    uid_command: str # execid
    uid_time_found: str # timefound
    uid: int # zavati


@backend.post("/v2/register")
async def register_zavati_time(data: Register):
    reg_dict = data.model_dump()

    await handle_file(reg_dict)
    return JSONResponse(
        status_code=200,
        content={
            "message": "logged count of zavati sucessfully",
            "code": 200,
            "req_data": [
                reg_dict
            ]
        }
    )



async def handle_file(json_response):
    json_path = path.cwd() / "Zavati" / "zavati.json"
    json_path.parent.mkdir(parents=True, exist_ok=True)

    if json_path.exists():
        async with aiofiles.open(json_path, mode="r") as f:
            content = await f.read()
        if content:
            loaded = json.loads(content)
            data = loaded if isinstance(loaded, list) else [loaded]
        else:
            data = []
    else:
        data = []

    data.append(json_response)

    async with aiofiles.open(json_path, mode="w") as f:
        await f.write(json.dumps(data, indent=2))
    