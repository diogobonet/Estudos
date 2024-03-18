package Aula02.Exercicio;

public class contrabaixo {
    String marca;
    String modelo;
    int quantidadecordas;
    boolean plugado;
    int volume;


    void status() {
        System.out.println("Marca: " + this.marca);
        System.out.println("Modelo" + this.modelo);
        System.out.println("Quantidade de Cordas: " + this.quantidadecordas);
        System.out.println("Plugado: " + this.plugado);
        System.out.println("Volume: " + this.volume);
    }
    void tocando() {
        if (plugado == false) {
            System.out.println("ERRO! Não pode tocar com o cabo desplugado!");
        } else {
            System.out.println("Estou tocando normalmente!");
        }
    }

    void plug() {
        this.plugado = true;
    }

    void desplug() {
        this.plugado = false;
    }
}
