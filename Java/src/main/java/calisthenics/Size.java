package calisthenics;

/**
 * Value object Size.
 */
public class Size {

    private int value;

    public static Size defaultSize() {
        return new Size(1);
    }

    public Size(int value) {
        this.value = value;
    }

    public int value() {
        return value;
    }

}
