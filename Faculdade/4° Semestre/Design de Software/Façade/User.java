public class Main {
    public static void main(String[] args) {
        BankFacade bank = new BankFacade();
        bank.addMoney(50);
        bank.addMoney(500);
        bank.consultValue();
        bank.loanRequest(true, 5000);

        User user1 = new User("Diogo", 0, 0);
        user1.bankFacade.addMoney(50);
    }
}
