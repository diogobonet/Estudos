package PBL.PBL05;

public class Concursado extends Funcionario  {
    // Definindo os atributos
    protected int ano_ingresso;
    protected double salario_mensal;

    // Construtor da Classe Concursado
    public Concursado(String nome, String funcao, int ano_ingresso, double salario_mensal) {
        // Atributos do contrutor da classe Funcionário
        super(nome, funcao);
        // Atributos da propria classe filha
        this.ano_ingresso = ano_ingresso;
        this.salario_mensal = salario_mensal;
    }

    public String gerar_contra_cheque() {
        // Retornando o Contra Cheque do concursado
        return ("Contra-cheque de: " + nome +
                "\nFunção: " + funcao +
                "\nAno de ingresso: " + ano_ingresso +
                "\nSalário mensal: " + salario_mensal +
                "\nPagamento: " + salario_mensal);
    }
}