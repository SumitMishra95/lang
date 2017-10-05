package example2;

class dim
{
	double le;
	double br;
	double he;
	
	double volume()
	{
		return le * br * he;
	}
	
	dim(double b, double l, double h)
	{
		le = l;
		br = b;
		he = h;
	}
}

public class Class_parameters {

	public static void main(String[] args) {
		double vol;
		dim new_box1 = new dim(10, 2, 3);
		dim new_box2 = new dim(2, 3, 4);
		
		vol = new_box1.volume();
		System.out.println("The volume of the 1st box is " + vol);
		
		vol = new_box2.volume();
		System.out.println("The volume of the 2st box is " + vol);

	}

}
