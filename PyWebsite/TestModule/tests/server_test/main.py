from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import time
import uvicorn

app = FastAPI()

html = Jinja2Templates('./')
database = []
@app.get('/', response_class=HTMLResponse)
async def main_page():
    return html.TemplateResponse(name='test.html', request={"request": Request})

@app.post('/database')
async def database_page(text: str=Form(...)):
    database.append({"text": text})
    return "Thanks!"

# if __name__ == 'main':
    # uvicorn.run()
# 
# for i in range(10):
    # print(database)
    # time.sleep(5)