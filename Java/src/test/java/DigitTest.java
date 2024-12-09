import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class DigitTest {

    @Test
    public void shouldShowFive() {
        Digit five = new Digit(new HoricontalBar(Led.ON), //
                new VerticalBars(Led.ON, Led.OFF), //
                new HoricontalBar(Led.ON), //
                new VerticalBars(Led.OFF, Led.ON), //
                new HoricontalBar(Led.ON));

        Lines lines = five.scale(new Size(1));

        assertEquals(new Lines(//
                new Line(" - "), //
                new Line("|  "), //
                new Line(" - "), //
                new Line("  |"), //
                new Line(" - ")), lines);
    }

}
