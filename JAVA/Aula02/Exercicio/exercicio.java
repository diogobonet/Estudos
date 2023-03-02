package Aula02.Exercicio;

public class exercicio {
    public static void main (String[] args) {
        contrabaixo b1 = new contrabaixo();
        b1.marca = "Tagima";
        b1.modelo = "TJB5";
        b1.quantidadecordas = 5;
        b1.plugado = true;
        b1.volume = 100;
        b1.status();
        b1.desplug();
        b1.tocando();
    }
}
