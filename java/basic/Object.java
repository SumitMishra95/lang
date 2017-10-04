package example;

public class Continue {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i;
		for(i=0;i<10;i++)
		{
			System.out.print(i+ " ");
			if(i%2 == 0) continue;
				System.out.println();
		}
	}
}
