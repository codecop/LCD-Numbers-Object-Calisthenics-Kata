
public class HoricontalBar {

    private final BarIs barIs;

    public HoricontalBar(BarIs barIs) {
        this.barIs = barIs;
    }

    public Line scale(Size size) {
        return new Line(" - ");
    }

}
