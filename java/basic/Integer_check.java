package example;

public class Check_integer {

	public static void main(String[] args) {
// check once for 40 and 400 in the place of x and y
		
		         Integer x = 400, y = 400;
		         if (x == y)
		            System.out.println("Same");
		         else
		            System.out.println("Not Same");
		         // for this ans will be not same
		         // But instead of 400 if you try 40 it will be same 
		         
		         Integer x1 = 40, y1 = 40;
		         if (x1 == y1)
		            System.out.println("Same");
		         else
		            System.out.println("Not Same");
		         //Its because Integer only holds upto 127

	}

}
