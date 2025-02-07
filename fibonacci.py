def fibonacci(n):
    if n == 0:
      return 0
    if n == 1:
      return 1
  #if not isinstance(n, int):
		#return "N must be an integer"
	#if n < 0:
		#return "N must be positive"
    else:
      fib_list = [0, 1, 1]
        #fn = n-1 + n-2
      for i in range(3, n+1, 1):
        #print("i", i)
        if i-2 < 0:
          return fib_list[n]
        fib_list.append(fib_list[i-1] + fib_list[i-2])
        #print("append", fib_list[i-1] + fib_list[i-2])
        #print(fib_list)
      return fib_list[n]
	
#print(fibonacci(3))


