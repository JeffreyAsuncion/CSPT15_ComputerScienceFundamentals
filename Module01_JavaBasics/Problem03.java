// https://www.youtube.com/watch?v=uYLkKT-VrmM

public class Problem03 {

    public void SwitchCase1(String str) {
    
	    
	// Approach1
	
        //String str = "Welcome To Java"; // Original string
        // Step 1 - split string into words
	String[] words = str.split(" ");  //Splitting into words

	String reverseString = "";
	// Step 2 - go thru each word
	for (String w:words) 
	{
	    // Step 2a - reverse each word char by char
	    String reverseword = "";
	    // start from end of word	
	    for (int i=w.length()-1; i >=0; i--) // Welcome
	    {
		reverseword = reverseword + w.charAt(i);
	    }
	    // Step 3 - rebuild the String with reverseword from 2a
	    reverseString = reverseString + reverseword + " "; // emocleW
	}
	System.out.println(reverseString);
    }	

    public void SwitchCase2(String str) {
	
	// Approach2
	
        //String str = "Welcome To Java"; // Original string
	
	//Step 1 split into array of words
	String[] words = str.split("\\s");

	String reverseword = "";

	for (String w:words)// Welcome // like for(w in words) python
	{
	    // Step 2
	    StringBuilder sb = new StringBuilder(w);  //
	    sb.reverse(); // built-in function // emocleW
	    
            // Step 3	    
	    reverseword = reverseword + sb.toString() + " ";
	}

	System.out.println(reverseword);

    }

    // Method to convert characters of string to opposite case
    // https://www.geeksforgeeks.org/convert-alternate-characters-string-upper-case/
    public static String convertOpposite(StringBuffer str)
    {
        int ln = str.length();

	// Conversion using predefined methods
	for (int i=0; i<ln; i++)
	{
	    Character c = str.charAt(i);
	    if (Character.isLowerCase(c))
                str.replace(i, i+1, Character.toUpperCase(c)+"");
	    else
		str.replace(i, i+1, Character.toLowerCase(c)+"");
	}
	return str;
    }

    public static void main(String[] args) {
    
        StringBuffer str = new StringBuffer("Hello World!");
	// Calling the Method
	convertOpposite(str);

	System.out.println(str);
		://www.geeksforgeeks.org/convert-alternate-characters-string-upper-case//
    
    }





}
