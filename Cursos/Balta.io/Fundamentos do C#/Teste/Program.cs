using System; // Importação 

/* O USO DO SYSTEM NÃPO É OBRIGATORIO POIS ELE JÁ É IMPLICITO PELO SDK E RUNTIME*/

namespace Teste
{
    class Program {
        static void Main(string[] args) {
            // Variaveis
            int idade = 0; // Inicia com 0
            Console.WriteLine(idade);
            // int idade = 15;
            //var idade = 15;

            // Constante (GERALMENTE O IDENTIFICADOR É EM MAISUCULO)
            const int IDADE_MINIMA = 18;
            Console.Write(IDADE_MINIMA);

            /* TIPOS PRIMITIVOS DE DADOS */
            
            // BYTE (8-BIT) de 0-255
            // sbyte -128-127

            byte meuByte = 254;
            sbyte meuByte = -127;


            /* NÚMEROS INTEIROS 
            
            SHORT (16 bits)

            INT (32 bits)

            LONG (64 bits)
            
            USHORT, UINT, ULONG (Somente números inteiros)
            */

        }
    }
}