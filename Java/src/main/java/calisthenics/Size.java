package calisthenics;

import java.util.function.UnaryOperator;

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

    public <T> T repeat(T identity, UnaryOperator<T> code) { // NOPMD OneLevelOfIntention - don't know how to do it otherwise?
        T current = identity;
        for (int i = 2; i <= count; i++) {
            current = code.apply(current);
        }
        return current;
    }

}
