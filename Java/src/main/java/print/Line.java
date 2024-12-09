package print;
import java.util.Arrays;
import java.util.stream.Collectors;

import util.Joinable;

public class Line implements Joinable<Line> {
    // Value Object

    private final String characters;

    public Line(String... parts) {
        this.characters = Arrays.asList(parts). //
                stream(). //
                collect(Collectors.joining());
    }

    @Override
    public Line join(Line other) {
        return new Line(characters + other.characters);
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
        // not needed
        return characters.hashCode();
    }

    @Override
    public String toString() {
        return "Line '" + characters + '\'';
    }

}
