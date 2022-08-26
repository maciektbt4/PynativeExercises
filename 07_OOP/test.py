class RememberObject:
    obejcts_list =[]


    def __init__(self, name) -> None:
        self.name = name     
        RememberObject.obejcts_list.append(self)

for i in range(5):
    object = RememberObject(f"Object {i}")
    print(f"Object {i}: {object.name}")


for object in RememberObject.obejcts_list:
    print(getattr(object, "name"))