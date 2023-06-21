package Atividade05;

public class C {
    public static void main(String[] args) {
        int inicio = 1000000;
        int ultimo = 1000500;
        long startTime = System.currentTimeMillis();


        System.out.println("Números primos no intervalo: " + inicio + " - " + ultimo);

        MinhaThread thread1 = new MinhaThread();
        thread1.setName("Thread1");
        thread1.inicio = inicio;
        thread1.ultimo = (ultimo-inicio)/2;

        MinhaThread thread2 = new MinhaThread();
        thread2.setName("Thread1");
        thread2.inicio = ((ultimo-inicio)/2)+1;
        thread2.ultimo = ultimo;

        thread1.start();
        thread2.start();

        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;
        System.out.println("Tempo de Execução: " + executionTime);
    }
}
