
public class HoricontalBar {

    private final BarIs barIs;

    public HoricontalBar(BarIs barIs) {
        this.barIs = barIs;
    }

    public Line scale(Size size) {
        String corner = " ";
        String middle = barIs == BarIs.FILLED ? "-" : " ";
        return new Line(corner, middle);
    }

}
