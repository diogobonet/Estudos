import java.util.ArrayList;
import java.util.Scanner;

public class Jogo {
    String opcao;
    public static void menuGame() {
        Scanner scanner = new Scanner(System.in);
        int opcao = 0;
        System.out.println("=====================");
        System.out.print("[1] -> + Dicas\n");
        System.out.print("[2] -> + Tentar acertar\n");
        System.out.println("[3] -> + Parar de jogar");
        System.out.println("=====================\n");

        while (opcao != 3) {

            opcao = scanner.nextInt();

            switch (opcao) {
                case 1: {
                    break;
                }

                case 2: {
                    System.out.println("Escolheu a opção 2");
                }

                case 3:
                    System.out.println("Saindo!");
                    break;

                default:
                    System.out.println("Opção inválida.");
                    break;
            }
        }

    }

    public static void dica(ArrayList<String> game1) {
        Scanner scanner = new Scanner(System.in);
        String opcao;
        opcao = scanner.next();
    }
}
