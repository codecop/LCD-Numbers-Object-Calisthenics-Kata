
public class VerticalBar {

    private final Led upperLed;
    private final Led lowerLed;

    public VerticalBar(Led upperLed, Led lowerLed) {
        this.upperLed = upperLed;
        this.lowerLed = lowerLed;
    }

    public Lines scale(Size size) {
        return new Lines(new Line(" "), new Line("|"), new Line(" "), new Line("|"), new Line(" "));
    }

}
