import java.util.Arrays;
import java.util.stream.Collectors;

public class Line {

    private final String characters;

    public Line(String... parts) {
        this.characters = Arrays.asList(parts).stream().collect(Collectors.joining());
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
