//  Write a Java Program to implement Singleton pattern for multithreading.

class Singleton {
    private static Singleton instance;
    private Singleton() {
    }

    // Synchronized method to ensure thread safety
    public static synchronized Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }

    // Example method
    public void showMessage() {
        System.out.println("Singleton instance accessed by " + Thread.currentThread().getName());
    }
}

public class Q1 {
    public static void main(String[] args) {
        // Creating two threads that access the Singleton instance
        Thread t1 = new Thread(() -> {
            Singleton singleton = Singleton.getInstance();
            singleton.showMessage();
        });

        Thread t2 = new Thread(() -> {
            Singleton singleton = Singleton.getInstance();
            singleton.showMessage();

        });

        t1.start();
        t2.start();
    }
}
