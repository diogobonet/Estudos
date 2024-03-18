using System;

namespace Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Menu();
            }
        }

        static void Soma(double v1, double v2)
        {
            double resultado = v1 + v2;
            Console.WriteLine($"{v1} + {v2} = {resultado}");
        }

        static void Subtracao(double v1, double v2)
        {
            double resultado = v1 - v2;
            Console.WriteLine($"{v1} - {v2} = {resultado}");
        }

        static void Divisao(double v1, double v2)
        {
            double resultado = v1 / v2;
            Console.WriteLine($"{v1} / {v2} = {resultado}");
        }

        static void Multiplicacao(double v1, double v2)
        {
            double resultado = v1 * v2;
            Console.WriteLine($"{v1} * {v2} = {resultado}");
        }

        static void Menu()
        {
            Console.Clear();
            Console.WriteLine("Primeiro valor: ");
            double v1 = float.Parse(Console.ReadLine());

            Console.WriteLine("Segundo valor: ");
            double v2 = float.Parse(Console.ReadLine());

            Console.WriteLine("Qual operação deseja realizar?");
            Console.WriteLine("[1] - Soma");
            Console.WriteLine("[2] - Subtração");
            Console.WriteLine("[3] - Divisão");
            Console.WriteLine("[4] - Multiplicação");
            Console.WriteLine("[5] - Sair");
            int valor = int.Parse(Console.ReadLine());

            switch (valor) {
                case 1: 
                    Soma(v1, v2);
                    break;
                case 2: 
                    Subtracao(v1, v2);
                    break;
                case 3: 
                    Divisao(v1, v2);
                    break;
                case 4: 
                    Multiplicacao(v1, v2);
                    break;
                case 5:
                    System.Environment.Exit(0); break;
                default: Menu(); break;
            }
        }
    } 
}

/*
             * Console.
             * Possui várias funções
             * Write -> Escreve na tela
             * WriteLine -> Escreve na tela e pula uma linha
             * Read -> Ler
             * Read Key -> Ler um item
             * ReadLine -> Ler uma linha
             */