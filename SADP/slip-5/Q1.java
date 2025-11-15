import java.util.*;

class EnumerationIteratorAdapter implements Iterator<Object> {

    private Enumeration<?> enumeration;

    public EnumerationIteratorAdapter(Enumeration<?> enumeration) {
        this.enumeration = enumeration;
    }

    @Override
    public boolean hasNext() {
        return enumeration.hasMoreElements();
    }

    @Override
    public Object next() {
        return enumeration.nextElement();
    }
}

public class Q1 {
    public static void main(String[] args) {
        Vector<String> vector = new Vector<>();
        
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter elements (type 'exit' to finish):");
        while (true) {
            String input = scanner.nextLine();
            if (input.equalsIgnoreCase("exit")) {
                break; 
            }
            vector.add(input);
        }
        scanner.close();
        
        Enumeration<String> enumeration = vector.elements();

        Iterator<Object> iterator = new EnumerationIteratorAdapter(enumeration);

        System.out.println("Elements in the vector:");
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}