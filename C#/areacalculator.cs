using System;

class Program {
    static void Main() {
        Console.WriteLine("Choose a shape (circle, square, rectangle):");
        string shape = Console.ReadLine();

        double area = 0;

        switch (shape.ToLower()) {
            case "circle":
                Console.Write("Enter the radius: ");
                double radius = double.Parse(Console.ReadLine());
                area = Math.PI * radius * radius;
                break;
            case "square":
                Console.Write("Enter the side length: ");
                double side = double.Parse(Console.ReadLine());
                area = side * side;
                break;
            case "rectangle":
                Console.Write("Enter the length: ");
                double length = double.Parse(Console.ReadLine());
                Console.Write("Enter the width: ");
                double width = double.Parse(Console.ReadLine());
                area = length * width;
                break;
            default:
                Console.WriteLine("Invalid shape.");
                break;
        }

        Console.WriteLine($"The area of the {shape} is: {area}");
    }
}
