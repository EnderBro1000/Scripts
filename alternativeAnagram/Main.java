import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Main {
    
    public static Scanner standardInput;

    static {
        standardInput = new Scanner(System.in);
    }

    public static void main(String[] args) {
        /*
        String input = "gggggg";

        // if (input.length() % 2 != 0){
        //     System.out.println("");
        // }

        String anagram = anagram(input);

        System.out.println(anagram != null ? anagram : -1);

        */
        //String input = inToString();
        //String input = standardInput.nextLine();

        final long startTime = System.currentTimeMillis();

        String input = "nadlannoru";

        String anagram = anagram(input);
        
        System.out.println((anagram == null) ? "-1" : anagram);

        final long endTime = System.currentTimeMillis();

        final long computeTime = endTime - startTime;
        System.out.println("Time to complete: " + computeTime + "ms");
    }
    
    
    public static String anagram(String input) {

        input = sortedString(input);
        
        // if (trueAnagram(input)) return input;


        final int halfLength = input.length() / 2;
        final char midChar = input.charAt(halfLength);

        final int swap1Index = findSwap1(input, halfLength, midChar);
        final int swap2Index = findSwap2(input, midChar);

        if (swap2Index == -1) return null; // unsolvable

        return swap(input, swap1Index, swap2Index);
    }

    private static int findSwap1(String input, int halfLength, char midChar) {

        int firstPartCount = countCharInString(input.substring(0, halfLength), midChar);
        int secondPartCount = countCharInString(input.substring(halfLength), midChar);

        // go in opposite direction of comparison, becuase you swap towards smaller characters from halfLength
        return (firstPartCount < secondPartCount) ? halfLength -1 : halfLength;
    }
    
    private static int findSwap2(String input, char midChar) {
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) != midChar) return i;
        }
        return -1; // unsolvable
    }

    public static String swap(String input, int swap1Index, int swap2Index) {
        char temp = input.charAt(swap1Index);
        input = setChar(input, input.charAt(swap2Index), swap1Index);
        return setChar(input, temp, swap2Index);
    }

    public static String setChar(String input, char replaceChar, int index) {
        return input.substring(0, index) + replaceChar + input.substring(index + 1);
    }

    public static int countCharInString(String str, char character) {
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == character) count++;
        }
        return count;
    }


    
    private static String halfSubstring(String input, int substringNumber) {
        return input.substring(substringNumber, substringNumber + input.length()/2);
    }
    
    private static String[] halfSubstrings(String input) {
        int inputHalf = input.length()/2 + 1;
        String[] substrings = new String[inputHalf];
        for (int i = 0; i < inputHalf; i++) {
            substrings[i] = halfSubstring(input, i);
        }
        return substrings;
    }

    // returns true when String is an 'alternate' anagram
    private static boolean trueAnagram(String anagram) {
        String[] substrings = halfSubstrings(anagram);
        return !duplicateElements(substrings);
    }


    private static <T> boolean duplicateElements(T[] list) {
        Set<T> set = new HashSet<T>();

        for (T subPiece : list) {
            if (!set.add(subPiece)) return true;
        }
        return false;
    }

    // sorts a String array in ascending order and returns the result.
    public static String sortedString(String str) {
        List<Character> list = new ArrayList<Character>();
        for (int i = 0; i < str.length(); i++) {
            list.add(str.charAt(i));
        }
        Collections.sort(list);
        // {b,a,c}
        // {a,b,c}
        String out = "";
        for (int i = 0; i < str.length(); i++) {
            out += list.get(i);
        }
        return out;
    }

    // converts System.in input (file) to a single String, with no breaks between the line(s).
    public static String inToString() {
        Scanner input = new Scanner(System.in);
        String allLines = "";
        while(input.hasNextLine()) {
            allLines += input.nextLine();
        }
        input.close();
        return allLines;
    }
}
