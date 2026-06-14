import aiohttp



async def send_backend(zavati, execid, execuser, timefound):
   backend_url = "http://127.0.0.1:8000"
   backend_body = {
      "username_command": str(execuser),
      "uid_command": str(execid),
      "uid": zavati,
      "uid_time_found": str(int(timefound.timestamp()))
   }

   async with aiohttp.ClientSession() as session:
      async with session.post(f"{backend_url}/v2/register", json=backend_body) as resp:
         response = await resp.json()

         return response

