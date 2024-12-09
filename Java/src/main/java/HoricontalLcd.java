import print.Line;
import print.Lines;

public class HoricontalLcd implements Lcd {

    private final Led middleLed;

    public HoricontalLcd(Led middleLed) {
        this.middleLed = middleLed;
    }

    @Override
    public Lines scale(Size size) {
        return new Lines(new Line(corner(), lcdOf(size), corner()));
    }

    private String corner() { // NOPMD this is no getter
        return " ";
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
