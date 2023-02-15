import java.util.Scanner;


public class Account {

    private double balance;

    public Account() {
        balance = 0;
    }

    public void transact(double amount) {
        balance = balance + amount; 
        balance = Math.round(balance * 100) / 100.0;

        String balStr = getBalanceString();

        double lowMargin = 250;
        String lowMarginStr = stringDouble(lowMargin);

        if (amount == 0) {
            System.out.println("Your final balance is " + balStr);
        } else if (balance < 0.0) {
            System.out.println("ALERT: Your account has a negative balance of " + balStr);
        } else if (balance < lowMargin && balance >= 0.0) {  
            System.out.println("WARNING: Your balance of " + balStr + " is less than " + lowMarginStr);
        } else {
            //System.out.println("Error: Your balance is: " + balStr); 
        }
    }

    private String getBalanceString() {
        return stringDouble(balance);
    }

    private static String stringDouble(double input) {
        String string = "$";
        string += input;
        String[] parts = string.split("\\.");
        if (parts[1].length() < 2) {
            string += "0";
        }

        return string;
    }

    public static void main(String[] args) {
        Account account = new Account();
        Scanner scan = new Scanner(System.in);

        double amount = -1;
        while (amount != 0) {
            System.out.print("Transaction: ");
            try {
                amount = scan.nextDouble();
                // System.out.println("Checking...");
                if ((amount * 100) % 1 == 0) {
                    // System.out.println("Success at: " + amount);
                    account.transact(amount);
                } else {
                    System.out.println("ALERT: No partial cents allowed.");
                }
            } catch (Exception e) {
                System.out.println("ALERT: Transaction must be a number.");
            }
            scan.nextLine();
        }


        scan.close();
    }
}
