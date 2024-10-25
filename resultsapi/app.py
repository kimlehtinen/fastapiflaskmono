from fastapi import FastAPI
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()
executor = ThreadPoolExecutor()

def blocking_task():
    import time
    time.sleep(5)
    return "Task completed"

@app.get("/")
def root():
    future = executor.submit(blocking_task)
    result = future.result()
    return {"message": result}
