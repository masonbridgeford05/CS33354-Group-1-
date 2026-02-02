package SortingAlgorithms;

import static SortingAlgorithms.BubbleSort.BubbleFunc;
import static SortingAlgorithms.SelectionSort.SelectionFunc;
import static SortingAlgorithms.InsertionSort.InsertionFunc;

/*
 Main program to compare the performance of Bubble Sort, Selection Sort, and Insertion Sort.
 
 Generates a random array, sorts it using each algorithm, and prints timing results.
 */
public class SortingComparison_cxc210050{
    public static void main(String[] args)
    {
        int SIZE = 10000; // Size of the array to sort
        int array[] = new int[SIZE];

        // Generate random array
        genRand(array, SIZE);

        // Print the first 20 elements of the original array
        System.out.println("Original array (first 20 elements):");
        for (int i = 0; i < 20; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.print("\n\n");

    // Run Bubble Sort and measure only the sort (copying excluded)
    SortResult bubbleResult = runBubbleSort(array, SIZE);
    int[] bubbleSorted = bubbleResult.sorted;
    double bubbleTime = bubbleResult.timeMs;

        // Print the first 20 elements of the bubble sorted array
        System.out.println("Bubble Sort (first 20 elements of sorted array):");
        for (int i = 0; i < 20; i++) {
            System.out.print(bubbleSorted[i] + " ");
        }
        System.out.println("\n\n");

    // Run Selection Sort and measure only the sort (copying excluded)
    SortResult selectionResult = runSelectionSort(array, SIZE);
    int[] selectionSorted = selectionResult.sorted;
    double selectionTime = selectionResult.timeMs;

        // Print the first 20 elements of the selection sorted array
        System.out.println("Selection Sort (first 20 elements of sorted array):");
        for (int i = 0; i < 20; i++) {
            System.out.print(selectionSorted[i] + " ");
        }
        System.out.println("\n\n");

    // Run Insertion Sort and measure only the sort (copying excluded)
    SortResult insertionResult = runInsertionSort(array, SIZE);
    int[] insertionSorted = insertionResult.sorted;
    double insertionTime = insertionResult.timeMs;

        // Print the first 20 elements of the Insertion sorted array
        System.out.println("Insertion Sort (first 20 elements of sorted array):");
        for (int i = 0; i < 20; i++) {
            System.out.print(insertionSorted[i] + " ");
        }
        System.out.println("\n\n");

        // Print timing results for each algorithm
        System.out.println("========== PERFORMANCE COMPARISON ==========");
        System.out.println("Bubble Sort Time:     " + String.format("%.2f", bubbleTime) + " ms");
        System.out.println("Selection Sort Time:  " + String.format("%.2f", selectionTime) + " ms");
        System.out.println("Insertion Sort Time:  " + String.format("%.2f", insertionTime) + " ms");
        System.out.println("=============================================\n");
    }

    
    // Fills the given array with random integers in the range 0 to 9999
    public static void genRand(int[] array, int SIZE)
    {
        for (int i = 0; i < SIZE; i++) {
            array[i] = (int)(Math.random() * 10000);
        }
    }

    // Small container for a sort result: sorted array and time in milliseconds.
    
    public static class SortResult {
        public final int[] sorted;
        public final double timeMs;

        public SortResult(int[] sorted, double timeMs) {
            this.sorted = sorted;
            this.timeMs = timeMs;
        }
    }

    // Run BubbleSort on a copy of src and return the sorted array and elapsed time in ms.
    public static SortResult runBubbleSort(int[] src, int n) {
        int[] work = copyArray(src, n);
        long start = System.nanoTime();
        int[] sorted = BubbleFunc(work, n);
        long end = System.nanoTime();
        return new SortResult(sorted, (end - start) / 1_000_000.0);
    }

    // Run SelectionSort on a copy of src and return the sorted array and elapsed time in ms.
    public static SortResult runSelectionSort(int[] src, int n) {
        int[] work = copyArray(src, n);
        long start = System.nanoTime();
        int[] sorted = SelectionFunc(work, n);
        long end = System.nanoTime();
        return new SortResult(sorted, (end - start) / 1_000_000.0);
    }

    // Run InsertionSort on a copy of src and return the sorted array and elapsed time in ms.
    public static SortResult runInsertionSort(int[] src, int n) {
        int[] work = copyArray(src, n);
        long start = System.nanoTime();
        int[] sorted = InsertionFunc(work, n);
        long end = System.nanoTime();
        return new SortResult(sorted, (end - start) / 1_000_000.0);
    }

    
    //Returns a new array that is a copy of the first n elements of src.
    public static int[] copyArray(int[] src, int n) {
        int[] dst = new int[n];
        for (int i = 0; i < n; i++) {
            dst[i] = src[i];
        }
        return dst;
    }
}



