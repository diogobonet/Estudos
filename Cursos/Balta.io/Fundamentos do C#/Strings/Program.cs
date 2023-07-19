using System;

namespace Strings
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
             * Guids
             * Global Unique Identifier
             */

            var id = Guid.NewGuid(); // Gera um ID novo
            id.ToString();

            //var id = Guid.NewGuid("bbf1fc12-3c57-4913-87ba-47b035d38184");
             // Ele inicializa um identificador com 0
            Console.WriteLine(id);

            /*
             * Interpolação de Strings
             * 
             */

            var price = 10.2;
            // var texto = "O preço do produto é " + price + "apenas na promoção!"; // Concatenação


            //var texto = string.Format("O preço do produto é {0}, apenas na promoção", price); // String.Format

            var texto = $@"O preço do produto é {price}, apenas na promoção!";
            Console.WriteLine(texto);

            /*
             * Comparação de Texto
             */

            var textando = "Testando";
            Console.WriteLine(textando.CompareTo("Testando")); // Retorna um inteiro, se for "0" é igual, se for
            // "1" 
            var texto1 = "Vamos fazer teste do que hoje?";
            Console.WriteLine(texto1.Contains("teste"));
            Console.WriteLine(texto1.Contains("Teste"));

            if (texto1.Contains("teste") == true)
            {
                Console.WriteLine("É verdadeiro!");
            } else
            {
                Console.WriteLine("É falso!");
            }

            /*
             * StartsWith ou EndsWith
             */
            var texto2 = "Este texto é um teste!";
            Console.WriteLine(texto2.StartsWith("Este"));

            Console.WriteLine(texto2.EndsWith("teste!"));

            /* 
             * Equals
             */
            Console.WriteLine(texto2.Equals("Este texto é um teste!")); // True
            Console.WriteLine(texto2.Equals("este texto é um teste")); // False
            Console.WriteLine(texto2.Equals("este texto é um teste!", StringComparison.OrdinalIgnoreCase)); //True, pq
            // ele ignora os casos de letras minusculas ou maiusculas

            /*
             * IndexOf
             */
            Console.WriteLine(texto2.IndexOf("é"));
            Console.WriteLine(texto2.IndexOf("um"));
            Console.WriteLine(texto2.LastIndexOf("s"));

            /*
             * Métodos Adicionais
             */
            Console.WriteLine(texto.ToLower()); // Tudo para letra minuscula
            Console.WriteLine(texto.ToUpper());
            Console.WriteLine(texto.Insert(5, "AQUI "));
            Console.WriteLine(texto.Remove(5, 5));
            Console.WriteLine(texto.Length);
        }
    }
}