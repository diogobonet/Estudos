package PBL.PBL04;

public class Pais {
    private Estado estado1;
    private Estado estado2;

    public Pais(Estado e1, Estado e2) {
        estado1 = e1;
        estado2 = e2;
    }

    int populacao() {
        return estado1.populacao() + estado2.populacao();
    }

    double area() {
        return estado1.area() + estado2.area();
    }

    double densidade() {
        return populacao() / area();
    }
}