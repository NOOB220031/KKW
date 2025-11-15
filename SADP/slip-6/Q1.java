interface Command {
    public void execute();
}

class Light {
    public void on(){
        System.out.println("Light is on");
    }
    public void off() {
        System.out.println("Light is off");
    }
}

class LightOnCommand implements Command {
    private Light light;
    public LightOnCommand(Light light ) {
        this.light = light;
    }
    public void execute() {
        light.on();
    }
}

class LightOffCommand implements Command {
    private Light light;
    
    public LightOffCommand(Light light) {
        this.light = light;
    }
    public void execute() {
        light.off();
    }
}
class RemoteControl {
    private Command command;
    public RemoteControl() {}
    
    public void setCommand(Command command) {
        this.command = command;
    }
    
    public void buttonWasPressed() {
        command.execute();
    }
}

public class Q1 {
    public static void main(String[] args) {
        
        Light light = new Light();
        
        LightOnCommand lightOn = new LightOnCommand(light);
        LightOffCommand lightOff = new LightOffCommand(light);
            
        RemoteControl remote = new RemoteControl();
    
        remote.setCommand(lightOn);
        remote.buttonWasPressed();
        
        remote.setCommand(lightOff);
        remote.buttonWasPressed();
    }
}
