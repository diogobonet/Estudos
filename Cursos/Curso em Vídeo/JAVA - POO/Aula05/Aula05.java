package Aula05;

public class Aula05 {
    public static void main(String[] args) {
        Banco b1 = new Banco(1,"Diogo");

        b1.abrirConta("CP");
        b1.pagarMensal();
        b1.status();
    }
}
