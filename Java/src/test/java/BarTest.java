import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

class BarTest {

    void assertEqualsLine(String expected, Lines actual) {
        assertEquals(new Lines(new Line(expected)), actual);
    }

    @Nested
    class HoricontalLcdTest {

        @Test
        public void shouldShowFilled() {
            PartLcd horicontal = new HoricontalLcd(Led.ON);
            Lines lines = horicontal.scale(new Size(1));
            assertEqualsLine(" - ", lines);
        }

        @Test
        public void shouldShowEmpty() {
            PartLcd horicontal = new HoricontalLcd(Led.OFF);
            Lines lines = horicontal.scale(new Size(1));
            assertEqualsLine("   ", lines);
        }

        @Test
        public void shouldScaleTwo() {
            PartLcd horicontal = new HoricontalLcd(Led.ON);
            Lines lines = horicontal.scale(new Size(2));
            assertEqualsLine(" -- ", lines);
        }

    }

    @Nested
    class VerticalLcdTest {

        @Test
        public void shouldShowFilled() {
            VerticalLcds vertical = new VerticalLcds(Led.ON, Led.ON);
            Lines lines = vertical.scale(new Size(1));
            assertEqualsLine("| |", lines);
        }

        @Test
        public void shouldShowNotFilled() {
            VerticalLcds vertical = new VerticalLcds(Led.ON, Led.OFF);
            Lines lines = vertical.scale(new Size(1));
            assertEqualsLine("|  ", lines);
        }

        @Test
        public void shouldScaleTwo() {
            VerticalLcds vertical = new VerticalLcds(Led.OFF, Led.ON);
            Lines lines = vertical.scale(new Size(2));
            assertEquals(new Lines(new Line("   |"), new Line("   |")), lines);
        }

    }

}
