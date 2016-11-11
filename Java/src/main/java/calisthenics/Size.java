package calisthenics;

/**
 * Value object for Bar Size. No Getter for the value!
 */
public class Size {

    private int count;

    public static Size defaultSize() { // NOPMD false positive - factory method is no getter
        return new Size(1);
        // TODO new Size(1) is ok, is not this.x or simply x.
    }

    public Size(int value) {
        this.count = value;
    }

    public void repeat(Runnable code) {
        for (int i = 2; i <= count; i++) {
            code.run();
        }
    }

}
