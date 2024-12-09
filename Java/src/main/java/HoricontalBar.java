
public class HoricontalBar {

    private final Led middleLed;

    public HoricontalBar(Led middleLed) {
        this.middleLed = middleLed;
    }

    public Line scale(Size size) {
        return new Line(corner(), barOf(size), corner());
    }

    private String corner() { // NOPMD this is no getter
        return " ";
    }

    private String barOf(Size size) {
        String symbol = " ";
        if (middleLed == Led.ON) {
            symbol = "-";
        }
        return times(symbol, size);
    }

    private String times(String symbol, Size size) {
        StringBuilder buffer = new StringBuilder();
        size.loop(() -> {
            buffer.append(symbol);
        });
        return buffer.toString();
    }

}
