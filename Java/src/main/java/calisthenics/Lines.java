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

    public void duplicate(int index) { // NOPMD PrimitiveObsession - but is an index
        lines.add(index, lines.get(index));
    }

    public Lines map(Function<String, String> mapper) {
        Stream<String> newLines = stream().map(mapper); // NOPMD LoD is too strict for Streams - still only one dot.
        return new Lines(newLines);
    }

    private Stream<String> stream() {
        return lines.stream();
    }

    public Lines join(Lines other) {
        Iterator<String> right = other.lines.iterator(); // NOPMD LoD is too strict for Streams - still only one dot.
        return map(line -> line + right.next());
    }

    public String join() {
        String cr = "\n";
        return stream().collect(joining(cr)) + cr; // NOPMD LoD is too strict for Streams - still only one dot.
    }

}
