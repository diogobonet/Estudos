package exerciciosprova;
import java.util.Arrays;
import java.util.Scanner;
import java.lang.Math;

public class ex02 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Altura: ");
        float altura = teclado.nextFloat();
        System.out.print("Peso: ");
        float peso = teclado.nextFloat();
        float imc = peso / (altura * altura);

        if (imc <= 18.5) {
            System.out.println("Abaixo do peso normal!");
        }

        if (imc > 18.5 && imc <= 25) {
            System.out.println("Peso normal!");
        }

        if (imc > 25 && imc <= 30) {
            System.out.println("Acima do peso normal");
        }

        if (imc > 30) {
            System.out.println("Obesidade");
        }

    }
}
