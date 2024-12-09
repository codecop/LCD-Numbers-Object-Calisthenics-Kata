package util;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Joiner<T extends Joinable<T>> {

    public List<T> join(Iterable<T> left, Iterable<T> right) { // NOPMD I want this generic
        Iterator<T> leftIterator = left.iterator();
        Iterator<T> rightIterator = right.iterator();
        return join(leftIterator, rightIterator);
    }

    private List<T> join(Iterator<T> leftIterator, Iterator<T> rightIterator) {
        List<T> result = new ArrayList<>();

        while (leftIterator.hasNext() && rightIterator.hasNext()) {
            T nextLeft = leftIterator.next();
            T nextRight = rightIterator.next();
            result.add(join(nextLeft, nextRight));
        }

        return result;
    }

    public T join(T left, T right) {
        return left.join(right);
    }
}
