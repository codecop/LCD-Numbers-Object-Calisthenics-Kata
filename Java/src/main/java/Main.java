import lcd.Size;

public class Main {

    public static void main(String[] args) { // NOPMD String[] is API
        int argument1 = 755;
        int argument2 = 3;

        number.Number number = new number.Number(argument1);
        Size size = new Size(argument2);

        new DigitsLookup().getFor(number).scale(size).println(); // NOPMD This is a massive violation ;-)
    }

}
