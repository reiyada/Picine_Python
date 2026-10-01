from callLimit import callLimit


# @callLimit(3) is same as f = callLimit(3)(f)
@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


for i in range(3):
    print(f"=====  Loop {i + 1} =====")
    f()
    g()
