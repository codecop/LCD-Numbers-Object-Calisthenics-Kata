package lcd;

import java.util.ArrayList;
import java.util.List;

import print.Line;
import print.Lines;

public class HoricontalLcd implements Lcd {

    private final Led middleLed;

    public HoricontalLcd(Led middleLed) {
        this.middleLed = middleLed;
    }

    @Override
    public Lines scale(Size size) {
        List<Line> lines = new ArrayList<>();
        lines.add(createLine(size));
        return new Lines(lines);
    }

    private Line createLine(Size size) {
        // real logic
        String characters = " " + lcdOf(size) + " ";
        return new Line(characters);
    }

    private String lcdOf(Size size) {
        return times(symbolFor(middleLed), size);
    }

    private String symbolFor(Led aLed) {
        if (aLed == Led.ON) {
            return "-";
        }
        return " ";
    }

    private String times(String symbol, Size size) {
        StringBuilder buffer = new StringBuilder();
        size.loop(() -> {
            buffer.append(symbol);
        });
        return buffer.toString();
    }

}
