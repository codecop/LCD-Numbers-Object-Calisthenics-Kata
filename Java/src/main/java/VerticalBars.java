
public class VerticalBars {

    private final Led upperLed;
    private final Led lowerLed;

    public VerticalBars(Led upperLed, Led lowerLed) {
        this.upperLed = upperLed;
        this.lowerLed = lowerLed;
    }

    public Lines scale(Size size) {
        Lines lines = new Lines();
        lines.add(new Line("|", corner(), "|"));
        return lines;
    }

    private String corner() { // NOPMD this is no getter
        return " ";
    }

}
