package calisthenics;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class LcdTest {

    @Test
    public void shouldReturnOne() {
        Lcd lcd = new Lcd();
        String lines = lcd.format(1);
        assertEquals("   \n  |\n   \n  |\n   \n", lines);
    }

}
