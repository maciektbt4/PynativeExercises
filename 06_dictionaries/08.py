sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

# pop function to remove item from dictionary returns value of delated item
sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)