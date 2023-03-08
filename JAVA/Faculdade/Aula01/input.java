package Faculdade.Aula01;
import java.util.Arrays;
import java.util.Scanner;

public class input {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite um número: ");
        int k = teclado.nextInt();
        System.out.println("O número digitado foi: " + k);
        System.out.print("Digite seu nome: ");
        String n = teclado.next();
        System.out.println("O seu nome é: " + n);
    }
}
