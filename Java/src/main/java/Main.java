import lcd.Size;
import print.Lines;

public class Main {

    public static void main(String[] args) { // NOPMD this is API
        Size size = new Size(2);
        int number = 575;

        Lines lines = new DigitsLookup(). //
                getFor(new number.Number(number)). // this is a LoD violation!
                scale(size); //

        System.out.println(lines);
    }
}
