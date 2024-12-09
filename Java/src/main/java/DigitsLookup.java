import java.util.HashMap;
import java.util.Map;

public class DigitsLookup {

    private final Map<Digit, LcdDigit> digitsByNumber = new HashMap<>();

    public DigitsLookup() {
        digitsByNumber.put(new Digit(5), new LcdDigit(//
                new HoricontalLcd(Led.ON), //
                new VerticalLcds(Led.ON, Led.OFF), //
                new HoricontalLcd(Led.ON), //
                new VerticalLcds(Led.OFF, Led.ON), //
                new HoricontalLcd(Led.ON)));

        digitsByNumber.put(new Digit(7), new LcdDigit(//
                new HoricontalLcd(Led.ON), //
                new VerticalLcds(Led.OFF, Led.ON), //
                new HoricontalLcd(Led.OFF), //
                new VerticalLcds(Led.OFF, Led.ON), //
                new HoricontalLcd(Led.OFF)));

        // add other numbers...
    }

    public Lcd getFor(Digit digit) {
        if (!digitsByNumber.containsKey(digit)) {
            throw new IllegalArgumentException(digit.toString());
            // could return an E for unknown numbers or throw an exception.
        }
        return digitsByNumber.get(digit);
    }

}
