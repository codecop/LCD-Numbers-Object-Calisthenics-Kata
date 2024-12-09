public class Digit {
    // Value Object

    private final int value;

    public Digit(int value) {
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

}
