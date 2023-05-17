package PBL.PBL05;

public class Comissionado extends Concursado {
    // Definindo os atributos
    private double comissao;
    private String cargo;

    public Comissionado(String nome, String funcao, int ano_ingressado, double salario_mensal, double comissao,
                        String cargo) {
        // Atributos do contrutor da classe Concursando
        super(nome, funcao, ano_ingressado, salario_mensal);
        // Atributos da propria classe filha
        this.comissao = comissao;
        this.cargo = cargo;
    }

    @Override // Sobreescrevendo o método abstrato da classe Funcionario
    public String gerar_contra_cheque() {
        double pagamento = salario_mensal + comissao; // Pagamento do comissionado
        return ("Contra-cheque de: " + nome +
                "\nFunção: " + funcao +
                "\nAno de ingresso: " + ano_ingresso +
                "\nCargo: " + cargo  +
                "\nSalário mensal: " + salario_mensal +
                "\nComissão: " + comissao +
                "\nPagamento: " + pagamento);
    }
}
