package number;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class NumberTest {

    @Test
    void shouldContainDigit() {
        number.Number number = new number.Number(1);
        for (Digit actual : number) {
            assertEquals(new Digit(1), actual);
        }
    }

}
