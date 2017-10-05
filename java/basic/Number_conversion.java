package example2;

public class Number_conversion {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i = 43245;
    // Convert from integer to binary
		System.out.println(i + " in binary		" + Integer.toBinaryString(i));
    // Convert from integer to octal
		System.out.println(i + " in octal		" + Integer.toOctalString(i));
    // Convert from integer to hexadecimal
		System.out.println(i + " in hexadecimal	" + Integer.toHexString(i));

	}

}
