package calisthenics;

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
        if (size.value() == 1) {
            List<String> template = Arrays.asList("   ", "  |", "   ", "  |", "   ");
            return template.//
                    stream().//
                    collect(Collectors.joining("\n")) + "\n";
        }
        if (size.value() == 2) {
            List<String> template = Arrays.asList("   ", "  |", "  |", "   ", "  |", "  |", "   ");
            return template.//
                    stream().//
                    map(this::x).collect(Collectors.joining("\n")) + "\n";
        }
        return null;
    }

    private String x(String line) {
        StringBuilder buf = new StringBuilder(line.length() + size.value());
        buf.append(line.substring(0, 1));
        String c = line.substring(1, 2);
        for (int i = 1; i <= size.value(); i++) {
            buf.append(c);
        }
        buf.append(line.substring(2));
        return buf.toString();
    }
}
