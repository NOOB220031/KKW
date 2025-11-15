/*
Write a JAVA Program to implement built-in support (java.util.Observable) Weather station
with members temperature, humidity, pressure and methods - mesurmentsChanged(),
setMesurment(), getTemperature(), getHumidity(), getPressure()
*/

import java.util.Observable;
import java.util.Observer;

// WeatherStation class that extends Observable
class WeatherStation extends Observable {
    private float temperature;
    private float humidity;
    private float pressure;

    // Method to set measurements and notify observers
    public void setMeasurements(float temperature, float humidity, float pressure) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.pressure = pressure;
        measurementsChanged();
    }

    // Method to notify observers of changes
    public void measurementsChanged() {
        setChanged(); // Marks the observable as having been changed
        notifyObservers(); // Notify all observers
    }

    // Getter methods for temperature, humidity, and pressure
    public float getTemperature() {
        return temperature;
    }

    public float getHumidity() {
        return humidity;
    }

    public float getPressure() {
        return pressure;
    }
}

// Display class that implements Observer
class Display implements Observer {
    @Override
    public void update(Observable o, Object arg) {
        if (o instanceof WeatherStation) {
            WeatherStation ws = (WeatherStation) o;
            System.out.println("Updated weather data: ");
            System.out.println("Temperature: " + ws.getTemperature());
            System.out.println("Humidity: " + ws.getHumidity());
            System.out.println("Pressure: " + ws.getPressure());
        }
    }
}

// Main class to test the WeatherStation
public class Q1 {
    public static void main(String[] args) {
        // Create weather station and display objects
        WeatherStation weatherStation = new WeatherStation();
        Display display = new Display();

        // Register the display as an observer
        weatherStation.addObserver(display);

        // Simulate new weather measurements
        weatherStation.setMeasurements(25.5f, 65.0f, 1013.1f);
        weatherStation.setMeasurements(30.0f, 70.0f, 1012.5f);
    }
}
