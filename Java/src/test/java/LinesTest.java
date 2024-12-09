import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class LinesTest {

    @Test
    void test() {
        Lines left = new Lines( //
                new Line(" - "), //
                new Line("|  "), //
                new Line(" - "), //
                new Line("  |"), //
                new Line(" - "));
        Lines right = new Lines( //
                new Line(" - "), //
                new Line("| |"), //
                new Line(" - "), //
                new Line("| |"), //
                new Line(" - "));

        Lines actual = left.join(right);

        assertEquals(new Lines( //
                new Line(" -  - "), //
                new Line("|  | |"), //
                new Line(" -  - "), //
                new Line("  || |"), //
                new Line(" -  - ")), actual);
    }

}
