package example;
import java.util.Random;

public class Loop {

	public static void main(String[] args) {
		
		Random r = new Random();
		 int i =1;
		 for (i = 1; i <= 10; i=i+2)
			 System.out.println(r.nextInt(10));
	}
}
