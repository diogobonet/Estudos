package Faculdade.Aula01.Exercicios.Casa;
import java.util.Arrays;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.println("============================================");
        System.out.println("Endereço:");

        System.out.print("Digite o nome da Rua: ");
        String rua = teclado.nextLine();

        System.out.print("Digite o número da residencia: ");
        int numero = teclado.nextInt();

        System.out.println("Digite o complemento residencia: ");
        String complemento = teclado.next();

        System.out.print("Digite o bairro residencia: ");
        String bairro = teclado.next();

        System.out.println("============================================");
        System.out.print("Digite o número de quartos: ");
        int numQuartos = teclado.nextInt();

        System.out.print("Digite a COR da Casa: ");
        String cor = teclado.next();

        System.out.print("Digite quantos metros quadrados (m²): ");
        float m2 = teclado.nextFloat();

        System.out.print("Digite qual o valor atual da CASA: R$");
        float valor = teclado.nextFloat();

        System.out.print("A casa está trancada? ");
        boolean trancada = teclado.hasNext();

        System.out.print("============================================");
        System.out.print("Digite o nome do proprietário: ");
        String nome = teclado.next();
        System.out.print("Digite a idade: " );
        int idade = teclado.nextInt();
        System.out.print("Digite o CPF: ");
        String CPF = teclado.next();
        System.out.print("Digite o telefone: ");
        int telefone = teclado.nextInt();
        System.out.print("Digite o salario: ");
        float salario = teclado.nextFloat();

        Endereço add = new Endereço(rua, numero, complemento, bairro);
        Casa casa = new Casa(cor, numQuartos, m2, valor, trancada);
        Proprietario pessoa = new Proprietario(nome, idade, CPF, telefone, salario);
        add.status();
        casa.status();
    }
}
