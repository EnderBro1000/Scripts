import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public class CaeserCipher {

    private ArrayList<String> words;
    
    public CaeserCipher(File wordFile) {
        words = getLines(wordFile);
    }

    
    public String[] cipher(File testFile, int key) {
        ArrayList<String> inputLines = getLines(testFile);
        String[] outputLines = new String[inputLines.size()];
        for (int i = 0; i < inputLines.size(); i++) { // each line
            outputLines[i] = "";
            String inputLine = inputLines.get(i);
            for (int j = 0; j < inputLine.length(); j++) { // each character
                outputLines[i] += cipheredChar(inputLine.charAt(i), key);
            }
        }
        
        
        return outputLines; 
    }
    
    private char cipheredChar(char initial, int key) {

        int ascii = initial; 
        int remain; 

        return (char)32; 

    }

    private static boolean charIsUppercase(char c) {
        boolean isUpperCase; 
        int ascii = c; 
        //65 through 90
        if(ascii >= 65 || ascii < 90){
            isUpperCase = true; 
        }else{
            isUpperCase = false; 
        }
        
        return isUpperCase; 
    }

    private static boolean charIsLowercase(char c) {
        boolean isLowerCase; 
        int ascii = c; 
        //97 - 121
        if(ascii >= 97 || ascii <= 121){
            isLowerCase = true; 
        }else{
            isLowerCase =  false; 
        }
        return isLowerCase; 
    
    }
    
    
    public String[] decipher(File testFile) {
        ArrayList<String> inputLines = getLines(testFile);
        String[] outputLines = new String[inputLines.size()];

        int key = findKey();

        for (int i = 0; i < inputLines.size(); i++) { // each line
            outputLines[i] = "";
            String inputLine = inputLines.get(i);
            for (int j = 0; j < inputLine.length(); j++) { // each character
                outputLines[i] += decipherChar(inputLine.charAt(i), key);
            }
        }
        
        return outputLines;
    }
    
    // sorted list containing amount of characters 
    private int[] getCharFrequency(ArrayList<String> inputLines) {
        int[] charFrequencies = new int[52]; 
        for (String inputLine : inputLines) {
            for (int cIndex = 0; cIndex < inputLine.length(); cIndex++) {
                int ascii = (int)(inputLine.charAt(cIndex));
                charFrequencies[ascii]++;
            }
        }
        
        
        
    }

    private int findKey() {
        int key = 
    }
    
    private char decipherChar(char initial, int key) {
        
    }

    private static ArrayList<String> getLines(File input) {
        try {
            ArrayList<String> lines = new ArrayList<>();
            Scanner scan = new Scanner(testFile); 
            while (scan.hasNextLine()) {
                 lines.add(scan.nextLine());
            }
            scan.close();
            
            return lines;
        } catch (Exception e) {
            System.out.println("File not found");  
            e.printStackTrace();
        }

        return null;
    }

    public static int randomInt(int min, int max) {
        return (int)(Math.random() * (max - min + 1));
    }

    public static void main(String[] args) {
        CaeserCipher cipher = new CaeserCipher(new File("words.txt"));
        String[] output = cipher.cipher(new File("tiny.txt"), CaeserCipher.randomInt(0, 25));
        
        System.out.println("test:");
        for (String outputLine : output){
            System.out.println(outputLine);
        }
    }


}
