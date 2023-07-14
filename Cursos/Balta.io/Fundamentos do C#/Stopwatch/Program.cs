using System;

namespace Stopwatch
{
    class Program
    {
        static void Main(string[] args)
        {
            Start(6);
        }

        static void Start(int time)
        {
            int currentTime = 0;

            while (currentTime != time) {
                Console.Clear();
                currentTime++;
                Console.WriteLine(currentTime);
                Thread.Sleep(1000);
            }
            Console.Clear();
            Console.WriteLine("Stopwatch finalizado");
            Menu();
        }

        static void Menu()
        {
            switch ()
            {

            }
         }
    }
}