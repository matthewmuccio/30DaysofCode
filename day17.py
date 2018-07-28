class Calculator(object):
    def power(self, n, p):
        self.n = n
        self.p = p
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n ** p


if __name__ == "__main__":
	myCalculator = Calculator()
	x = int(input())
	for i in range(x):
		n, p = map(int, input().split())
		try:
			ans = myCalculator.power(n,p)
			print(ans)
		except Exception as e:
			print(e)
