package example2;

public class Argument_passing {

	public static void main(String[] args) {
		test obj = new test(10,20);
		
		System.out.println("Value before using class test : " + obj.a +" " + obj.b);
		obj.math(obj);
		System.out.println("Value after using class test : " + obj.a + " " + obj.b);
		

	}

}

class test
{
	int a,b;
	test (int i, int j)
	{
		a =i;
		b = j;
	}
	
	void math (test o)
	{
		o.a = o.a *2;
		o.b = o.b /2;
	}
}
