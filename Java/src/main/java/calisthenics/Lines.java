package calisthenics;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Stream;

public class Lines {

    private final List<String> lines;

    public Lines(List<String> lines) {
        this.lines = new ArrayList<>(lines);
    }

    public Lines(Stream<String> lines) {
        this(lines.collect(toList()));
    }

    public void duplicate(int index) {
        lines.add(index, lines.get(index));
    }

    public Lines map(Function<String, String> mapper) {
        Stream<String> newLines = stream().map(mapper);
        return new Lines(newLines);
    }

    private Stream<String> stream() {
        return lines.stream();
    }

    public Lines join(Lines other) {
        Iterator<String> right = other.lines.iterator();
        return map(line -> line + right.next());
        // NOPMD LoD is too strict but only one dot.
    }

    public String join(String sep) {
        return stream().collect(joining(sep)) + sep;
    }

}
