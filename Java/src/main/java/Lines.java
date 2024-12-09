import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class Lines implements Iterable<Line> {
    // First Order Collection

    private final List<Line> lines = new ArrayList<>();

    public Lines(Line... lines) {
        this.lines.addAll(Arrays.asList(lines));
    }

    public Lines(List<Line> lines) {
        this.lines.addAll(lines);
    }

    public void add(Line line) {
        lines.add(line);
    }

    public Lines append(Lines other) {
        lines.addAll(other.lines);
        return this;
    }

    public Lines join(Lines other) {
        return join(this.iterator(), other.iterator());
    }

    private Lines join(Iterator<Line> values, Iterator<Line> otherValues) {
        Lines result = new Lines();

        while (values.hasNext() && otherValues.hasNext()) {
            Line next = values.next();
            Line otherNext = otherValues.next();
            Line joinedLine = Line.join(next, otherNext);
            result.add(joinedLine);
        }

        return result;
    }

    @Override
    public Iterator<Line> iterator() {
        return lines.iterator();
    }

    @Override
    public boolean equals(Object other) {
        if (!(other instanceof Lines)) {
            return false;
        }
        Lines that = (Lines) other;
        return Objects.equals(lines, that.lines);
    }

    @Override
    public int hashCode() {
        // not needed
        return Objects.hash(lines);
    }

    @Override
    public String toString() {
        return "Lines\n" + lines.stream(). // NOPMD fluent interface
                map(Line::toString). //
                collect(Collectors.joining("\n"));
    }

}
