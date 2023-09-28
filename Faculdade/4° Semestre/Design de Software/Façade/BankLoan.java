public class BankLoan {
    double loanValue;
    public static double minimumValue;
    boolean loanStatus;

    public BankLoan(double loanValue, double minimumValue, boolean loanStatus) {
        this.loanValue = loanValue;
        this.minimumValue = minimumValue;
        this.loanStatus = loanStatus;
    }
}
