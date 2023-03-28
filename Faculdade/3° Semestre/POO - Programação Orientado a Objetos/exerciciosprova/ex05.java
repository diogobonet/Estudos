package exerciciosprova;
import java.util.Arrays;
import java.util.Scanner;

public class ex05 {
    public static void main(String[] args) { // Comparação de ano bissexto
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o ano: ");
        int ano = teclado.nextInt();

        if(ano % 400 == 0){
            System.out.println(ano + " é bissexto.");
            // se o ano for menor que 400
        } else if((ano % 4 == 0) && (ano % 100 != 0)){
            System.out.println(ano + " é bissexto.");
        } else{
            System.out.println(ano + " não é bissexto");
        }
    }
}
