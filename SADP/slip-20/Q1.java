// Write a Java Program to implement I/O Decorator for converting uppercase letters to  lower case letters.

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class Q1 {
    public static void main(String[] args) throws IOException {
        // Take input from user
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter text: ");
        String input = sc.nextLine();

        // Convert the input to a stream and wrap it with a BufferedReader
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
        // Output stream with OutputStreamWriter to write to the console
        OutputStreamWriter writer = new OutputStreamWriter(System.out);

        int ch;
        // Read each character, convert to lowercase and write to output
        while ((ch = reader.read()) != -1) {
            writer.write(Character.toLowerCase(ch));
        }

        // Flush the writer to ensure output is displayed
        writer.flush();
        // Close resources
        reader.close();
        writer.close();
        sc.close();
    }
}