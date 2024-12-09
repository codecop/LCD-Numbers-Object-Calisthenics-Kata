import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

class DigitTest {

    @Nested
    class HoricontalBarTest {

        @Test
        public void shouldScaleOne() {
            HoricontalBar horicontal = new HoricontalBar(Bar.FILLED);

            horicontal.scale(new Size(1));
            
            assertEquals("", horicontal.toString());
        }
        
    }
    
    
    @Test
    public void shouldSample() {
        assertEquals(2, 1 + 1);
    }

}
