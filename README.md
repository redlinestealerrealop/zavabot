## Announcer, Account Manager, and Session Manager for Zavati Script Loader.



Zavati Script Loader is a Script Loader for Minecraft and other games. This is its discord bot, that has the backend, the commands, and the user frontend logic (Discord).





## Files

`botutils/utils.py` - Utilities for the bot to communicate with the Backend

`api/` - All API logic.

`api/Zavati` - Backend API test JSON dumps (currently only the relationship handshake check rn) 

`api/frontend` - The subprocess starter, and more API frontend logic to come.





## How to run

If you are on Windows, Linux, or Android, you will need uv (from astral.sh). To install it, there will be a couple different methods:



**Windows**

`winget astral-sh.uv`

OR

`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex`



**Linux**

`curl -LsSf https://astral.sh/uv/install.sh | sh`

OR by using your package manager


**Termux/Android**

`apt install rust uv`

OR

`cargo install uv`



While this is a pretty small bot, i plan to add more features over the summer. It will take a while, so you can watch commits in #bot-updates or you can watch my github.

