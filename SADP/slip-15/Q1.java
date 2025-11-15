class Amplifier {
    public void on() { 
        System.out.println("Amplifier ON"); 
    }
    public void off() { 
        System.out.println("Amplifier OFF"); 
    }
    public void setSurroundSound() {
        System.out.println("Amplifier surround sound ON (5 speakers, 1 subwoofer)");
    }
    public void setVolume(int level) {
        System.out.println("Amplifier volume set to " + level);
    }
}

class DvdPlayer {
    public void on() { 
        System.out.println("DVD Player ON"); 
    }
    public void off() { 
        System.out.println("DVD Player OFF"); 
    }
    public void play(String movie) { 
        System.out.println("Playing movie: " + movie); 
    }
    public void stop() { 
        System.out.println("Stopping movie"); 
    }
    public void eject() { 
        System.out.println("DVD ejected"); 
    }
}

class Projector {
    public void on() { 
        System.out.println("Projector ON"); 
    }
    public void off() { 
        System.out.println("Projector OFF"); 
    }
    public void wideScreenMode() { 
        System.out.println("Projector in widescreen mode (16x9)"); 
    }
}

class TheaterLights {
    public void dim(int level) { 
        System.out.println("Lights dimmed to " + level + "%"); 
    }
    public void on() { 
        System.out.println("Lights ON"); 
    }
}

class Screen {
    public void down() { 
        System.out.println("Screen going down"); 
    }
    public void up() { 
        System.out.println("Screen going up"); 
    }
}

class PopcornPopper {
    public void on() {
        System.out.println("Popcorn Popper ON"); 
    }
    public void off() { 
        System.out.println("Popcorn Popper OFF"); 
    }
    public void pop() { 
        System.out.println("Popping popcorn!"); 
    }
}

// Facade
class HomeTheaterFacade {
    private Amplifier amp;
    private DvdPlayer dvd;
    private Projector projector;
    private TheaterLights lights;
    private Screen screen;
    private PopcornPopper popper;

    public HomeTheaterFacade(Amplifier amp, DvdPlayer dvd, Projector projector,
                             TheaterLights lights, Screen screen, PopcornPopper popper) {
        this.amp = amp;
        this.dvd = dvd;
        this.projector = projector;
        this.lights = lights;
        this.screen = screen;
        this.popper = popper;
    }

    public void watchMovie(String movie) {
        System.out.println("\n--- Get ready to watch a movie ---");
        popper.on(); popper.pop();
        lights.dim(10);
        screen.down();
        projector.on(); projector.wideScreenMode();
        amp.on(); amp.setSurroundSound(); amp.setVolume(5);
        dvd.on(); dvd.play(movie);
    }

    public void endMovie() {
        System.out.println("\n--- Shutting movie theater down ---");
        popper.off();
        lights.on();
        screen.up();
        projector.off();
        amp.off();
        dvd.stop(); dvd.eject(); dvd.off();
    }
}

// Client
public class Q1 {
    public static void main(String[] args) {
        // Create subsystems
        Amplifier amp = new Amplifier();
        DvdPlayer dvd = new DvdPlayer();
        Projector projector = new Projector();
        TheaterLights lights = new TheaterLights();
        Screen screen = new Screen();
        PopcornPopper popper = new PopcornPopper();

        // Create Facade
        HomeTheaterFacade homeTheater = new HomeTheaterFacade(
                amp, dvd, projector, lights, screen, popper
        );

        // Client uses simple methods
        homeTheater.watchMovie("Avengers: Endgame");
        homeTheater.endMovie();
    }
}

