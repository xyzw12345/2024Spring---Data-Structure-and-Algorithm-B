f = lambda y : (lambda x : x + y)

#g = (lambda f, x: (lambda y : f(f, x, y)))(lambda g, x, y : [] if y == [] else (x, y[0]) + g(g, x, y[1 : ]))

#print(g(1, [2, 3, 4, 5]))

print(f(1)(2))

h = (lambda f : (lambda x : f(f, x)))(lambda y, n : 1 if n == 0 else n * y(y, n - 1))

print(h(5))

u = (lambda f : (lambda x, y : f(f, x, y)))(lambda g, x, y : [] if (x == [] or y == []) else (lambda x, y : list((x, item) for item in y))(x[0], y) + g(g, x[1 :], y))

print(u([1, 2, 3], [4, 5, 6]))