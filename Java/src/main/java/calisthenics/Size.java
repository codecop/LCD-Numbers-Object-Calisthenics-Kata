package calisthenics;

/**
 * Value object Size.
 */
public class Size {

    private int value;

    public static Size defaultSize() { // NOPMD factory method is no getter
        return new Size(1); 
        // TODO new Size(1) is ok, is not this.x or simply x.
    }

    public Size(int value) {
        this.value = value;
    }

    public int value() {
        return value;
    }

}
