

def div(a,b):
    print(a/b)


def smart_div(funt):

    def inner(a,b):
        if a<b :
            a,b = b,a

        return funt(a,b)
    return inner

div = smart_div(div)


div(6,3)
div(3,6)