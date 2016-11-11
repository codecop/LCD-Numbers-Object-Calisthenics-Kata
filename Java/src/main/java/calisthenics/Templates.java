package calisthenics;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Templates {

    private final Map<Integer, List<String>> templates = new HashMap<>();

    public Templates() {
        templates.put(1, Arrays.asList("   ", "  |", "   ", "  |", "   "));
        templates.put(2, Arrays.asList(" - ", "  |", " - ", "|  ", " - "));
    }

    public List<String> digit(int number) { // NOPMD - Primitive Obsession - this is a number here?
        return new ArrayList<>(templates.get(number));
    }

}
