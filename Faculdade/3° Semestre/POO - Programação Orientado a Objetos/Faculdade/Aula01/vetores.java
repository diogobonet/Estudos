package Faculdade.Aula01;

import java.util.Arrays;

public class vetores {
    public static void main(String[] args) {
       int [] primo = new int[7];

       primo[0] = 1;
       primo[1] = 2;
       primo[2] = 3;

       int i = 0;
       while(i < primo.length) {
           System.out.println(primo[i]);
           i++;
       }

       String[ ] carros = new String[10];
       carros[0] = "Ferrari 867";
       carros[1] = "F1-75";
       carros[2] = "F1-125";

    }
}
