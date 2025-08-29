// See https://aka.ms/new-console-template for more information
using System;
using System.Collections.Generic;
class crossword
{
    int xmax;
    int ymax;
    public crossword(string[] str, int xmax, int ymax)
    {
        this.xmax = xmax;
        this.ymax = ymax;
        init( str );
    }

    private bool isValid( char[] str)
    {
        foreach ( string item in str)
        {
            Console.WriteLine($"{item}");
        }
        return true;
    }

    private void Init(string[] str){
        
        foreach (string word in str)
        {
            //Console.WriteLine($"{IsValid(str)}");
            // Logic to add the word to the crossword grid would go here
            for (int i = 0; i < word.Length; i++)
            {
                Console.WriteLine($"{word[i]}");
            }
        }
    }
}


class Program
{
    static void Main(string[] args)
    {
        // Console.WriteLine("Welcome to the Crossword App!");
        // Initialize crossword or other logic here
        string[] sampleWords = { "hello", "world" };
        crossword myCrossword = new crossword(sampleWords, 10, 10);
        // Console.WriteLine("Crossword initialized with dimensions 10x10.");
    }
}