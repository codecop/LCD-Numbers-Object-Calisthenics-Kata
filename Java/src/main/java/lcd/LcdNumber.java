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
        return digits.stream(). // NOPMD fluent API but has violations
                map(lcdDigit -> lcdDigit.scale(size)). //
                reduce(Lines::join).get();
    }

}
