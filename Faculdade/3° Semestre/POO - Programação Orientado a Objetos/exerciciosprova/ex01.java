package exerciciosprova;
import java.util.Arrays;
import java.util.Scanner;

public class ex01 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Velocidade máxima: ");
        double vm = teclado.nextDouble(); // Velocidade Máxima input

        System.out.print("Velocidade do carro: ");
        double vc = teclado.nextDouble(); // Velocidade carro input

        if (vc > vm) {
            double dif = vc - vm;
            if (dif == 10) {
                System.out.println("Você tomou uma multa de R$100 por passar 10km's ou mais da velocidade " +
                        "máxima permitida!");
            }
            if (dif > 11 && dif <= 30) {
                System.out.println("Você tomou uma multa de R$183 por passar 10km's ou mais da velocidade " +
                        "máxima permitida!");
            }

            if (dif > 31) {
                System.out.println("Você tomou uma multa de R$347 por passar 10km's ou mais da velocidade " +
                        "máxima permitida!");

            }
        }
        else {
            System.out.println("Você está andando em velocidade normal da via.");
        }
    }
}
