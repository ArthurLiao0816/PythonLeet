from datetime import date


def func(x=100):
    list = []
    for i in range(x):
        list.append(x)


def test(fun: callable = None):
    from datetime import datetime
    startTime = datetime.now().timestamp()
    fun(50_000_000)
    endTime = datetime.now().timestamp()
    print(endTime-startTime)


test(func)
