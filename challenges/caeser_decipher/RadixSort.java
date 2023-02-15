import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class RadixSort {

    private static final int BASE = 10; // numbering system base (0-9 is 10)

    public static void main(String[] args) {
        System.out.println("Bucket Sort\n");

        System.out.println("Original: ");
        int[] input = randomIntList(25, 1000, 9999);
        printList(input);

        System.out.println("Sorted: ");
        int[] sorted = bucketSort(input);
        printList(sorted);
    }

    public static int[] bucketSort(int[] inputArray) {
        Stack<Integer> centralStack = new Stack<>();
        addAllIntsToStack(centralStack, inputArray);

        List<Stack<Integer>> buckets = new ArrayList<Stack<Integer>>(BASE);
        // initialize each Stack in buckets
        for (int i = 0; i < BASE; i++) {
            buckets.add(new Stack<Integer>());
        }

        int passes = getMaxDigitCount(inputArray);
        for (int pass = 0; pass < passes; pass++) { // each pass
            // distribute
            while (!centralStack.empty()) { // all numbers
                int num = centralStack.pop();
                int digit = getNthDigit(num, pass+1); // finds correct digit depending on which pass
                // System.out.println("Pass #" + pass + ":\tDigit: " + digit);
                for (int i = 0; i < buckets.size(); i++) { // through each bucket
                    if (digit == i) {
                        // System.out.println("Distributed into bucket: " + i);
                        buckets.get(i).push(num);
                        break;
                    }
                }
            }

            // combine
            for (int i = 0; i < buckets.size(); i++) { // all buckets
                while (!buckets.get(i).empty()) { // every number in each bucket
                    int num = buckets.get(i).pop();
                    centralStack.push(num);
                    // System.out.println("Successfully popped " + num + " from bucket " + i);
                }
            }
        }
        
        return intsFromIntegerStack(centralStack);
    }

    // gets the greatest amount of digits in one int from an int array
    private static int getMaxDigitCount(int[] input) {
        int count = 0;
        int[] clonedInput = input.clone(); // ensures a new reference to not destroy input
        for (int i = 0; i < clonedInput.length; i++) {
            count = Math.max(count, getMaxDigitCount(clonedInput[i]));
        }
        return count;
    }

    // gets the greatest amount of digits in one int. Can be used directly if range is known
    private static int getMaxDigitCount(int input) {
        int count = 0;
        while (input > 0) {
            input /= BASE;
            count++;
        }
        return count;
    }

    // formula from StackOverflow user João Silva
    private static int getNthDigit(int number, int n) {    
        return (int) ((number / Math.pow(BASE, n - 1)) % BASE);
    }

    private static void addAllIntsToStack(Stack<Integer> stack, int[] inputArray) {
        for (int input : inputArray) {
            stack.push(input);
        }
    }

    // returns an int[] from a Stack of Integers. (This seems like a bad way of doing this)
    private static int[] intsFromIntegerStack(Stack<Integer> stack) {
        int[] ints = new int[stack.size()];
        for (int i = 0; i < stack.size(); i++) {
            ints[i] = stack.get(i);
        }
        return ints;
    }

    public static void printList(int[] values) {
        String out = "[";
        for (int i = 0; i < values.length; i++) {
            out += values[i];
            if (i < values.length-1) {
                out += ", ";
            } else {
                out += "]";
            }
        }
        System.out.println(out);
    }

    // generates an int array with length length and with numbers between min and max (inclusive)
    public static int[] randomIntList(int length, int min, int max) {
        int[] values = new int[length];
        for (int i = 0; i < values.length; i++) {
            values[i] = (int)(Math.random() * (max - min + 1)) + min;
        }
        return values;
    }

    public static int[] reverseList(int[] list) {
        int[] reverse = new int[list.length];
        for (int i = list.length-1; i >= 0; i--){
            reverse.add(list[i]);
        }
        return reverse;
    }
}