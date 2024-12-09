import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

import org.junit.jupiter.api.Test;

import number.Digit;
import print.Line;
import print.Lines;

class DigitLookupTest {

    private DigitsLookup digits = new DigitsLookup();

    @Test
    void shouldKnowSingleDigit7() throws IOException {
        int scale = 2;
        int number = 7;
        Lcd seven = digits.getFor(new Digit(number));
        Lines lines = seven.scale(new Size(scale));
        assertEquals(linesFromTestDataFor(scale, number), lines);
    }

    @Test
    void shouldKnowDigits5() throws IOException {
        int scale = 1;
        int number = 5;
        Lcd both = digits.getFor(new number.Number(number));
        Lines lines = both.scale(new Size(scale));
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
