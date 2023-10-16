package Aula07;

public class main {
    public static void main(String[]args) {
        Lutador l1 = new Lutador("Pretty Boy", "França", 31, 1.75f, 68.9f, 11,2, 1);
        l1.apresentar();
        l1.status();
        Lutador l2 = new Lutador("Putscript", "Brasil", 29, 1.68f, 57.8f, 14, 2, 3);
        l2.ganharLuta();
        l2.apresentar();
        l2.status();
    }

}