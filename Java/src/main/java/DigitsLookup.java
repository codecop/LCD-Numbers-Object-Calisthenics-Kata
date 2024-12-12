import java.util.HashMap;
import java.util.Map;

import lcd.HoricontalLcd;
import lcd.Lcd;
import lcd.LcdDigit;
import lcd.LcdNumber;
import lcd.Led;
import lcd.VerticalLcds;
import number.Digit;

public class DigitsLookup {
    // First Class Collection

    private final Map<Digit, LcdDigit> digitsByNumber = new HashMap<>();

    public DigitsLookup() {
        // 0-4 missing
        digitsByNumber.put(new Digit(5), new LcdDigit(//
                new HoricontalLcd(Led.ON), //
                new VerticalLcds(Led.ON, Led.OFF), //
                new HoricontalLcd(Led.ON), //
                new VerticalLcds(Led.OFF, Led.ON), //
                new HoricontalLcd(Led.ON)));
        // 6 missing
        digitsByNumber.put(new Digit(7), new LcdDigit(//
                new HoricontalLcd(Led.ON), //
                new VerticalLcds(Led.OFF, Led.ON), //
                new HoricontalLcd(Led.OFF), //
                new VerticalLcds(Led.OFF, Led.ON), //
                new HoricontalLcd(Led.OFF)));
        // 8-9 missing

        // add other numbers...
    }

    public Lcd getFor(number.Number number) {
        LcdNumber lcdNumber = new LcdNumber();
        number.forEach(digit -> {
            Lcd lcdDigit = getFor(digit);
            lcdNumber.add(lcdDigit);
        });
        return lcdNumber;
    }

    private Lcd getFor(Digit digit) {
        // delegate to elements
        if (!digitsByNumber.containsKey(digit)) {
            throw new IllegalArgumentException(digit.toString());
            // could return an E for unknown numbers or throw an exception.
        }
        return digitsByNumber.get(digit);
    }

}
