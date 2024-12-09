import java.util.Arrays;

import print.Lines;

public class Main {

    public static void main(String[] args) { // NOPMD this is API
        Size size = new Size(2);
        int number = 575;

        DigitsLookup lookup = new DigitsLookup();

        String[] digits = Integer.toString(number).split("");
        Lines lines = Arrays.stream(digits). //
                map(Digit::new). //
                map(lookup::getFor). //
                map(lcdDigit -> lcdDigit.scale(size)). //
                reduce(new Lines(), Lines::join); // TODO still not working, why?
        System.out.println(lines);
    }
}
