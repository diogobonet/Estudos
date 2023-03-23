package Faculdade.Aula01.Exercicios.Casa;

public class Proprietario {
    String nome;
    int idade;
    String CPF;
    int telefone;
    float salario;

    public Proprietario(String nome, int idade, String CPF, int telefone, float salario) {
        this.nome = nome;
        this.idade = idade;
        this.CPF = CPF;
        this.telefone = telefone;
        this.salario = salario;
    }

    public void status() {
        System.out.println("Nome: " + this.getNome() + " | Idade: " + this.getIdade() + " | CPF: "
        + this.getCPF() + " | Telefone: " + this.getTelefone() + " | Salário: " + this.getSalario());
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public String getCPF() {
        return CPF;
    }

    public void setCPF(String CPF) {
        this.CPF = CPF;
    }

    public int getTelefone() {
        return telefone;
    }

    public void setTelefone(int telefone) {
        this.telefone = telefone;
    }

    public float getSalario() {
        return salario;
    }

    public void setSalario(float salario) {
        this.salario = salario;
    }
}
