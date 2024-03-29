﻿using System; // Importação 

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
            string texto = "Olá, Mundo!";

            /* VAR 

            É possivel criar uma variavel sem definir especificamente o tipo de dados para a variavel mas assim que for definida um algum dado passado, ele assume o tipo do dado. E não é possivel mudar depois.
            
            */

            var idade3 = 25;
            int idade2 = 25;

            /* OBJECT 
            É um tipo qualquer pode ser qualquer coisa.
            */

            object velocidade;
            velocidade = 5;
            velocidade = 5.5;

            /* NULLABLE TYPES
            void = vazio (significado)

            null = também é vazio, diferente de 0 ou uma string vazia. utilizar null pode dar erro no código
            
            */

            int? vazio = null;
            Console.WriteLine(vazio);

            /* ALIAS
            int idade = 25; // Alias
            Int32 idade = 25; // Tipo
            
            */

            /*
            Conversão de Dados

            =====
            Conversão Implicita
            Não precisa informar o tipo de dados que serão convertidos

            Conversão explicita
            Informar o tipo de dados que serão convertidos
            
            */

            // Implicito
            int valor = 25;
            float outro = 25.8f;

            outro = valor;

            Console.WriteLine(outro);

            // Explicito
            int inteiro = 100;
            uint int22 = (uint)inteiro;

            /*
            Parse
            É usado para converter um caractere ou uma string para um tipo qualquer, caso haja compatibilidade
            */

            int inteiro23 = int.Parse("100");
            Console.WriteLine(inteiro23);

            /*
            Convert
            É uma classe/objeto que permite a gente converter uma string para um tipo
            */

            int inteiro25 = Convert.ToInt32("100");

            /* Operadores aritméticos 
            
            Soma => +
            Subtração => -
            Multiplicação => *
            Divisão => /
            
            */

            /* Operadores de atribuição
            
            x = 0;
            x += 5;
            x -= 1;
            x *= 10;
            x /= 2;

            */

            /*
            Operadores de Comparação
            Dá pra comparar qualquer tipo de dado (Numero, string, byte), só retorna booleano

            1. Igual: ==
            2. Diferente: !=
            3. Maior que: >
            4. Menor que <
            5. Maior ou igual que: >=
            6. Menor igual que: <=         
            */

            /*
            Operadores lógicos 
            Usado em operações condicionais, retorna sempre verdadeiro ou falso
            E - and
            Representado por: &&

            Ou - or
            Representado por: ||

            Negação - not
            Representado por: !
            */

            /* Estruturas condicionais
            
            if -> Utilizado para tomada de decisões
            else if ->
            else 
            */

            if (25 == 50) {
                Console.WriteLine("É igual");
            }

            else if (25 != 80) {
                Console.WriteLine("É diferente!");
            }

            else {
                Console.WriteLine("Entrou no ELSE!");
            }

            /*
            Switch
            É utilizada quando tem muitas decisões, executado em cascata, para manualmente a execução com o comando "break".
            Possui uma execução padrão, chamada de "default"
            */

            int valornormal3 = 3;
            switch (valornormal3) {
                case 1: Console.WriteLine("1"); break;
                case 2: Console.WriteLine("2"); break;
                default: Console.WriteLine("Padrão"); break;
            }

            /*
            Laços de Repetição (FOR)
            Executa uma determinada ação várias vezes
            O for exige 3 parametros:
            Contador
            Condição
            Incremento
            */

            int i;

            // Conta de 0 a 5
            for (i = 0; i <= 5; i++) {
                Console.WriteLine(i);
            }

            // Conta de 1 a 5
            for (i = 1; i <= 5; i++) {
                Console.WriteLine(i);
            }

            // Conta de 0 a 4
            for (i = 0; i < 5; i++) {
                Console.WriteLine(i);
            }

            // Conta de 5 a 0
            for (i = 5; i <= 0; i--) {
                Console.WriteLine(i);
            }

            /*
             Laços de Repetição (While)
             Enquanto uma condição for verdadeira, exige apenas uma condição, e checa a condição ANTES de executar
             */

            var valorinteiro27 = 0;
            while (valorinteiro27 <= 5)
            {
                Console.WriteLine(valorinteiro27);
                valorinteiro27++;
            }

            /*
             Laços de Repetição "Do"
             Realiza uma ação enquanto...
             Exige apenas uma condição no while, e checa a condição DEPOIS de executar
             */

            var valorinteiro28 = 0;
            do
            {
              Console.WriteLine(valorinteiro28);
              valorinteiro28++;
            } while (valorinteiro28 < 5);

            /*
             Funções ou Métodos
             Possui um retorno, um nome e parâmetros
             Começam sempre com maiúscula
            */

            MinhaFuncao("C# é brabo");
            string nome = RetornaNome("Diogo", "Sobezak");
            Console.WriteLine(nome);
            string pessoa = RetornaPessoa("Diogo", "Sobezak", 18);

            /*
            Tipos de Referencias e Tipos de Valor

            A memória é dividida em duas partes Heap e Stack;
            1. Heap armazena os dados
            2. Stack armazena as referencias para esses dados

            Qualquer tipo no .NET é tratado como:
            Tipos de Referencia (ReferenceType)
            Tipo de Valor (ValueType) -> Armazenam dados em um local da memória chamada Stack

            // ValueType
            Quando armazenamos um valor, a memória é alocada.
            
             */

            /*
             Structs
             Tipos de dados estruturados, o esqueleto
            Para criar novos tipos de dados
             */

            var product = new Product(1, "Mouse Gamer", 128.75f, EProductType.Product);
            var manutencao = new Product(2, "Elétrica", 500.00f, EProductType.Service);
            Console.WriteLine(product.Id.ToString());
            Console.WriteLine(product.Title);
            Console.WriteLine(product.Price);
            Console.WriteLine(product.PriceInDolar(4.81f));

            Console.WriteLine("===========");
            Console.WriteLine(manutencao.Id.ToString());
            Console.WriteLine(manutencao.Title);
            Console.WriteLine(manutencao.Price);
            Console.WriteLine(manutencao.Tipo);

            /*
             Enums
            Os enumeradores são inteiros que fornecem uma melhor visualização no código
             */

            /*
             * Guids
             * Global Unique Identifier
             */

            var id = Guid.NewGuid();
        }

        struct Product
        {
            // Propriedade
            public int Id;
            public string Title;
            public float Price;
            public EProductType Tipo;

            public Product(int id, string title, float price, EProductType type) {
                Id = id;
                Price = price;
                Title = title;
                Tipo = type;
            }

            // Métodos
            public float PriceInDolar(float dolar)
            {
                return Price * dolar;
            }
        }

        enum EProductType
        {
            Product = 1,
            Service = 2
        }

        static void MinhaFuncao(string parametros)
        {
            Console.WriteLine(parametros);
        }

        static string RetornaNome(string nome, string sobrenome)
        {
            return nome + sobrenome;
        }

        static string RetornaPessoa(
            string nome,
            string sobrenome,
            int idade
            )
        {
            return nome + "" + sobrenome + " tem " + idade.ToString();
        }
    }
}