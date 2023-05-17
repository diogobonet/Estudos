package PBL.PBL05;

import java.util.ArrayList;

public class Empresa {
    // Criando uma array para adicionar os funcionário
    private ArrayList<Funcionario> funcionarios = new ArrayList<>();
    private String nome;
    public Empresa(String nome) {
        this.nome = nome;
    }
    public void gerar_folha() {
        // Gera a folha para cada funcionario chamado na Iniciadora
        for (Funcionario f : funcionarios){
            System.out.println("=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
            System.out.println(f.gerar_contra_cheque());
        }
    }

    public void incluir(Funcionario f) {
        // Adiciona um funcionario a ArrayList da classe Empresa
        this.funcionarios.add(f);
    }
}
