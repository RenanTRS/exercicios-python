import java.util.Scanner;

public class Aula08 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número ");
        double n = scanner.nextInt();
        scanner.close();

        double r = Math.sqrt(n);

        System.out.print(r);
    }
}
