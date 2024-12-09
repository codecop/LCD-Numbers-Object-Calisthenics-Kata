public class Line {

    private final String characters;

    public Line(String corner, String middle) {
        this.characters = corner + middle + corner;
    }

    @Override
    public boolean equals(Object other) {
        if (!(other instanceof Line)) {
            return false;
        }
        Line that = (Line) other;
        return characters.equals(that.characters);
    }

    @Override
    public int hashCode() {
        return characters.hashCode();
    }

    @Override
    public String toString() {
        return "Line [" + characters + ']';
    }

}
