package Faculdade.Aula01.Exercicios.Casa;
import java.util.Arrays;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.println("=-=-=-=-=-=-=-=-=-=-=-=-");
        System.out.println("Endereço:");

        System.out.print("Digite o nome da Rua: ");
        String rua = teclado.nextLine();

        System.out.print("Digite o número da residencia: ");
        int numero = teclado.nextInt();

        System.out.print("Digite o complemento residencia: ");
        String complemento = teclado.toString();

        System.out.print("Digite o bairro residencia: ");
        String bairro = teclado.next();

        Endereço add = new Endereço(rua, numero, complemento, bairro);
        add.status();
    }
}
