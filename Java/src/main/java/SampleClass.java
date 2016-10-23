
public class SampleClass {

    private int a;
    private int b;
    private int thirdField;

    public void withElse() {
        if (a == b) {
            System.out.println("==1");
        } else {
            // !else
            System.out.println("<>1");
        }
    }
}
