package calisthenics;

public class Lcd {

    private final int size;

    public Lcd() {
        this(1);
    }

    public Lcd(int size) {
        this.size = size;
    }

    public String format(int number) { // xNOPMD - Primitive Obsession is public API
        if (size == 1) {
            return "   \n" + //
                    "  |\n" + //
                    "   \n" + //
                    "  |\n" + //
                    "   \n";
        }
        if (size == 2) {
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
