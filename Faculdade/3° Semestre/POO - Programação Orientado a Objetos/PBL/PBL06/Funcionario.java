package PBL.PBL05;

public abstract class Funcionario {
    // Definindo os atributos
    protected String nome;
    protected String funcao;

    // Construtor da classe Funcionario
    public Funcionario (String nome, String funcao) {
        this.nome = nome;
        this.funcao = funcao;
    }

    // Esse método é abstrato pois como a classe funcionário é a classe mãe,
    // ela implementa para todas as classes filhas
    abstract public String gerar_contra_cheque();
}
