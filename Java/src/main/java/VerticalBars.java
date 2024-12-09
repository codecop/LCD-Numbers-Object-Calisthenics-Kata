
public class VerticalBars {

    private final Led upperLed;
    private final Led lowerLed;

    public VerticalBars(Led upperLed, Led lowerLed) {
        this.upperLed = upperLed;
        this.lowerLed = lowerLed;
    }

    public Lines scale(Size size) {
        Lines lines = new Lines();
        lines.add(corner());
        lines.add(new Line("|"));
        lines.add(corner());
        lines.add(new Line("|"));
        lines.add(corner());
        return lines;
    }

    private Line corner() {
        return new Line(" ");
    }

}
