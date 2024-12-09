import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

class BarTest {

    void assertEqualsLine(String expected, Lines actual) {
        assertEquals(new Lines(new Line(expected)), actual);
    }

    @Nested
    class HoricontalBarTest {

        @Test
        public void shouldShowFilled() {
            LineScaler horicontal = new HoricontalBar(Led.ON);
            Lines lines = horicontal.scale(new Size(1));
            assertEqualsLine(" - ", lines);
        }

        @Test
        public void shouldShowEmpty() {
            LineScaler horicontal = new HoricontalBar(Led.OFF);
            Lines lines = horicontal.scale(new Size(1));
            assertEqualsLine("   ", lines);
        }

        @Test
        public void shouldScaleTwo() {
            LineScaler horicontal = new HoricontalBar(Led.ON);
            Lines lines = horicontal.scale(new Size(2));
            assertEqualsLine(" -- ", lines);
        }

    }

    @Nested
    class VerticalBarTest {

        @Test
        public void shouldShowFilled() {
            VerticalBars vertical = new VerticalBars(Led.ON, Led.ON);
            Lines lines = vertical.scale(new Size(1));
            assertEqualsLine("| |", lines);
        }

        @Test
        public void shouldShowNotFilled() {
            VerticalBars vertical = new VerticalBars(Led.ON, Led.OFF);
            Lines lines = vertical.scale(new Size(1));
            assertEqualsLine("|  ", lines);
        }

        @Test
        public void shouldScaleTwo() {
            VerticalBars vertical = new VerticalBars(Led.OFF, Led.ON);
            Lines lines = vertical.scale(new Size(2));
            assertEquals(new Lines(new Line("  |"), new Line("  |")), lines);
        }

    }

}
