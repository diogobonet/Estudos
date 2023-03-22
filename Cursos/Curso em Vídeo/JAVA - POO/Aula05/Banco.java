package Aula05;

public class Banco {
    public int numConta;
    protected String tipo;
    private String dono;
    private float saldo;
    private boolean status;

    public Banco(int n, String d) {
        this.setNumConta(n);
        this.setDono(d);
    }
    public int getNumConta(){
        return this.numConta;
    }
    public void setNumConta(int n){
        this.numConta = n;
    }

    public String getTipo() {
        return this.tipo;
    }

    public void setTipo(String t){
        this.tipo = t;
    }

    public String getDono() {
        return this.dono;
    }

    public void setDono(String d){
        this.dono = d;
    }

    public float getSaldo() {
        return this.saldo;
    }

    public void setSaldo(float s){
        this.saldo = s;
    }
    public boolean getStatus() {
        return this.status;
    }

    public void setStatus(boolean st){
        this.status = st;
    }

    public void status(){
        System.out.println("Nome do dono da conta: " + this.dono);
        System.out.println("Número da conta: " + this.numConta);
        System.out.println("Tipo da conta: " + this.tipo);
        System.out.println("Saldo da conta: " + this.saldo);
        System.out.println("Status da conta: " + this.status);
    }

    public void abrirConta(String t) {
        this.setTipo(t);
        this.setStatus(true);
        if (t == "CC") {
            this.setSaldo(50);
        } if (t == "CP") {
            this.setSaldo(150);
        } else {
            System.out.println("Você não pode criar uma conta" + t + "pois está conta não existe!");
        }
    }

    public void fecharConta() {
        if (this.saldo > 0) {
            System.out.println("Conta com dinheiro!");
        } else if (this.saldo < 0) {
            System.out.println("Conta em débito!");
        } else {
            this.setStatus(false);
        }
    }

    public void depositar(float v) {
       if (getStatus() == true) {
            this.setSaldo(this.getSaldo() + v);
            System.out.println("Deposito concluido com sucesso na conta de " + this.getDono());
       }
        
        else if (getStatus() == false) {
           System.out.println("Você não pode depositar, pois sua conta está fechada!");
       }
    }

    public void sacar(float v) {
        if (getStatus() == true && saldo > 0) {
            this.setSaldo(this.getSaldo() - v);
            System.out.println("Dinheiro sacado com sucesso!Você agora possui R$" + this.getSaldo());
        }
        else if (getStatus() == true && saldo <= 0) {
            System.out.println("Não foi possivel sacar pois você não possui dinheiro na sua conta!");

        } else if (getStatus() == false) {
            System.out.println("Não foi possivel sacar o dinheiro, pois sua conta está FECHADA!");
        }
    }

    public void pagarMensal() {
        float v = 0;
        if (this.getTipo() == "CC") {
            v = 12;
        } else if (this.getTipo() == "CP") {
            v = 20;
        }
        if (getStatus()) {
            this.setSaldo(this.getSaldo() - v);
            System.out.println(this.getDono() + ", a sua mensalidade foi paga com sucesso! Seu saldo atual na conta é de R$" + this.getSaldo());
        } else {
            System.out.println("Sua conta está fechada portanto não poderá pagar mensalmente o plano do banco!");
        }
    }

}
