import java.util.Random;

public class Cofre {
    private static int senha;
    public void gerarsenha(){
        Random random = new Random();
        int numero = random.nextInt(99999);
        senha = numero;
        System.out.println("A Senha é " + senha);
    }
    public static boolean testarsenha(int bruteforce){
        return bruteforce == senha;
    }
}
