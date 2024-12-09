package number;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class NumberTest {

    @Test
    void shouldContainDigit() {
        number.Number number = new number.Number(1);
        Digit actual = number.iterator().next();
        assertEquals(new Digit("1"), actual);
    }

}
