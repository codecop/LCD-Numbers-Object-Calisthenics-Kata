
public class VerticalBars {

    private final Led leftLed;
    private final Led rightLed;

    public VerticalBars(Led leftLed, Led rightLed) {
        this.leftLed = leftLed;
        this.rightLed = rightLed;
    }

    public Lines scale(Size size) {
        Lines lines = new Lines();
        lines.add(new Line(verticalSymbolFor(leftLed), space(), verticalSymbolFor(rightLed)));
        return lines;
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
