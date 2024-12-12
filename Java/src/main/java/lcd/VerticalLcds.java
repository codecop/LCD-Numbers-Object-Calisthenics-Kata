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
        // real logic
        List<Line> lines = new ArrayList<>();
        Line line = createLine(size);
        size.loop(() -> lines.add(line));
        return new Lines(lines);
    }

    private Line createLine(Size size) {
        // real logic
        String characters = symbolFor(leftLed) + //
                spaceOf(size) + //
                symbolFor(rightLed);
        return new Line(characters);
    }

    private String symbolFor(Led aLed) {
        if (aLed == Led.ON) {
            return "|";
        }
        return " ";
    }

    private String spaceOf(Size size) {
        return times(" ", size);
    }

    private String times(String symbol, Size size) {
        StringBuilder buffer = new StringBuilder();
        size.loop(() -> {
            buffer.append(symbol);
        });
        return buffer.toString();
    }

}
