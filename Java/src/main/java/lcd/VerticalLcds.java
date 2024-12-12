package lcd;

import java.util.ArrayList;
import java.util.List;

import print.Line;
import print.Lines;

public class VerticalLcds implements Lcd {

    private final Led leftLed;
    private final Led rightLed;

    public VerticalLcds(Led leftLed, Led rightLed) {
        this.leftLed = leftLed;
        this.rightLed = rightLed;
    }

    @Override
    public Lines scale(Size size) {
        List<Line> lines = new ArrayList<>();
        size.loop(() -> {
            lines.add(createLine(size));
        });
        return new Lines(lines);
    }

    private Line createLine(Size size) {
        String characters = symbolFor(leftLed) + //
                times(space(), size) + //
                symbolFor(rightLed);
        return new Line(characters);
    }

    private String symbolFor(Led aLed) {
        if (aLed == Led.ON) {
            return "|";
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

    private String space() { // NOPMD this is no getter
        return " ";
    }

}
