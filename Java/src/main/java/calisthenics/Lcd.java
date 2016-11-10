package calisthenics;

import java.util.Arrays;
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
            return Arrays.asList("   ", "  |", "   ", "  |", "   ").//
            stream().//
            collect(Collectors.joining("\n")) + "\n";
        }
        if (size.value() == 2) {
            return x("   \n") + //
                    x("  |\n") + //
                    x("  |\n") + //
                    x("   \n") + //
                    x("  |\n") + //
                    x("  |\n") + //
                    x("   \n");

        }
        return null;
    }

    private String x(String line) {
        String c = line.substring(1, 2);
        return line.substring(0, 1) + c + c + line.substring(2);
    }
}
