# Consider these two simple functions:

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

# What will the following function invocation return?

bar(foo())

# false, triggered by and short-circuit. 