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

    public String format(int number) { // NO PMD - Primitive Obsession is public API
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
        Lines left = asNumber(leftDigit);
        Lines right = asDigit(rightDigit);
        return left.join(right); // NOPMD LoD false positive, get back same type
    }

}
