import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class Lines {
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
