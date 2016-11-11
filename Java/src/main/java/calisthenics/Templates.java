package calisthenics;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * First class collection of the templates, ie the string patterns.
 */
public class Templates {

    private final Map<Integer, Lines> templates = new HashMap<>();

    public Templates() {
        add(1, "   ", "  |", "   ", "  |", "   ");
        add(2, " - ", "  |", " - ", "|  ", " - ");
    }

    private void add(int index, String... lines) {
        templates.put(index, new Lines(Arrays.asList(lines)));
    }

    public Lines digit(int number) { // NOPMD - Primitive Obsession - this is a number here?
        return templates.get(number);
    }

}
