def fibonacci(count):
	if count == 0: return 0 
	if count == 1: return 1

	return fibonacci(count - 1) + fibonacci(count - 2)

if __name__ == "__main__":
    print(fibonacci(40))