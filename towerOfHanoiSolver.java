import java.util.Scanner;

public class towerOfHanoiSolver {
    static void towerOfHanoi(int n, int source, int dest, int aux) {
        if (n == 1) {
            System.out.println("Move disk 1 from peg "+ source+" to peg "+dest);
            return;
        }
        towerOfHanoi(n - 1, source, aux, dest);
        System.out.println("Move disk "+ n + " from peg " + source +" to peg " + dest );
        towerOfHanoi(n - 1, aux, dest, source);
    }

    // Driver code
    public static void  main(String args[]) {
        Scanner scnr = new Scanner(System.in);
        System.out.print("How many disks are on the tower?");
        int n = scnr.nextInt(); // Number of disks
        hanoi(n, 1, 2); // A, B and C are name of towers
    }
    public static void hanoi(int n, int source, int dest) {
        int aux;
        switch (source) {
            case 1:
                if (dest == 2) aux = 3;
                else aux = 2;
                break;
            case 2:
                if (dest == 1) aux = 3;
                else aux = 1;
                break;
            case 3:
                if (dest == 1) aux = 2;
                else aux = 1;
                break;
            default:
                aux = 0;
                System.out.println("Error");
        }

        if (n == 1) {
            System.out.println("Move disk 1 from peg "+ source+" to peg "+dest);
            return;
        }
        hanoi(n - 1, source, aux);
        System.out.println("Move disk "+ n + " from peg " + source +" to peg " + dest );
        hanoi(n - 1, aux, dest);
    }
}