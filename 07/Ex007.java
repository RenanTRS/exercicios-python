import java.util.Scanner;

public class Ex007 {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a primeira nota: ");
        float nota1 = scanner.nextFloat();

        System.out.print("Digite a segunda nota: ");
        float nota2 = scanner.nextFloat();
        
        scanner.close();

        float media = (nota1 + nota2) / 2;

        System.out.printf("Média do aluno: %.1f \n", media);
    }
}
