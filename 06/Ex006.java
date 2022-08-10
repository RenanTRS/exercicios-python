import java.util.Scanner;

public class Ex006 {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite um número: ");
        int n = scanner.nextInt();
        scanner.close();

        System.out.printf("Dobro: %d \nTriplo: %d \nRaiz Quadrada: %.0f \n", n*2, n*3, Math.sqrt(n));
    }
}
