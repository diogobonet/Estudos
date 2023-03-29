package exerciciosprova;

import java.util.Arrays;
import java.util.Scanner;

public class ex08 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("RA1: ");
        float ra1 = teclado.nextFloat();
        System.out.print("RA2: ");
        float ra2 = teclado.nextFloat();
        System.out.print("RA3: ");
        float ra3 = teclado.nextFloat();

        double result = (0.30 * ra1) + (0.30 * ra2) + (0.40 * ra3);

        System.out.println("Sua nota foi: " + result);
        if (result > 6) {
            System.out.println("Aprovado!");
        }

        if (result < 6 && result > 4) {
            System.out.println("Verificação suplementar");
        }

        if (result < 4) {
            System.out.println("Reprovado kkkkkkkkkkkkkkkkkk!");
        }
    }
}
