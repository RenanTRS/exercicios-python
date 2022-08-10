import java.util.Scanner;

public class Ex008 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        System.out.print("Informe a quantidade de metros: ");
        float m = scan.nextFloat();

        float cm = m * 100;
        float mm = m * 1000;

        scan.close();

        System.out.printf("Cm: %.1fcm \nMm: %.1fmm \n", cm, mm);
    }
}
