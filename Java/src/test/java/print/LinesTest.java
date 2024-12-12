package print;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

class LinesTest {

    @Test
    void shouldJoin() {
        Lines left = new Lines(Arrays.asList( //
                new Line(" - "), //
                new Line("|  "), //
                new Line(" - "), //
                new Line("  |"), //
                new Line(" - ")));
        Lines right = new Lines(Arrays.asList( //
                new Line(" - "), //
                new Line("| |"), //
                new Line(" - "), //
                new Line("| |"), //
                new Line(" - ")));

        Lines actual = left.join(right);

        assertEquals(new Lines(Arrays.asList( //
                new Line(" -  - "), //
                new Line("|  | |"), //
                new Line(" -  - "), //
                new Line("  || |"), //
                new Line(" -  - "))), actual);
    }

}
