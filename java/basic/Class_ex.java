package example2;

class box
{
	double h;
	double b;
	double l;
}

class square
{
	double l;
	double b;
}

public class Class_box {

	public static void main(String[] args) {
		box new_box = new box();
		square new_square = new square();
		double volume,area;
		new_box.b = new_square.b = 10;
		new_box.h = 15;
		new_box.l = new_square.l = 20;
		
		volume =new_box.b * new_box.h * new_box.l;
		area = new_square.b * new_square.l;
		System.out.println("And the volume of the box is " + volume);
		System.out.println("And the square of the box is " + area);

	}

}
