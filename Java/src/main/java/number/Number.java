package number;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Collectors;

public class Number implements Iterable<Digit> {

    private final List<Digit> digits;

    public Number(int number) {
        this.digits = mapToDigits(number);
    }

    private List<Digit> mapToDigits(int number) {
        String[] singleDigits = Integer.toString(number).split("");
        return Arrays.stream(singleDigits). //
                map(Digit::new). //
                collect(Collectors.toList());
    }

    @Override
    public Iterator<Digit> iterator() {
        return digits.iterator();
    }

}
