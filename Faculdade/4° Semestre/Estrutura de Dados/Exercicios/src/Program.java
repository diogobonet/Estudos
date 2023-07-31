import java.util.Scanner;
public class Program {
    static void Menu() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("========================");
        System.out.println("Bem vindo ao Restaurante X!");
        System.out.println("========================");
        System.out.println("\n 1) Fazer Pedido \n 2) Sair \n Escolha uma opção: ");
        int opt = scanner.nextInt();

        switch (opt) {
            case 1:
                Pedido();
                break;
            case 2:
                System.out.println("Fechando programa...");
                System.exit(1);
                break;
        }
    }

    static void Pedido() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite seu nome:");
        String nome = scanner.next();
        Cardapio();
        System.out.println(nome + ", o que você deseja?");
        int opt = scanner.nextInt();
        while (opt != 0) {

        }
    }

    static void Cardapio() {
        System.out.println("Cardapio:");
        System.out.println("1) Prato da Casa (R$49.90)");
        System.out.println("2) Macarronada ào molho sugo (R$38.50)");
        System.out.println("3) Hamburguer (R$17.90)");
        System.out.println("4) Batata Doce (R$22.90)");
        System.out.println("5) Suco natural (R$ 08.50");
        System.out.println("6) Refrigerante 350ml (R$06.50)");
        System.out.println("0) Sair");
    }
}
