public class Size {

    private final int value;

    public Size(int value) {
        this.value = value;
    }

    @Override
    public boolean equals(Object other) {
        if (!(other instanceof Size)) {
            return false;
        }
        Size that = (Size) other;
        return value == that.value;
    }

    @Override
    public int hashCode() {
        return value;
    }

    @Override
    public String toString() {
        return "Size [" + value + ']';
    }

}
