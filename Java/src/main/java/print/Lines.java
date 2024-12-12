package print;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Objects;

public class Lines {
    // First Class Collection

    private final List<Line> lines = new ArrayList<>();

    public Lines(List<Line> lines) {
        this.lines.addAll(lines);
    }

    public void append(Lines other) {
        // real logic
        lines.addAll(other.lines);
    }

    public Lines join(Lines other) {
        // real logic
        List<Line> newLines = join(other.lines);
        return new Lines(newLines);
    }

    private List<Line> join(List<Line> other) {
        // delegate to elements
        List<Line> newLines = new ArrayList<>();

        Iterator<Line> otherIterator = other.iterator();
        for (Line thisline : lines) {
            Line otherLine = otherIterator.next();
            newLines.add(thisline.join(otherLine));
        }

        return newLines;
    }

    public void println() {
        // delegate to elements
        for (Line line : lines) {
            line.println();
        }
    }

    @Override
    public boolean equals(Object other) {
        // this is only needed for assertEquals in unit tests.
        if (!(other instanceof Lines)) {
            return false;
        }
        Lines that = (Lines) other;
        return Objects.equals(lines, that.lines);
    }

}
