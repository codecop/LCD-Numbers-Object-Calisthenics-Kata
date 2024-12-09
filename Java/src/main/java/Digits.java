import java.util.HashMap;
import java.util.Map;

public class Digits {

    private final Map<Integer, Digit> digitsByNumber = new HashMap<>();

    public Digits() {
        digitsByNumber.put(5, new Digit(//
                new HoricontalBar(Led.ON), //
                new VerticalBars(Led.ON, Led.OFF), //
                new HoricontalBar(Led.ON), //
                new VerticalBars(Led.OFF, Led.ON), //
                new HoricontalBar(Led.ON)));

        digitsByNumber.put(7, new Digit(//
                new HoricontalBar(Led.ON), //
                new VerticalBars(Led.OFF, Led.ON), //
                new HoricontalBar(Led.OFF), //
                new VerticalBars(Led.OFF, Led.ON), //
                new HoricontalBar(Led.OFF)));
    }

    public Digit getFor(int number) {
        return digitsByNumber.get(number);
    }

}
