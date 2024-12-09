import java.util.HashMap;
import java.util.Map;

public class DigitsLookup {

    private final Map<Integer, LcdDigit> digitsByNumber = new HashMap<>();

    public DigitsLookup() {
        digitsByNumber.put(5, new LcdDigit(//
                new HoricontalLcd(Led.ON), //
                new VerticalLcds(Led.ON, Led.OFF), //
                new HoricontalLcd(Led.ON), //
                new VerticalLcds(Led.OFF, Led.ON), //
                new HoricontalLcd(Led.ON)));

        digitsByNumber.put(7, new LcdDigit(//
                new HoricontalLcd(Led.ON), //
                new VerticalLcds(Led.OFF, Led.ON), //
                new HoricontalLcd(Led.OFF), //
                new VerticalLcds(Led.OFF, Led.ON), //
                new HoricontalLcd(Led.OFF)));

        // add other numbers...
    }

    public LcdDigit getFor(int number) {
        // could return an E for unknown numbers or throw an exception.
        return digitsByNumber.get(number);
    }

}
