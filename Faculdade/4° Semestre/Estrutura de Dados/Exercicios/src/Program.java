import java.util.Scanner;
import java.util.ArrayList;
public class Program {
    static int opt;
    static float valorTotal;
    static void Menu() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("===========================");
        System.out.println("Bem vindo ao Restaurante X!");
        System.out.println("===========================");
        System.out.println("\n1) Fazer Pedido \n2) Sair \nEscolha uma opção: ");
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
        ArrayList<String> produtos = new ArrayList<>();
        ArrayList<Float> valor = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite seu nome:");
        String nome = scanner.next();
        Cardapio();

        do {
            try {
                System.out.println(nome + ", o que você deseja?");
                opt = scanner.nextInt();
                switch (opt) {
                    case 1:
                        produtos.add(0, "Prato da Casa");
                        valor.add(0, 49.90f);
                        break;
                    case 2:
                        produtos.add(0, "Macarronada ào Molho Sugo");
                        valor.add(0, 38.50f);
                        break;
                    case 3:
                        produtos.add(0, "Hamburguer");
                        valor.add(0, 17.90f);
                        break;
                    case 4:
                        produtos.add(0, "Batata Doce");
                        valor.add(0, 22.90f);
                        break;
                    case 5:
                        produtos.add(0, "Suco Natural");
                        valor.add(0, 08.50f);
                        break;
                    case 6:
                        produtos.add(0, "Refrigerante");
                        valor.add(0, 06.50f);
                        break;
                    case 0:
                        for (Float n : valor) {
                            valorTotal += n;
                        }
                        NotaFiscal(valorTotal, valor, produtos);
                        return;
                    default:
                        System.out.println("Valor inválido! Tente novamente!");
                }
            }
            catch (Exception e) {
                System.out.println("ERRO! Tente novamente");
                Pedido();
                return;
            }

        } while (opt != 0);
    }

    static void Cardapio() {
        System.out.println("Cardapio:");
        System.out.println("1) Prato da Casa (R$49.90)");
        System.out.println("2) Macarronada ào molho sugo (R$38.50)");
        System.out.println("3) Hamburguer (R$17.90)");
        System.out.println("4) Batata Doce (R$22.90)");
        System.out.println("5) Suco Natural (R$ 08.50");
        System.out.println("6) Refrigerante 350ml (R$06.50)");
        System.out.println("0) Sair");
    }

    static void NotaFiscal(float valorTotal, ArrayList valor, ArrayList produtos) {
        float valorFinal = valorTotal;
        var taxaServico = valorFinal * 0.1;
        valorTotal += taxaServico;
        System.out.println("Produtos: " + produtos);
        System.out.println("Valor dos Produtos:  R$" + valor);
        System.out.println("Taxa de Serviço: R$" + taxaServico);
        System.out.println("Valor Total: R$" + valorTotal);
    }
}

/* DESCULPA PROFESSORA MARINA PELO CÓDIGO PORCO 😉 */
