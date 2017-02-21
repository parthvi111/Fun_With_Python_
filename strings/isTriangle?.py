def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)
      

print is_triangle(1,2,2) 