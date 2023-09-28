public class User {
    public static void main(String[] args) {
        BankFacade bank = new BankFacade();
        bank.addMoney(50);
        bank.addMoney(2000);
        bank.consultValue();
        bank.loanRequest(true, 500000);
    }
}
