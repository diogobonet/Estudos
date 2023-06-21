package Atividade05;

public class D {
    public static void main(String[] args) {
        int inicio = 2;
        int ultimo = 100;
        int fimconjunto = 0;
        long startTime = System.currentTimeMillis();
        System.out.println("Números primos no intervalo: " + inicio + " - " + ultimo);

        while (fimconjunto < ultimo){
            fimconjunto = Math.min((inicio + 10), ultimo);
            MinhaThread thread = new MinhaThread();
            thread.inicio = inicio;
            thread.ultimo = fimconjunto;
            thread.start();
            inicio = fimconjunto + 1;
        }
        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;
        System.out.println("Tempo de Execução: " + executionTime);
    }
}
