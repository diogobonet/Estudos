package Atividade05.exercicio1;
import java.util.ArrayList;

public class A {

    public static void main(String[] args) {
        int inicial = 1000000;
        int ultimo = 1000500;

        long startTime = System.currentTimeMillis();

        ArrayList<Integer> primos = new ArrayList<>();

        for (int i = inicial; i <= ultimo; i++){
            if(isPrimo(i)){
                primos.add(i);
            }
        }

        System.out.println("Números primos no intervalo: " + inicial + " - " + ultimo);
        for (int num : primos){
            System.out.print(num + " ");
        }

        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;
        System.out.println("Tempo de Execução: " + executionTime);
    }
    private static boolean isPrimo(int numero) {
        for (int i = 2; i < numero; i++) {
            if (numero % i == 0)
                return false;
        }
        return true;
    }
}
