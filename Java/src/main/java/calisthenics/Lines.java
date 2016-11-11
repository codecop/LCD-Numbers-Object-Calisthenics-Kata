package calisthenics;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Stream;

/**
 * First class collection of the lines making a single digit.
 */
public class Lines {

    private final List<String> lines;

    /* for Templates only */ Lines(List<String> lines) {
        this.lines = lines;
    }

    private Lines(Stream<String> lines) {
        this(lines.collect(toList()));
    }

    public Lines duplicate(int lineIndex) { // NOPMD PrimitiveObsession - is an index
        List<String> list = new ArrayList<>(lines);
        list.add(lineIndex, list.get(lineIndex));
        return new Lines(list);
    }

    public Lines map(Function<String, String> mapper) {
        Stream<String> newLines = stream().map(mapper); // NOPMD LoD is too strict for Streams - still only one dot.
        return new Lines(newLines);
    }

    private Stream<String> stream() {
        return lines.stream();
    }

    public Lines append(Lines other) {
        Iterator<String> right = other.lines.iterator(); // NOPMD LoD is too strict for Streams - still only one dot.
        return map(line -> line + right.next());
    }

    public String join() {
        String cr = "\n";
        return stream().collect(joining(cr)) + cr; // NOPMD LoD is too strict for Streams - still only one dot.
    }

}
