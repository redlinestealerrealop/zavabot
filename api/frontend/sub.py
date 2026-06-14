from pathlib import Path
import asyncio


async def start_bot_backend():
    TARGET_DIR = Path(__file__).resolve().parent.parent
    backend = await asyncio.create_subprocess_exec(
        "uv", "run", "uvicorn", "main:backend", "--port", "8000",
        cwd=TARGET_DIR,
        stderr=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE
    )

    await asyncio.sleep(2)

    if backend.returncode is not None:
        print(f"backend exited early with code {backend.returncode}")
        stderr = await backend.stderr.read()
        print(f"stderr: {stderr.decode()}")
        return

    print("backend started")

    async def read_stream(stream, label):
        while True:
            line = await stream.readline()
            if not line:
                break
            print(f"[{label}] {line.decode().rstrip()}")

    await asyncio.gather(
        read_stream(backend.stdout, "out"),
        read_stream(backend.stderr, "err"),
    )


if __name__ == "__main__":
    asyncio.run(start_bot_backend())