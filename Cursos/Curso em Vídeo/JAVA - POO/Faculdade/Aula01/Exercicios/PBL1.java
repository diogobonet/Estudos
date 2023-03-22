package Faculdade.Aula01.Exercicios;
import java.util.Arrays;
import java.util.Scanner;


public class PBL1 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o valor do Primeiro termo de PA: ");
        double a_1 = teclado.nextDouble();
        System.out.print("Digite o valor da razão de PA: ");
        double r = teclado.nextDouble();
        System.out.print("Digite o número de termos de PA: ");
        int n = teclado.nextInt();
        double a_n = a_1 + (n-1) * r;
        System.out.println("Ultimo termo de PA: " + a_n);
        double s_n = (a_1 + a_n) * n / 2;
        System.out.println("Soma dos primeiros termos de uma PA: " + s_n);
    }
}
