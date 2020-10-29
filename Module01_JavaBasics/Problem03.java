// https://www.youtube.com/watch?v=uYLkKT-VrmM

public class Problem03 {

    public static void main(String[] args) {
    
	    
	// Approach1
	
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
	        /* THIS DOES NOT WORK AS PLANNED
		if (Character.isUpperCase(w.charAt(i)))
		{
			w.charAt(i) = w.toLowerCase();
		}
		else
		{
			w.charAt(i) = w.charAt(i).toUppercase();
		}
		*/
		reverseword = reverseword + w.charAt(i);
	    }
	    // Step 3 - rebuild the String with reverseword from 2a
	    reverseString = reverseString + reverseword + " "; // emocleW
	}
	System.out.println(reverseString);
	
	/*	
	// Approach2
	
        String str = "Welcome To Java"; // Original string
	
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
	*/
	
    }
}
