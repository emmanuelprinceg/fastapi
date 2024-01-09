from typing import Union

from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_root():
    html_content="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fetch API Example</title>
</head>
<body>
<h1>Other 2 IP's</h1>
<div id="data-container1">INSTANCE B</div>
<div id="data-container2">INSTANCE C</div>


<script>
    document.addEventListener("DOMContentLoaded", fetchData1);

    function fetchData1() {
        // Replace 'your-api-endpoint' with the actual API endpoint URL
        fetch('http://18.60.55.247:8000/ip1/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                displayData1(data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    function displayData1(data) {
        var dataContainer = document.getElementById('data-container1');

        // Assuming the API response is an array of objects with a 'name' property
        data.forEach(item => {
            var paragraph = document.createElement('p');
            paragraph.textContent = item.client_host1;
            dataContainer.appendChild(paragraph);
        });
    }

   
document.addEventListener("DOMContentLoaded", fetchData2);

    function fetchData2() {
        // Replace 'your-api-endpoint' with the actual API endpoint URL
        fetch('http://18.61.0.200:8000/ip2/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                displayData2(data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    function displayData2(data) {
        var dataContainer = document.getElementById('data-container2');

        // Assuming the API response is an array of objects with a 'name' property
        data.forEach(item => {
            var paragraph = document.createElement('p');
            paragraph.textContent = item.client_host2;
            dataContainer.appendChild(paragraph);
        });
    }
</script>

</body>
</html>


"""


    return HTMLResponse(content=html_content,status_code=200)


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
 
# @app.post('/my-endpoint')
# async def my_endpoint(stats: Stats, request: Request):
#     ip = request.client
#     print(ip)
#     return {'status': 1, 'message': 'ok'}


# @app.get("/ip1/")
# def read_root1(request: Request):
#     objects=[]
#     # client_host = request.client.host
#     d= {'client_host1':'Private IP:172.31.27.168, Public IP: 18.60.55.247'}
#     objects.append(d)
#     return objects


# @app.get("/ip2/")
# def read_root2(request: Request):
#     objects=[]
#     # client_host = request.client.host
#     d= {'client_host2':'Private IP:172.31.20.90, Public IP: 18.61.0.200'}
#     objects.append(d)
#     return objects