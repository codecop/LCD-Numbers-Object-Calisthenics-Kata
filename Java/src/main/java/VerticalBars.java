
public class VerticalBars implements LineScaler {

    private final Led leftLed;
    private final Led rightLed;

    public VerticalBars(Led leftLed, Led rightLed) {
        this.leftLed = leftLed;
        this.rightLed = rightLed;
    }

    @Override
    public Lines scale(Size size) {
        Lines lines = new Lines();
        size.loop(() -> {
            lines.add(createLine(size));
        });
        return lines;
    }

    private Line createLine(Size size) {
        return new Line(verticalSymbolFor(leftLed), //
                times(space(), size), //
                verticalSymbolFor(rightLed));
    }

    private String verticalSymbolFor(Led aLed) {
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
