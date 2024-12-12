package lcd;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import print.Lines;

public class LcdDigit implements Lcd {
    // First Class Collection

    private final List<Lcd> parts;

    public LcdDigit(Lcd... parts) {
        this.parts = Arrays.asList(parts);
    }

    @Override
    public Lines scale(Size size) {
        // delegate to elements
        Lines lines = new Lines(Collections.emptyList());
        for (Lcd part : parts) {
            lines.append(part.scale(size));
        }
        return lines;
    }

}
