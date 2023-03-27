package PBL.PBL04;

public class Estado {
    private Municipio municipio1;
    private Municipio municipio2;
    private Municipio municipio3;
    private Municipio municipio4;
    public Estado(Municipio m1, Municipio m2, Municipio m3, Municipio
            m4)
    {
        municipio1 = m1;
        municipio2 = m2;
        municipio3 = m3;
        municipio4 = m4;
    }
    public int populacao()
    {
        return municipio1.populacao() +
                municipio2.populacao() +
                municipio3.populacao() +
                municipio4.populacao();
    }
    public double area()
    {
        return municipio1.area() +
                municipio2.area() +
                municipio3.area() +
                municipio4.area();
    }
    double densidade() { return populacao() / area(); }
}