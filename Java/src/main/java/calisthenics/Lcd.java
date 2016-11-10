package calisthenics;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
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
        List<String> template = new ArrayList<>(Arrays.asList("   ", "  |", "   ", "  |", "   "));
        expandY(template);
        return template.//
                stream().//
                map(this::expandX).//
                collect(Collectors.joining("\n")) + "\n";
    }

    private void expandY(List<String> template) {
        if (size.value() == 2) {
            template.add(3, template.get(3));
            template.add(1, template.get(1));
        }
    }

    private String expandX(String line) {
        StringBuilder buf = new StringBuilder(line.length() + size.value());
        buf.append(line.substring(0, 1));
        String c = line.substring(1, 2);
        repeat(buf, c);
        buf.append(line.substring(2));
        return buf.toString();
    }

    private void repeat(StringBuilder buf, String c) {
        for (int i = 1; i <= size.value(); i++) {
            buf.append(c);
        }
    }
}
