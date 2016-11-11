package calisthenics;

import static java.util.stream.Collectors.joining;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Lcd {

    private final Size size;

    public Lcd() {
        this(Size.defaultSize());
    }

    public Lcd(Size size) {
        this.size = size;
    }

    public String format(int number) { // NO PMD - Primitive Obsession is public API
        if (number < 10) {
            List<String> original = templateFor(number);
            List<String> template = new ArrayList<>(original);
            
            expandY(template);
            
            String cr = "\n";
            return template. // NOPMD? LoD Stream is same type & pattern is like that
                    stream(). //
                    map(this::expandX). //
                    collect(joining(cr)) + cr;
        }
        
        List<String> original = templateFor(number / 10);
        List<String> template = new ArrayList<>(original);
        Iterator<String> second = templateFor(number % 10).iterator();
        template = template.stream().map(line -> line + second.next()).collect(Collectors.toList());
        expandY(template);
        
        String cr = "\n";
        return template. // NOPMD? LoD Stream is same type & pattern is like that
                stream(). //
                map(this::expandX). //
                collect(joining(cr)) + cr;
    }

    private List<String> templateFor(int number) {
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
