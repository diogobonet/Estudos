package Aula02;

public class aula02 {
    public static void main (String[] args) {
        caneta c1 = new caneta();
        c1.modelo = "Caneta BIC";
        c1.cor = "Preta";
        c1.destampar();
        c1.carga = 40;
        c1.ponta = 0.45f;
        c1.status();
        c1.rabiscar();

        System.out.println("------");

        caneta c2 = new caneta();
        c2.modelo = "Caneta Azul Azul Caneta";
        c2.cor = "Azul";
        c2.tampar();
        c2.ponta = 0.25f;
        c2.status();
        c2.rabiscar();
    }

}
