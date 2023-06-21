public class HackerDescendente extends Thread {
    @Override
    public void run() {
        for (int i = 99999; i >= 0; i--){
            if(Cofre.testarsenha(i)){
                System.out.println("O Hacker 2 conseguiu descobrir a senha:" + i);
                System.exit(2);
            }

            try {
                Thread.sleep(1);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
