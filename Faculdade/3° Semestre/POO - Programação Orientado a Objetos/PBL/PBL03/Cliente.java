public class Cliente {
    private String cliente;
    private double saldo;

    public Cliente(String cliente, double saldo) {
        this.cliente = cliente;
        this.saldo = saldo;
    }

    public String getCliente() {
        return cliente;
    }

    public void setCliente(String cliente) {
        this.cliente = cliente;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public void depositar(double valor) {
        this.setSaldo(this.getSaldo() + valor);
    }
    public void retirar (double valor) {
        if (saldo > valor) {
            this.setSaldo(this.getSaldo() - valor);
        } else {
            System.out.println("Você não conseguiu retirar seu dinheiro, porque o valor é menor que o saldo que você possui na sua conta!");
        }

    }
    public void status() {
        System.out.println("Nome: " + this.getCliente());
        System.out.println("Saldo da Conta: " + this.getSaldo());
    }
}
