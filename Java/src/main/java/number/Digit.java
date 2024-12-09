package number;

public class Digit {
    // Value Object

    private final int value;

    public Digit(int value) {
        if (value < 0 || value > 9) {
            throw new IllegalArgumentException("" + value);
        }
        this.value = value;
    }

    @Override
    public boolean equals(Object other) {
        if (!(other instanceof Digit)) {
            return false;
        }
        Digit that = (Digit) other;
        return value == that.value;
    }

    @Override
    public int hashCode() {
        return value;
    }

    @Override
    public String toString() {
        return "Digit '" + value + "'";
    }

}
