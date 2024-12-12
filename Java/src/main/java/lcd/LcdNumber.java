package lcd;

import java.util.ArrayList;
import java.util.List;

import print.Lines;

public class LcdNumber implements Lcd {
    // First Class Collection

    private final List<Lcd> digits = new ArrayList<>();

    public void add(Lcd lcdDigit) {
        digits.add(lcdDigit);
    }

    @Override
    public Lines scale(Size size) {
        // delegate to elements
        return digits.stream(). // NOPMD fluent API
                map(digit -> digit.scale(size)). //
                reduce(Lines::join).get();
    }

}
