/* input names - a list of strings
 *
 * output - an integer which is the location of Bob
 * if Bob not present return -1
 */ 

import java.util.ArrayList;


public class Problem01 {

    public static void main(String[] args) {
	
	String[] names_list = new String[] {"Jeff", "Kim", "Bob"};
	
	String name = "Bob";

	for (int i=0; i<names_list.length; i++) {
	    if (names_list[i] == name) {
	        System.out.println(name);
		System.out.println(i);
	    }
	    else {
	    	System.out.println("Bob is not here?");
	    }
	}
    }

}
