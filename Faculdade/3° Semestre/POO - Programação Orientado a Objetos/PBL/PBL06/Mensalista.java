package PBL.PBL05;

// A Classe mensalista está herdando propriedades do Temporario
public class Mensalista extends Temporario {
    // Definindo os atributos
    private double salario_mensal;

    // Constutor do Mensalista
    public Mensalista(String nome, String funcao, int tempo_meses, double salario_mensal) {
        // Atributos do contrutor da classe Concursando
        super(nome, funcao, tempo_meses);
        // Atributos da propria classe filha
        this.salario_mensal = salario_mensal;
    }

    @Override // Sobreescrevendo o método abstrato da classe Funcionario
    public String gerar_contra_cheque() {
        // Essa função retorna o Contra-cheque do Mensalista
        return ("Contra-cheque de: " + nome +
                "\nFunção: " + funcao +
                "\nTempo em Meses: " + tempo_meses +
                "\nSalário Mensal: " + salario_mensal +
                "\nPagamento: " + salario_mensal);
    }
}
