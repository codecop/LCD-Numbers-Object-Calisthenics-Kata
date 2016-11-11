package calisthenics;

import static java.util.stream.Collectors.joining;

import java.util.Iterator;
import java.util.List;
import java.util.stream.Stream;

public class Lcd {

    private final Size size;
    private final Templates template = new Templates();

    public Lcd() {
        this(Size.defaultSize());
    }

    public Lcd(Size size) {
        this.size = size;
    }

    public String format(int number) { // NO PMD - Primitive Obsession is public API
        String cr = "\n";
        return expandedNumber(number).collect(joining(cr)) + cr; // NOPMD LoD is too strict but only one dot.
    }

    private Stream<String> expandedNumber(int number) { // NOPMD OneLevelOfIntention - don't know how to do it otherwise?
        if (number < 10) {
            return expandedDigit(number);
        }
        return append(number / 10, number % 10);
    }

    private Stream<String> expandedDigit(int number) {
        List<String> digit = template.digit(number);
        expandY(digit);
        return expandX(digit);
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

    private Stream<String> append(int leftDigit, int rightDigit) {
        Stream<String> left = expandedNumber(leftDigit);
        Iterator<String> right = expandedDigit(rightDigit).iterator(); // NOPMD LoD is too strict but only one dot.
        return left.map(line -> line + right.next()); // NOPMD LoD is too strict but only one dot.
    }

}
