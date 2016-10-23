
public class SampleClass {

    private int a;
    private int b;
    private int thirdField; // ! third field

    public void withElse() {
        if (a == b) {
            a = thirdField;
        } else {
            // ! else 
            b = thirdField;
        }
    }
}
