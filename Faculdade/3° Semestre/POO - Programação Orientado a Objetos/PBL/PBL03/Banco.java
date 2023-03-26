public class Banco {
    public static void main(String[] args) {
        Cliente c1 = new Cliente("Jandira Silva", 2500.00f);
        Cliente c2 = new Cliente("Sandra Rodrigues", 1800.00f);
        Cliente c3 = new Cliente("Luciana Teixeira", 5000.00f);
        c1.status();
        c2.status();
        c3.status();
        System.out.println("===========================================");
        c1.retirar(1000.00f);
        c1.status();
        System.out.println("===========================================");
        c2.retirar(2000.00f);
        c2.status();
        c2.depositar(500.00f);
        c2.retirar(2000.00f);
        c2.status();
        System.out.println("===========================================");
        c3.depositar(1000.00f);
        c3.status();
    }
}
