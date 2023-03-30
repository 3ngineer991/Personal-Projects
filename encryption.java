//DISCLAIMER: this program is not intended for any serious use cases and is just a fun demonstration of my coding abilities
import java.util.*;

public class encryption {

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        String answer = "";
        while (!answer.equals("exit")) {
            System.out.println("\n\n---------------------Welcome to Collin's Encryption and Decryption center---------------------");
            System.out.println(    "Would you like to encrypt or decrypt a message? You can also leave by typing \"exit\"");
            System.out.print("> ");

            answer = scnr.next();

            switch (answer) {
                case "encrypt" -> encrypt();
                case "decrypt" -> decrypt();
                case "exit" -> System.out.println("Exiting");
                default -> System.out.println("ERROR: " + answer + " is an incorrect value or has not yet been implemented. Make sure to answer \"encrypt\", \"decrypt\", or \"exit\".");
            }
        }
    }

    private static void decrypt() {
        Scanner scnr = new Scanner(System.in);
        String key;
        String phrase;
        StringBuilder encryptedMessage = new StringBuilder();
        Queue<Character> keyQueue = new LinkedList<>();

        System.out.println("ALL phrases are encrypted and decrypted in lower case.");
        System.out.println("What is the key?");
        System.out.print("> ");
        key = scnr.nextLine().toLowerCase(Locale.ENGLISH);

        for (Character i: key.toCharArray()) {
            keyQueue.add(i);
        }

        System.out.println("What phrase do you want to decrypt?");
        System.out.print("> ");
        phrase = scnr.nextLine().toLowerCase(Locale.ENGLISH);

        for (char i: phrase.toCharArray()) {
            int tempKey = keyQueue.poll() - 97;
            char temp;
            if (i + tempKey > 122) {
                temp = (char) (i + tempKey - 26);
            } else {
                temp = (char) (i + tempKey);
            }
            temp = temp == ':' ? ' ': temp;
            encryptedMessage.append(temp);

            keyQueue.add((char) (tempKey + 97));
        }
        System.out.println("Encrypted message: " + encryptedMessage);
    }

    public static void encrypt() {
        Scanner scnr = new Scanner(System.in);
        String key;
        String phrase;
        StringBuilder encryptedMessage = new StringBuilder();
        Queue<Character> keyQueue = new LinkedList<>();

        System.out.println("What phrase do you want to use as the key?");
        System.out.print("> ");
        key = scnr.nextLine().toLowerCase(Locale.ENGLISH);

        for (Character i: key.toCharArray()) {
            keyQueue.add(i);
        }

        System.out.println("What phrase do you want to encrypt?(ONLY LETTERS AND SPACES ARE SUPPORTED)");
        System.out.print("> ");
        phrase = scnr.nextLine().toLowerCase(Locale.ENGLISH);

        for (char i: phrase.toCharArray()) {
            int tempKey = keyQueue.poll() - 97;
            char temp;
            if (i - tempKey < 97) {
                temp = (char) (i - tempKey + 26);
            } else {
                temp = (char) (i - tempKey);
            }
            encryptedMessage.append(temp);

            keyQueue.add((char) (tempKey + 97));
        }
        System.out.println("Encrypted message: " + encryptedMessage);
    }
}
