package number;

public class Digit {
    // Value Object

    private final String value;

    public Digit(String value) {
        if (!value.matches("\\d")) {
            throw new IllegalArgumentException(value);
        }
        this.value = value;
    }

    public Digit(int value) {
        this(Integer.toString(value));
    }

    @Override
    public boolean equals(Object other) {
        if (!(other instanceof Digit)) {
            return false;
        }
        Digit that = (Digit) other;
        return value.equals(that.value);
    }

    @Override
    public int hashCode() {
        return value.hashCode();
    }

    @Override
    public String toString() {
        return "Digit '" + value + "'";
    }

}
