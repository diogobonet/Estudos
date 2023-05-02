import java.util.Date;
public class Funcionario extends Pessoa {
    private String email;
    private String conta;

    public Funcionario(String email, String conta, String nome, String cpf, Date dt){
        super(nome, cpf, dt);
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getConta() {
        return conta;
    }

    public void setConta(String conta) {
        this.conta = conta;
    }
}
