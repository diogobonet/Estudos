package Aula03;

public class aula03 {
    public static void main (String[] args) {
        caneta c1 = new caneta();
        c1.modelo = "BIC CRISTAL";
        c1.cor = "Azul";
        //c1.ponta = 0.5f;
        c1.carga = 50;
        //c1.tampada = false;
        c1.tampar();
        c1.status();
        c1.rabiscar();
    }
}
