public class BankLoan {
    double loanValue;
    double minimumValue = 1000;
    boolean loanStatus;

    public BankLoan(double loanValue, double minimumValue, boolean loanStatus) {
        this.loanValue = loanValue;
        this.minimumValue = minimumValue;
        this.loanStatus = loanStatus;
    }
}
