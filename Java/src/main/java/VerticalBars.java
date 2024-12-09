
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
            lines.add(createLine());
        });
        return lines;
    }

    private Line createLine() {
        return new Line(verticalSymbolFor(leftLed), space(), verticalSymbolFor(rightLed));
    }

    private String verticalSymbolFor(Led aLed) {
        if (aLed == Led.ON) {
            return "|";
        }
        return " ";
    }

    private String space() { // NOPMD this is no getter
        return " ";
    }

}
