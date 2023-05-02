import java.util.Date;
public class Pessoa {
    private String nome;
    private String cpf;
    private Date dt;
    public Pessoa(String nome, String cpf, Date dt) {
        this.nome = nome;
        this.cpf = cpf;
        this.dt = dt;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public Date getDt() {
        return dt;
    }

    public void setDt(Date dt) {
        this.dt = dt;
    }
}
