import java.util.ArrayList;
import java.util.Scanner;

public class TodoList {
    public static void main(String[] args) {
        ArrayList<String> tasks = new ArrayList<>();
        Scanner input = new Scanner(System.in);

        System.out.println("Welcome to the To-Do List App!");

        while (true) {
            System.out.print("Enter a task (or 'quit' to exit): ");
            String task = input.nextLine();

            if (task.equals("quit")) {
                break;
            }

            tasks.add(task);
            System.out.println("Task added!");
        }

        System.out.println("Your To-Do List:");
        for (int i = 0; i < tasks.size(); i++) {
            System.out.println((i + 1) + ". " + tasks.get(i));
        }
    }
}
