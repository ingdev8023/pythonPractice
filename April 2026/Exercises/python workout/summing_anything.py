def mysum(*args):
    if not args:
        return args
    output = args[0]
    for arg in args[1:]:
        output += arg
    return output

print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum('a', 'b', 'c', 'd'))
print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))