import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

class DigitTest {

    @Nested
    class HoricontalBarTest {

        @Test
        public void shouldScaleOne() {
            HoricontalBar horicontal = new HoricontalBar(BarIs.FILLED);

            Line line = horicontal.scale(new Size(1));

            assertEquals(new Line(" ", "-"), line);
        }

        @Test
        public void shouldScaleEmptyOne() {
            HoricontalBar horicontal = new HoricontalBar(BarIs.EMPTY);

            Line line = horicontal.scale(new Size(1));

            assertEquals(new Line(" ", " "), line);
        }

    }

    @Test
    public void shouldSample() {
        assertEquals(2, 1 + 1);
    }

}
