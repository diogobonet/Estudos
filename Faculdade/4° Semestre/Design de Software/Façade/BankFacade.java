public class BankFacade {
    private CurrentAccount currentAccount;
    private BankLoan bankLoan;

    public void addMoney(float value) {
        CurrentAccount.currentValue += value;
        System.out.println("R$" + CurrentAccount.currentValue + " foi adicionado a sua conta!");
    }

    public void consultValue() {
        System.out.println("Sua conta possui: R$" + CurrentAccount.currentValue);
    }

    public void loanRequest(boolean status, double value) {
        if (status && value >= bankLoan.minimumValue) {
            CurrentAccount.currentValue += value;
            System.out.println("O seu emprestimo no valor de R$" + value + " foi APROVADO! E já está disponivel em sua conta");
        } else {
            System.out.println("O seu emprestimo no valor de R$" + value + " foi REPROVADO!");
        }
    }
}
