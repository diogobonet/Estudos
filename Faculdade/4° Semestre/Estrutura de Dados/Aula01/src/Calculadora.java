import java.util.Scanner;
public class Calculadora {
    static void Menu() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o primeiro valor:");
        float val1 = scanner.nextFloat();
        System.out.println("Digite o segundo valor:");
        float val2 = scanner.nextFloat();
        System.out.println("Selecione uma opção: \n 1) Soma \n 2) Subtração \n 3) Multiplicação \n 4) Divisão");
        String opt = String.valueOf(scanner.hasNext());
        switch (opt.toString()) {
            case "Soma":
                Soma(val1, val2);
                break;
            case "Subtração":
                Sub(val1, val2);
                break;
            case "Multiplicação":
                Mult(val1, val2);
                break;
            case "Divisão":
                Div(val1, val2);
                break;
            default:
                System.out.println("Opção inválida!");
                break;
        }
    }

   static void Soma(float val1, float val2) {
        var resultado = val1 + val2;
       System.out.println("Resultado:" + resultado);
    }

    static void Sub(float val1, float val2) {
        var resultado = val1 - val2;
        System.out.println("Resultado:" + resultado);
    }

    static void Mult(float val1, float val2) {
        var resultado = val1 * val2;
        System.out.println("Resultado:" + resultado);
    }

    static void Div(float val1, float val2) {
        var resultado = val1 / val2;
        System.out.println("Resultado:" + resultado);
    }
}

