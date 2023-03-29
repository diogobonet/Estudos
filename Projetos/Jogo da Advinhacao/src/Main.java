import java.util.ArrayList;
import java.util.Scanner;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        ArrayList<String> game1 = new ArrayList<String>();
        game1.add("Ayrton Senna");
        game1.add("Foi um grande piloto de F1");
        game1.add("Pilotava muito bem na chuva");
        game1.add("Foi chamado de Mr. Monaco");
        game1.add("Fez 65 poles na carreira na F1");
        game1.add("Morou em Mônaco");
        game1.add("Foi tricampeão da F1");
        game1.add("Seu maior rival era francês");
        game1.add("Namorou uma famosa apresentadora da televisão");
        game1.add("Fundou um instituto para ajudar crianças e adolecentes");
        game1.add("Sua vitória favorita foi no país onde nasceu");
        int chances = 10;

        while (chances <= 10 & chances > 0) {
            ArrayList<Integer> escolhas = new ArrayList<Integer>();
            /*
            Adicionar as escolhas do usuário em
            para ele não escolher elas de novo
            */

            Random gerador = new Random();

            if ()
            System.out.print("Escolha uma dica: ");
            int escolhaDica = teclado.nextInt();

//            String chute = teclado.next();

//            if (chute != game1.get(0)) {
//                escolhaDica -= 1;
//            }
            String c = game1.get(escolhaDica);
            System.out.println(c);
        }
    }
}