public class BankFacade {
    private CurrentAccount currentAccount;
    private BankLoan bankLoan;

    public void addMoney(float value) {
        CurrentAccount.currentValue += value;
        CurrentAccount.totalValue += value;
        System.out.println("R$" + CurrentAccount.currentValue + " foi adicionado a sua conta!");
    }

    public void consultValue() {
        System.out.println("Sua conta possui: R$" + CurrentAccount.currentValue);
    }

    public void loanRequest(boolean status, double value) {
        loanMinimum(CurrentAccount.totalValue);
        if (BankLoan.minimumValue != 0)
            if (status && value >= BankLoan.minimumValue) {
                CurrentAccount.currentValue += value;
                CurrentAccount.totalValue += value;
                System.out.println("O seu emprestimo no valor de R$" + value + " foi APROVADO! E já está disponivel em sua conta");
            } else {
                System.out.println("O seu emprestimo no valor de R$" + value + " foi REPROVADO!");
            }
        else {
            System.out.println("Você não consegue pedir para realizar um emprestimo!");
        }
    }

    public void loanMinimum(double valueTotal) {
        if (valueTotal <= 1000) {
            BankLoan.minimumValue = 3000;
            System.out.println("Você consegue realizar um empréstimo de R$3.000");
        } else if (valueTotal >= 1000.1 && valueTotal <= 4999.99) {
            BankLoan.minimumValue = 5000;
            System.out.println("Você consegue realizar um empréstimo de R$5.000");
        } else if (valueTotal >= 5000 && valueTotal < 10000) {
            BankLoan.minimumValue = 10000;
            System.out.println("Você consegue realizar um empréstimo de R$10.000");
        } else if (valueTotal >= 10000) {
            BankLoan.minimumValue = 100000;
            System.out.println("Você consegue realizar um empréstimo de R$100.000");
        } else {
            System.out.println("Não é possível determinar o valor mínimo do empréstimo.");
        }
    }

}
