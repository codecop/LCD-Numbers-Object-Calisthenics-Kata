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
        Lcd lcd = new Lcd(2);
        String lines = lcd.format(1);
        assertEquals("    \n" + //
                "   |\n" + //
                "   |\n" + //
                "    \n" + //
                "   |\n" + //
                "   |\n" + //
                "    \n", lines);
    }

}
