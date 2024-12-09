package number;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Number implements Iterable<Digit> {

    private final List<Digit> digits;

    public Number(int number) {
        this.digits = mapToDigits(number);
    }

    private static List<Digit> mapToDigits(int number) {
        // return Integer.toString(number). //
        //    chars(). //
        //    mapToObj(c -> Character.valueOf((char) c)). //
        //    map(Object::toString). //
        //    map(Digit::new). //
        //    collect(Collectors.toList());

        List<Digit> result = new ArrayList<>();

        String digits = Integer.toString(number);
        for (int i = 0; i < digits.length(); i++) {
            int value = digits.charAt(i) - '0';
            result.add(new Digit(value));
        }

        return result;
    }

    @Override
    public Iterator<Digit> iterator() {
        return digits.iterator();
    }

}
