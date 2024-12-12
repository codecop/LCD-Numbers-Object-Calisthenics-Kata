package number;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;

public class Number {
    // First Class Collection

    private final List<Digit> digits = new ArrayList<>();

    public Number(int number) {
        // real logic
        String digitCharacters = Integer.toString(number);
        for (int i = 0; i < digitCharacters.length(); i++) {
            int value = digitCharacters.charAt(i) - '0';
            digits.add(new Digit(value));
        }
    }

    public void forEach(Consumer<Digit> consumer) {
        // delegate to elements
        digits.forEach(consumer);
    }

}
