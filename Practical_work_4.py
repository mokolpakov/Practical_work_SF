# get-запрос

import requests
import json

params_get = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

headers_get = {'accept': 'application/json'}

petId_get = 556

res = requests.get(f"https://petstore.swagger.io/v2/pet/{petId_get}",
                   params=params_get, headers=headers_get)

print(f"Status code: {res.status_code}")
print(res.json())


# post-запрос

headers_post = {'accept': 'application/json', 'Content-Type': 'application/json'}

data_post = {
  "id": 557,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.post(f"https://petstore.swagger.io/v2/pet",
                    data=json.dumps(data_post, ensure_ascii=False), headers=headers_post)

print(f"Status code: {res.status_code}")
print(res.json())


# put-запрос

headers_put = {'accept': 'application/json', 'Content-Type': 'application/json'}

data_put = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.put(f"https://petstore.swagger.io/v2/pet",
                   data=json.dumps(data_put, ensure_ascii=False), headers=headers_put)

print(f"Status code: {res.status_code}")
print(res.json())

# delete-запрос

headers_delete = {'accept': 'application/json', 'Content-Type': 'application/json'}

petId_delete = 556

res = requests.delete(f"https://petstore.swagger.io/v2/pet/{petId_delete}",
                      headers=headers_delete)

print(f"Status code: {res.status_code}")
print(res.json())
