package Aula05;

public class Aula05 {
    public static void main(String[] args) {
        Banco b1 = new Banco(1,"Diogo", 0.5f, true);
        b1.abrirConta("CP");
        b1.fecharConta();
        b1.status();
    }
}
