package example2;

public class Stringdemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str1 = "First String";
		String str2 = "Second String";
		String str3 = str1;
		
    // Counts no of characters in strings.
		System.out.println("No of characters in str1: " + str1.length());
    // Gets the character at the 4th position.
		System.out.println("char at 0th position in str2: " + str2.charAt(3)); //counts start at 0th position.
		
		if (str1.equals(str2))
			System.out.println("str1 == str2");
		else
			System.out.println("str1 != str2");
		
		if (str1.equals(str3))
			System.out.println("str1 == str3");
		else
			System.out.println("str1 != str3");

	}

}
