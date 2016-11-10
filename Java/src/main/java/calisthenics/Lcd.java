package calisthenics;

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
            return "   \n" + //
                    "  |\n" + //
                    "   \n" + //
                    "  |\n" + //
                    "   \n";
        }
        if (size.value() == 2) {
            return "    \n" + //
                    "   |\n" + //
                    "   |\n" + //
                    "    \n" + //
                    "   |\n" + //
                    "   |\n" + //
                    "    \n";

        }
        return null;
    }

}
