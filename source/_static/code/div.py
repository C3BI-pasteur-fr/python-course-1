

def my_div(a, b):
    msg = "something unexpected happened"
    try:
        a = int(a)
        b = int(b)
        res = a / b
        msg = "{0} / {1}: {2}".format(a, b, res)
    except TypeError as err:
        msg = "one argument is missing"
    except ValueError as err:
        msg = "one of the args ({0} or {1} )cannot be converted in int".format(a, b)
    finally:
        print msg
