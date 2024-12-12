package lcd;

import java.util.Arrays;
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
        return parts.stream(). //
                map(part -> part.scale(size)). //
                reduce(new Lines(), Lines::append);
    }

}
