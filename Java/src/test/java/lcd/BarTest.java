package lcd;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;

import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import print.Line;
import print.Lines;

class BarTest {

    void assertEqualsLine(String expected, Lines actual) {
        assertEquals(new Lines(Arrays.asList(new Line(expected))), actual);
    }

    @Nested
    class HoricontalLcdTest {

        @Test
        void shouldShowFilled() {
            Lcd horicontal = new HoricontalLcd(Led.ON);
            Lines lines = horicontal.scale(new Size(1));
            assertEqualsLine(" - ", lines);
        }

        @Test
        void shouldShowEmpty() {
            Lcd horicontal = new HoricontalLcd(Led.OFF);
            Lines lines = horicontal.scale(new Size(1));
            assertEqualsLine("   ", lines);
        }

        @Test
        void shouldScaleTwo() {
            Lcd horicontal = new HoricontalLcd(Led.ON);
            Lines lines = horicontal.scale(new Size(2));
            assertEqualsLine(" -- ", lines);
        }

    }

    @Nested
    class VerticalLcdTest {

        @Test
        void shouldShowFilled() {
            VerticalLcds vertical = new VerticalLcds(Led.ON, Led.ON);
            Lines lines = vertical.scale(new Size(1));
            assertEqualsLine("| |", lines);
        }

        @Test
        void shouldShowNotFilled() {
            VerticalLcds vertical = new VerticalLcds(Led.ON, Led.OFF);
            Lines lines = vertical.scale(new Size(1));
            assertEqualsLine("|  ", lines);
        }

        @Test
        void shouldScaleTwo() {
            VerticalLcds vertical = new VerticalLcds(Led.OFF, Led.ON);
            Lines lines = vertical.scale(new Size(2));
            assertEquals(new Lines(Arrays.asList(new Line("   |"), new Line("   |"))), lines);
        }

    }

}
