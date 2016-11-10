package calisthenics;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class LcdTest {

    @Test
    public void shouldReturnOneSize1() {
        Lcd lcd = new Lcd();
        String lines = lcd.format(1);
        assertEquals("   \n" + //
                "  |\n" + //
                "   \n" + //
                "  |\n" + //
                "   \n", lines);
    }

    @Test
    public void shouldReturnOneSize2() {
        Lcd lcd = new Lcd(new Size(2));
        String lines = lcd.format(1);
        assertEquals("    \n" + //
                "   |\n" + //
                "   |\n" + //
                "    \n" + //
                "   |\n" + //
                "   |\n" + //
                "    \n", lines);
    }

    @Test
    public void shouldReturnTwoSize1() {
        Lcd lcd = new Lcd();
        String lines = lcd.format(2);
        assertEquals(" - \n" + //
                "  |\n" + //
                " - \n" + //
                "|  \n" + //
                " - \n", lines);
    }

    @Test
    public void shouldReturn12() {
        Lcd lcd = new Lcd();
        String lines = lcd.format(12);
        assertEquals("    - \n" + //
                "  |  |\n" + //
                "    - \n" + //
                "  ||  \n" + //
                "    - \n", lines);
    }
}
