public class HackerAscendente extends Thread {
    @Override
    public void run() {
        for (int i = 0; i <= 99999; i++){
            if(Cofre.testarsenha(i)){
                System.out.println("O Hacker 1 conseguiu descobrir a senha:" + i);
                System.exit(1);
            }
            try {
                Thread.sleep(1);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
