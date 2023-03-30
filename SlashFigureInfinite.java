import java.util.Scanner;
public class SlashFigureInfinite {
    public static int SIZE;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("How large?>");
        SIZE = scanner.nextInt();
        System.out.println();
        for (int i = 1; i <= SIZE; i++) {
            for (int j = 1; j <= 2 * i - 2; j++) {
                System.out.print("\\");
            }
            for (int j = 1; j <= -4 * i + (4 * SIZE + 2); j++) {
                System.out.print("!");
            }
            for (int j = 1; j <= 2 * i - 2; j++) {
                System.out.print("/");
            }
            System.out.println();
        }
    }
}
