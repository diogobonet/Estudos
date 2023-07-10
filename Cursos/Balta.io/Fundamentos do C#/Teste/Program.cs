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

            // ===============================================================

            /* TIPOS PRIMITIVOS DE DADOS */
            
            // BYTE (8-BIT) de 0-255
            // sbyte -128-127

            byte meuByte = 254;
            sbyte meuByte2 = -127;

            // ===============================================================  

            /* NÚMEROS INTEIROS 
            
            SHORT (16 bits)

            INT (32 bits)

            LONG (64 bits)
            
            USHORT, UINT, ULONG (Somente números inteiros)
            */

            // ===============================================================

            /*
            NÚMEROS REAIS
            
            FLOAT (32 bits) toda a vez que for float usar o "f" no final

            DOUBLE (64 bits) não exige nada!

            DECIMAL (128 bits) toda a vez que for decimal usar o "m" no final
            
            */

            float men = 2.500f;

            // ===============================================================

            /*
            
            Boolean (8-bit)
            Apenas true or false

            */

            bool usuarioCadastrado = true;
            bool pagamentoRecebido = false;

            // ===============================================================

            /*     
            CHAR (unicode) tem que ser definida com aspas simples
            */

            char primeiraLetra = 'D';


            /*
            String armazena uma cadeia de caracteres e tem que ser definida com aspas duplas
            */
        }
    }
}