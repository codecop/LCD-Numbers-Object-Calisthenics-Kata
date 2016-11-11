package calisthenics;

public class Lcd {

    private final Size size;
    private final Templates template = new Templates();

    public Lcd() {
        this(Size.defaultSize());
    }

    public Lcd(Size size) {
        this.size = size;
    }

    public String format(int number) { // NO PMD - Primitive Obsession is public API
        return expandedNumber(number).join(); // NOPMD LoD is too strict but only one dot.
    }

    private Lines expandedNumber(int number) { // NOPMD OneLevelOfIntention - don't know how to do it otherwise?
        if (number < 10) {
            return expandedDigit(number);
        }
        return append(number / 10, number % 10);
    }

    private Lines expandedDigit(int number) {
        Lines digit = template.digit(number);
        expandY(digit);
        return expandX(digit);
    }

    private void expandY(Lines lines) {
        size.repeat(() -> lines.duplicate(3));
        size.repeat(() -> lines.duplicate(1));
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
        Lines left = expandedNumber(leftDigit);
        Lines right = expandedDigit(rightDigit);
        return left.join(right); // NOPMD LoD false positive, get back same type
    }

}
