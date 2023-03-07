package Aula05;

public class Banco {
    public int numConta;
    protected String tipo;
    private String dono;
    private float saldo;
    private boolean status;

    public Banco(int n, String d, float s, boolean st) {
        this.setNumConta(n);
        this.setDono(d);
        this.setSaldo(s);
        this.setStatus(st);
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

}
