package PBL.PBL05;

// O Temporario é uma classe apenas para basear o horista e o mensalista, tendo que ser abstrata
public abstract class Temporario extends Funcionario {

    // Definindo os atributos
    protected int tempo_meses;
    // Construtor da classe Temporario
    public Temporario(String nome, String funcao, int tempo_meses) {
        super(nome, funcao); // Construtor da classe Funcionario
        this.tempo_meses = tempo_meses; // Atributo da propria classe Temporario
    }
}
