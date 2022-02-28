def type_function(input):
    if type(input) == int:
        print("Integer")
    elif type(input) == str:
        print("String")
    elif type(input) == bool:
        print("Boolean")
    elif type(input) == object or type(input) == dict or type(input) == list:
        print("Object")


type_function()