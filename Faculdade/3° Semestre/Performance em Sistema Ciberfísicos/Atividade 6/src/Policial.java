public class Policial extends Thread{
    @Override
    public void run() {
        for (int i = 10; i > 0; i--){
            System.out.println("Tempo para o POLICIAL chegar: " + i);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
        System.out.println("Tempo Encerrado! O Policial chegou! Você está preso!");
        System.exit(0);
    }
}
