# Implement function that returns Nth Fibonacci number in recursive way.
def nth_fibonaci(n):
    a,b,count = 0,1,1
    while count <= n:
        a,b = b,a+b
        if count == n:
            return a
        count +=1
print nth_fibonaci(100)
# 354224848179261915075