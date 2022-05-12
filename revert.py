"""How to do an inversion of any string or list-type input using recursion..."""


def rev(string):
    string_type = type(string)
    empty_string = string_type()
    if string == empty_string:
        return empty_string
    rest = rev(string[1:]) #recursive magic
    first_string = string[0:1]
    result = rest + first_string

    return result


print(rev("string"))
print(rev([1,2,3]))
