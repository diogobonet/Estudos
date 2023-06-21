package Atividade05;

import java.util.ArrayList;

public class MinhaThread extends Thread {
    public int inicio;
    public int ultimo;

    @Override
    public void run() {
        ArrayList<Integer> primos = new ArrayList<>();
        for (int i = inicio; i <= ultimo; i++){
            if(isPrimo(i)){
                primos.add(i);
            }
        }
        printar(primos);
    }
    private static boolean isPrimo(int numero) {
        for (int i = 2; i < numero; i++) {
            if (numero % i == 0)
                return false;
        }
        return true;
    }
    private void printar(ArrayList<Integer> primos){
        for (int num : primos){
            System.out.print(num + " ");
        }
    }

}
