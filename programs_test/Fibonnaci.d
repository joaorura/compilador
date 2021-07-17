void fib(int n)
{                                          
	int fib1 = 1, fib2 = 1, soma;

	while(fib1 < n) {
		print(fib1);
		                                    
		soma = fib1 + fib2;                    
		fib1 = fib2;                           
		fib2 = soma;
	}
}                                          

int main()
{
	int n;
	scan(n);
	fib(n);
	
	return 0;
}