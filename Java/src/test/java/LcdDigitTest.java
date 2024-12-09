import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

import org.junit.jupiter.api.Test;

class LcdDigitTest {

    @Test
    public void shouldShowFive() throws IOException {
        LcdDigit five = new LcdDigit(new HoricontalLcd(Led.ON), //
                new VerticalLcds(Led.ON, Led.OFF), //
                new HoricontalLcd(Led.ON), //
                new VerticalLcds(Led.OFF, Led.ON), //
                new HoricontalLcd(Led.ON));

        Lines lines = five.scale(new Size(1));

        assertEquals(new Lines( //
                new Line(" - "), //
                new Line("|  "), //
                new Line(" - "), //
                new Line("  |"), //
                new Line(" - ")), lines);
        assertEquals(linesFromTestDataFor(1, 5), lines);
    }

    private Lines linesFromTestDataFor(int size, int digit) throws IOException {
        String fileName = "src/test/resources/size_" + size + "/number " + digit + ".txt";
        List<Line> lines = Files.lines(Paths.get(fileName)). // NOPMD fluent interface
                map(Line::new). //
                collect(Collectors.toList());
        return new Lines(lines);
    }

}
