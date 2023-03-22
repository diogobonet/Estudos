package Faculdade.Aula01.Aula02;

public class Aula02 {
    public String nome;
    public int periodo;
    protected String email;
    public boolean matricula;

    public Aula02(String nome, String email, int periodo, boolean matricula) {
        this.nome = nome;

        this.email = email;

        this.periodo = periodo;

        this.matricula = matricula;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }


    public void setPeriodo(short periodo) {
        this.periodo = periodo;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public boolean isMatricula() {
        return matricula;
    }

    public void setMatricula(boolean matricula) {
        this.matricula = matricula;
    }

    public void matricula() {
        if (matricula == true){
            System.out.println("O aluno %s está matriculado");
        }
    }

    public void status() {
        System.out.println("Aluno: " + this.nome);
        System.out.println("Email: " + this.email);

    }
}


