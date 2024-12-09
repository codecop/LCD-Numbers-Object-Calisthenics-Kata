import java.util.Arrays;
import java.util.List;

public class LcdDigit implements PartLcd {
    // First Order Collection

    private final List<PartLcd> parts;

    public LcdDigit(PartLcd... parts) {
        this.parts = Arrays.asList(parts);
    }

    @Override
    public Lines scale(Size size) {
        return parts.stream(). //
                map(part -> part.scale(size)). //
                reduce(new Lines(), Lines::append);
    }

}
