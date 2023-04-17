import java.util.Date;
public class Cliente extends Pessoa {
    private Date dt_criacao;
    public Cliente(Date dt_criacao, String nome, String cpf, Date dt){
        super(nome, cpf, dt);
        this.dt_criacao = dt;
    }

    public Date getDt_criacao() {
        return dt_criacao;
    }

    public void setDt_criacao(Date dt) {
        this.dt_criacao = dt;
    }
}
