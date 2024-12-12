package print;

import util.Joinable;

public class Line implements Joinable<Line> {
    // Value Object

    private final String characters;

    public Line(String characters) {
        this.characters = characters;
    }

    @Override
    public Line join(Line other) {
        // real logic
        return new Line(characters + other.characters);
    }

    @Override
    public boolean equals(Object other) {
        // this is only needed for assertEquals in unit tests.
        if (!(other instanceof Line)) {
            return false;
        }
        Line that = (Line) other;
        return characters.equals(that.characters);
    }

}
