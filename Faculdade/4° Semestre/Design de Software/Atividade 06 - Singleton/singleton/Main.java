package singleton;
public class Main {
    public static void main(String[] args) {
        ControlAccessSingleton access1 = new ControlAccessSingleton().getInstance();
        access1.Access();


        ControlAccessSingleton access2 = new ControlAccessSingleton().getInstance();


        ControlAccessSingleton access3 = new ControlAccessSingleton().getInstance();

    }
}
