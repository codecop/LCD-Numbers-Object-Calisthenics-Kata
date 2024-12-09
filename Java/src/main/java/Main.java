import java.util.Arrays;

import number.Digit;
import print.Lines;

public class Main {

    public static void main(String[] args) { // NOPMD this is API
        Size size = new Size(2);
        int number = 575;

        DigitsLookup lookup = new DigitsLookup();

        number.Number n = new number.Number(number);
//                map(lookup::getFor). //
//                map(lcdDigit -> lcdDigit.scale(size)). //
//                reduce(new Lines(), Lines::join); // TODO still not working, why?
//        System.out.println(lines);
    }
}
