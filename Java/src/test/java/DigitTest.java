import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

import org.junit.jupiter.api.Test;

class DigitTest {

    @Test
    public void shouldShowFive() throws IOException {
        Digit five = new Digit(new HoricontalBar(Led.ON), //
                new VerticalBars(Led.ON, Led.OFF), //
                new HoricontalBar(Led.ON), //
                new VerticalBars(Led.OFF, Led.ON), //
                new HoricontalBar(Led.ON));

        Lines lines = five.scale(new Size(1));

        assertEquals(new Lines( //
                new Line(" - "), //
                new Line("|  "), //
                new Line(" - "), //
                new Line("  |"), //
                new Line(" - ")), lines);
        assertEquals(linesFromTestDataFor(1, 5), lines);
    }

    @Test
    public void shouldKnowDigit7() throws IOException {
        int scale = 2;
        int number = 7;
        Digits digits = new Digits();
        Digit seven = digits.getFor(number);
        Lines lines = seven.scale(new Size(scale));
        assertEquals(linesFromTestDataFor(scale, number), lines);
    }

    private Lines linesFromTestDataFor(int size, int digit) throws IOException {
        String fileName = "src/test/resources/size_" + size + "/number " + digit + ".txt";
        List<Line> lines = Files.lines(Paths.get(fileName)). // NOPMD fluent interface
                map(Line::new). //
                collect(Collectors.toList());
        return new Lines(lines);
    }

}
