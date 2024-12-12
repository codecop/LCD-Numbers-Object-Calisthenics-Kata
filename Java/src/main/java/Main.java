import lcd.Lcd;
import lcd.Size;
import print.Lines;

public class Main {

    public static void main(String[] args) { // NOPMD String[] is API
        int argument1 = 755;
        int argument2 = 3;

        number.Number number = new number.Number(argument1);
        Size size = new Size(argument2);

        DigitsLookup digitsLookup = new DigitsLookup();
        Lcd lcdNumber = digitsLookup.getFor(number);
        Lines lines = lcdNumber.scale(size);

        lines.println();
    }
}
