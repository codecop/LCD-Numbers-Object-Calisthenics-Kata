import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

class DigitTest {

    @Nested
    class HoricontalBarTest {

        @Test
        public void shouldShowFilled() {
            HoricontalBar horicontal = new HoricontalBar(Led.ON);
            Line line = horicontal.scale(new Size(1));
            assertEquals(new Line(" ", "-"), line);
        }

        @Test
        public void shouldShowEmpty() {
            HoricontalBar horicontal = new HoricontalBar(Led.OFF);
            Line line = horicontal.scale(new Size(1));
            assertEquals(new Line(" ", " "), line);
        }

        @Test
        public void shouldScaleTwo() {
            HoricontalBar horicontal = new HoricontalBar(Led.ON);
            Line line = horicontal.scale(new Size(2));
            assertEquals(new Line(" ", "--"), line);
        }

    }

    @Test
    public void shouldSample() {
        assertEquals(2, 1 + 1);
    }

}
