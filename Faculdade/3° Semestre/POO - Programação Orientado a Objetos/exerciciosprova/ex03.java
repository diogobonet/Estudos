package exerciciosprova;
import java.util.Arrays;
import java.util.Scanner;

public class ex03 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Graus Celsius | C°: ");
        double celsius = teclado.nextDouble();

        double f = (celsius * 1.8f) + 32;
        double k = celsius + 273.15f;
        double Re = celsius * 8;
        double Ra = (celsius * 1.8) + 32 + 459.67;

        System.out.println("Celsius: " + celsius);

        System.out.println("Fahreinheit: " + f);
        System.out.println("Kelvin: " + k);
        System.out.println("Réaumur: " + Re);
        System.out.println("Rankine: " + Ra);


    }
}
