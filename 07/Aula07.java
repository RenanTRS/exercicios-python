import java.util.Scanner;

public class Aula07 {
    public static void main(String[] args) {
        int n1;
        int n2;

        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite um número: ");
        n1 = scanner.nextInt();

        System.out.print("Digite outro número: ");
        n2 = scanner.nextInt();

        scanner.close();

        int s = n1 + n2;
        int m = n1 * n2;
        float d = n1 / n2;
        int di = n1 / n2;
        double e = Math.pow(n1, n2);

        System.out.printf("Soma: %d, Produto: %d e a Divisão: %.1f \n", s, m, d);
        System.out.printf("Divisão inteira: %d e Exponênciação: %.0f \n", di, e);
    }
}
