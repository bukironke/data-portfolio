using System;

class Program {
    static void Main() {
        Random random = new Random();
        int secretNumber = random.Next(1, 101);
        int attempts = 0;
        int guess = 0;

        Console.WriteLine("Welcome to the Number Guessing Game!");
        Console.WriteLine("I'm thinking of a number between 1 and 100.");

        while (guess != secretNumber) {
            Console.Write("Enter your guess: ");
            guess = int.Parse(Console.ReadLine());
            attempts++;

            if (guess < secretNumber)
                Console.WriteLine("Too low! Try again.");
            else if (guess > secretNumber)
                Console.WriteLine("Too high! Try again.");
        }

        Console.WriteLine($"Congratulations! You guessed the number {secretNumber} in {attempts} attempts.");
    }
}
