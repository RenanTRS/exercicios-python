import java.util.Scanner;

public class Aula06 {
    public static void main(String [] args) {
        int n1;
        int n2;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite um número");
        n1 = scanner.nextInt();

        System.out.println("Digite outro número");
        n2 = scanner.nextInt();

        scanner.close();
        
        System.out.printf("A soma entre %d e %d vale: %d \n", n1, n2, n1+n2);

        
    }
}