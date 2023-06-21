package Atividade05;

public class B {
    public static void main(String[] args) {
        int inicio = 1000000;
        int ultimo = 1000500;

        long startTime = System.currentTimeMillis();

        MinhaThread thread = new MinhaThread();
        thread.setName("Thread1");
        thread.inicio = inicio;
        thread.ultimo = ultimo;
        System.out.println("Números primos no intervalo: " + inicio + " - " + ultimo);
        thread.start();

        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;
        System.out.println("Tempo de Execução: " + executionTime);

    }
}
