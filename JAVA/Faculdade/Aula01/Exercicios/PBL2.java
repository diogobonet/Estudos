package Faculdade.Aula01.Exercicios;
import java.lang.Math;
import java.util.Arrays;
import java.util.Scanner;

public class PBL2 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o valor de A: ");
        float a = teclado.nextFloat();
        System.out.print("Digite o valor de B: ");
        float b = teclado.nextFloat();


        if (a <= b) {
            System.out.print("Digite a quantidade de repetições: ");
            int n = teclado.nextInt();
            if (n > 0) {
                double area_total = 0;
                double x = a;
                double h = (b - a) / n;
                double y1 = f(x);
                int i = 0;
                while (i < n) {
                    x += h;
                    double y2 = f(x);
                    double area_do_trapezio = ((y1 + y2) / 2) * h;
                    area_total += area_do_trapezio;
                    y1 = y2;
                    i++;
                    System.out.println("Área total: " + area_total);
                }
            }
            else {
                System.out.println("O valor de A deve ser >= B");
            }
        }
    }
    public static double f(double x) {
        return (2 * Math.sin(x)) + (Math.cos(x)/3);
    }
}
