package calisthenics;

public class Lcd {

    private final Templates templates = new Templates();
    private final Size size;

    public Lcd() {
        this(Size.defaultSize());
    }

    public Lcd(Size size) {
        this.size = size;
    }

    public String format(int number) { // NOPMD - Primitive Obsession is public API
        return asNumber(number).join(); // NOPMD LoD is too strict but only one dot.
    }

    private Lines asNumber(int number) { // NOPMD OneLevelOfIntention - don't know how to do it otherwise?
        if (number < 10) {
            return asDigit(number);
        }
        return append(number / 10, number % 10);
    }

    private Lines asDigit(int number) {
        Lines digit = templates.digit(number);
        digit = expandY(digit);
        return expandX(digit);
    }

    private Lines expandY(Lines lines) {
        Lines current = lines;
        current = size.repeat(current, (x) -> x.duplicate(3)); // NOPMD LoD false positive, get back same type
        current = size.repeat(current, (x) -> x.duplicate(1)); // NOPMD LoD false positive, get back same type
        return current;
    }

    private Lines expandX(Lines lines) {
        return lines.map(this::expandX); // NOPMD LoD false positive, get back same type
    }

    private String expandX(String line) {
        StringBuilder buf = new StringBuilder();
        buf.append(line.substring(0, 1));
        String c = line.substring(1, 2);
        buf.append(c);
        size.repeat(() -> buf.append(c));
        buf.append(line.substring(2));
        return buf.toString();
    }

    private Lines append(int leftDigit, int rightDigit) {
        Lines left = asNumber(leftDigit);
        Lines right = asDigit(rightDigit);
        return left.append(right); // NOPMD LoD false positive, get back same type
    }

}
