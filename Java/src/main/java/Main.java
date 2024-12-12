import lcd.Size;
import print.Lines;

public class Main {

    public static void main(String[] args) { // NOPMD String[] is API
        Size size = new Size(2);
        int input = 575;

        number.Number number = new number.Number(input);

        Lines lines = new DigitsLookup(). //
                getFor(number). // this is a LoD violation!
                scale(size); //

        System.out.println(lines);
    }
}
