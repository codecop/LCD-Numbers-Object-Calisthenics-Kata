package lcd;

public class Size {
    // Value Object

    private final int value;

    public Size(int value) {
        this.value = value;
    }

    public void loop(Runnable block) {
        // real logic
        for (int i = 0; i < value; i++) {
            block.run();
        }
    }

}
