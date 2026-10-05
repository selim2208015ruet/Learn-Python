def test(*args, **kwargs):
    print(args)
    print(kwargs)
    
test(10, 20, name="Selim", age=22)