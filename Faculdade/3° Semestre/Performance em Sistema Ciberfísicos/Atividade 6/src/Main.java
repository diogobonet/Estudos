public class Main {
    public static void main(String[] args) {
        Cofre cofre = new Cofre();
        cofre.gerarsenha();
        Policial p = new Policial();
        HackerAscendente h1 = new HackerAscendente();
        HackerDescendente h2 = new HackerDescendente();
        h1.start();
        h2.start();
        p.start();
    }
}