
public class HoricontalBar {

    private final Led middleLed;

    public HoricontalBar(Led middleLed) {
        this.middleLed = middleLed;
    }

    public Line scale(Size size) {
        return new Line(corner(), barOf(size), corner());
    }

    private String corner() { // NOPMD this is no getter
        return " ";
    }

    private String barOf(Size size) {
        return times(horicontalSymbolFor(middleLed), size);
    }

    private String horicontalSymbolFor(Led aLed) {
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
