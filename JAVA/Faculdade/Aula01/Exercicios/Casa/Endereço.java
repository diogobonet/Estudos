package Faculdade.Aula01.Exercicios.Casa;

public class Endereço {
    String rua;
    int numero;
    String complemento;
    String bairro;

    public Endereço(String rua, int numero, String complemento, String bairro) {
        this.rua = rua;
        this.numero = numero;
        this.complemento = complemento;
        this.bairro = bairro;
    }

    public void status() {
        System.out.println(this.getRua() + " | número: " + this.getNumero() + " | Complemento: "
        + this.getComplemento() + " | Reside no bairro: " + this.getBairro());
    }

    public String getRua() {
        return rua;
    }

    public void setRua(String rua) {
        this.rua = rua;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public String getComplemento() {
        return complemento;
    }

    public void setComplemento(String complemento) {
        this.complemento = complemento;
    }

    public String getBairro() {
        return bairro;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }
}

