package singleton;

public class ControlAccessSingleton {

    private static ControlAccessSingleton instance;

    public ControlAccessSingleton() {
    }

    public ControlAccessSingleton getInstance() {
        if (instance == null) {
            instance = new ControlAccessSingleton();
        }
        System.out.println("A new user was registered!");
        return instance;
    }

    public void Access() {
        System.out.println("We're accessing a Control Access system!");
    }
    public void AccessDenied() { instance = null; }
}
