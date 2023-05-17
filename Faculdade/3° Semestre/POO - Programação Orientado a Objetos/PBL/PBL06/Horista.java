package PBL.PBL05;

public class Horista extends Temporario {
    // Definindo os atributos da classe
    private int horas_trabalhadas;
    private double valor_da_hora;

    // Construtor da classe Horista
    public Horista(String nome, String funcao, int tempo_meses, int horas_trabalhadas, double valor_da_hora) {
        // Atributos do contrutor da classe Temporario
        super(nome, funcao, tempo_meses);
        // Atributos da propria classe filha
        this.horas_trabalhadas = horas_trabalhadas;
        this.valor_da_hora = valor_da_hora;
    }

    @Override // Sobreescrevendo o método abstrato da classe Funcionario
    public String gerar_contra_cheque() {
        double salario = horas_trabalhadas * valor_da_hora; // Calculando o salário
        // Retornando o contra-cheque do Horista
        return ("Contra-cheque de: " + nome +
                "\nFunção: " + funcao +
                "\nHoras Trabalhadas: " + horas_trabalhadas +
                "\nValor da Hora: " + valor_da_hora  +
                "\nTempo em Meses: " + tempo_meses +
                "\nPagamento: " + salario);
    }
}
