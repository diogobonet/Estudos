package Faculdade.Aula01.Exercicios.Casa;

public class Casa {
    String cor;
    int numeroCasa;
    int quartos;
    float m2;
    float valor;
    boolean trancado;
    boolean portao;
    String proprietario;

    public Casa(String cor, int quartos, float m2, float valor, boolean trancado) {
        this.cor = cor;
        this.quartos = quartos;
        this.m2 = m2;
        this.valor = valor;
        this.trancado = trancado;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public int getNumeroCasa() {
        return numeroCasa;
    }

    public void setNumeroCasa(int numeroCasa) {
        this.numeroCasa = numeroCasa;
    }

    public int getQuartos() {
        return quartos;
    }

    public void setQuartos(int quartos) {
        this.quartos = quartos;
    }

    public float getM2() {
        return m2;
    }

    public void setM2(float m2) {
        this.m2 = m2;
    }

    public float getValor() {
        return valor;
    }

    public void setValor(float valor) {
        this.valor = valor;
    }

    public boolean isTrancado() {
        return trancado;
    }

    public void setTrancado(boolean trancado) {
        this.trancado = trancado;
    }

    public boolean isPortao() {
        return portao;
    }

    public void setPortao(boolean portao) {
        this.portao = portao;
    }

    public String getProprietario() {
        return proprietario;
    }

    public void setProprietario(String proprietario) {
        this.proprietario = proprietario;
    }
    public void status(){
        System.out.println("Valor da casa R$" + this.getValor() + " | Cor: " + this.getCor() + " | " +
                "Metros quadrados (m²): " + this.getM2() + " | Números de quartos: " + this.getQuartos() +
        "| A casa está trancada? " + this.isTrancado());
    }
}

