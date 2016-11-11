package calisthenics;

import static java.util.stream.Collectors.joining;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

public class Lcd {

    private final Size size;

    public Lcd() {
        this(Size.defaultSize());
    }

    public Lcd(Size size) {
        this.size = size;
    }

    public String format(int number) { // NO PMD - Primitive Obsession is public API
        String cr = "\n";
        return expandedNumber(number).collect(joining(cr)) + cr;
    }

    private Stream<String> expandedNumber(int number) {
        if (number < 10) {
            return expandedDigit(number);
        }
        Iterator<String> right = expandedDigit(number % 10).iterator();
        Stream<String> left = expandedNumber(number / 10);
        return left.map(line -> line + right.next());
    }

    private Stream<String> expandedDigit(int number) {
        List<String> digit = new ArrayList<>(digit(number));
        expandY(digit);
        return expandX(digit);
    }

    private List<String> digit(int number) {
        // TODO make field
        Map<Integer, List<String>> templates = new HashMap<>();
        templates.put(1, Arrays.asList("   ", "  |", "   ", "  |", "   "));
        templates.put(2, Arrays.asList(" - ", "  |", " - ", "|  ", " - "));
        return templates.get(number);
    }

    private void expandY(List<String> template) {
        size.repeat(() -> template.add(3, template.get(3)));
        size.repeat(() -> template.add(1, template.get(1)));
    }

    private Stream<String> expandX(List<String> template) {
        return template. // NOPMD? LoD Stream is same type & pattern is like that
                stream(). //
                map(this::expandX);
    }

    private String expandX(String line) {
        StringBuilder buf = new StringBuilder();
        buf.append(line.substring(0, 1));
        String c = line.substring(1, 2);
        buf.append(c);
        size.repeat(() -> buf.append(c));
        buf.append(line.substring(2));
        return buf.toString();
    }
}
