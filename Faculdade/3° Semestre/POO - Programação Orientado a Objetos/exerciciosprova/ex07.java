package exerciciosprova;

import java.util.Arrays;
import java.util.Scanner;

public class ex07 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Valor 1: ");
        float v1 = teclado.nextFloat();

        System.out.print("Valor 2: ");
        float v2 = teclado.nextFloat();

        System.out.println("================");
        System.out.println("Selecione uma operação");
        System.out.println("Soma [+]");
        System.out.println("Subtração [-]");
        System.out.println("Multiplicação [*]");
        System.out.println("Divisão [/}");
        System.out.println("Resto da divisão [%]");
        System.out.print("-> ");
        String sel = teclado.next();

        switch (sel.hashCode()) {
            case '+':
                float result = v1 + v2;
                System.out.println(result);
            break;

            case '-':
                float result1 = v1 - v2;
                System.out.println(result1);
                break;
            case '*':
                float result2 = v1 * v2;
                System.out.println(result2);
                break;
            case '/':
                float result3 = v1 / v2;
                System.out.println(result3);
                break;
            case '%':
                float result4 = v1 % v2;
                System.out.println(result4);
                break;
        }
    }
}
