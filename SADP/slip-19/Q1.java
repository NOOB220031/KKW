/*
Write a Java Program to implement Factory method for Pizza Store with
createPizza(), orderPizza(),prepare(), bake(), cut(), box(). Use this to create variety of
pizza’s like NyStyleCheesePizza, ChicagoStyleCheesePizzaetc.
*/

//Base Pizza class
abstract class Pizza {
    public void prepare() {
        System.out.println("Preparing " + this.getClass().getSimpleName());
    }

    public void bake() {
        System.out.println("Baking " + this.getClass().getSimpleName());
    }

    public void cut() {
        System.out.println("Cutting " + this.getClass().getSimpleName());
    }

    public void box() {
        System.out.println("Boxing " + this.getClass().getSimpleName());
    }
}

// NyStyleCheesePizza class
class NyStyleCheesePizza extends Pizza { }

// ChicagoStyleCheesePizza class
class ChicagoStyleCheesePizza extends Pizza { }

// PizzaStore class with the factory method
abstract class PizzaStore {
    // Factory Method: to be implemented by subclasses
    public abstract Pizza createPizza(String type);

    public Pizza orderPizza(String type) {
        Pizza pizza = createPizza(type); // Factory method call
        pizza.prepare();
        pizza.bake();
        pizza.cut();
        pizza.box();
        return pizza;
    }
}

// NyPizzaStore class implementing factory method
class NyPizzaStore extends PizzaStore {
    public Pizza createPizza(String type) {
        if (type.equals("cheese")) {
            return new NyStyleCheesePizza();
        }
        return null;
    }
}

// ChicagoPizzaStore class implementing factory method
class ChicagoPizzaStore extends PizzaStore {
    public Pizza createPizza(String type) {
        if (type.equals("cheese")) {
            return new ChicagoStyleCheesePizza();
        }
        return null;
    }
}

// Main class to test the program
public class Q1 {
    public static void main(String[] args) {
        PizzaStore nyStore = new NyPizzaStore();
        PizzaStore chicagoStore = new ChicagoPizzaStore();
        // Order pizzas from different stores
        nyStore.orderPizza("cheese");
        chicagoStore.orderPizza("cheese");
    }
}