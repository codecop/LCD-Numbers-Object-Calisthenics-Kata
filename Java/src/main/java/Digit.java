import java.util.Arrays;
import java.util.List;

public class Digit implements LineScaler {

    private final List<LineScaler> lineScalers;

    public Digit(LineScaler... lineScalers) {
        this.lineScalers = Arrays.asList(lineScalers);
    }

    @Override
    public Lines scale(Size size) {
        return lineScalers.stream(). //
                map(scalers -> scalers.scale(size)). //
                reduce(new Lines(), Lines::append);
    }

}
