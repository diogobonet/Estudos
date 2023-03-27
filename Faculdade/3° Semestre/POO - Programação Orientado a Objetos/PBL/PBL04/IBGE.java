package PBL.PBL04;

public class IBGE {
    public static void main(String args[])
    {
        Municipio curitiba = new Municipio(2400, 400);
        Municipio guarapuava = new Municipio( 200, 100);
        Municipio londrina = new Municipio( 800, 300);
        Municipio maringa = new Municipio( 600, 200);
        Estado parana = new Estado(curitiba, guarapuava, londrina,
                maringa);
        Municipio salvador = new Municipio(3000, 400);
        Municipio juazeiro = new Municipio( 400, 100);
        Municipio ilheus = new Municipio(280, 200);
        Municipio itabuna = new Municipio( 320, 300);
        Estado bahia = new Estado(salvador, juazeiro, ilheus,
                itabuna);
        Pais brasil = new Pais(bahia, parana);
        System.out.println( curitiba.densidade() ); // quadro 1
        System.out.println( parana.densidade() ); // quadro 3
        System.out.println( bahia.area() ); // quadro 2
        System.out.println( brasil.populacao() ); // quadro 4
        System.out.println( brasil.densidade() ); // quadro 5
    }
}