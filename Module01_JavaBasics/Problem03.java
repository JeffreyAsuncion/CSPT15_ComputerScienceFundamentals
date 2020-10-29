
public class Problem03 {

    public static void main(String[] args) {
    
        String str = "Welcome To Java"; // Original string
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
}
