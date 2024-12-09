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
        return digits.get(0).scale(size);
    }

}
