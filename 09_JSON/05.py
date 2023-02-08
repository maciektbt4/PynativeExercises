import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

dicFromJson =  json.loads(sampleJson)
print (dicFromJson["company"]["employee"]["payble"]["salary"])
