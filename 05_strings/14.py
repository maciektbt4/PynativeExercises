from queue import Empty


str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
str_list = [x for x in str_list if x != "" and x is not None]
print(str_list)