package SortingAlgorithms;

/**
 Implements the Insertion Sort algorithm for integer arrays.
 This class provides a static method to sort an array using Insertion Sort.
 */
public class InsertionSort {
    
    // Sorts a copy of the input array using Insertion Sort and returns the sorted array.
    
    public static int[] InsertionFunc(int[] array, int SIZE)
    {
        // Create a copy of the input array to avoid modifying the original
        int insertArr[] = new int[SIZE];
        for (int i = 0; i < SIZE; i++) {
            insertArr[i] = array[i];
        }

        // Perform Insertion Sort
        for (int i = 1; i < SIZE; i++) {
            int key = insertArr[i]; // Current element to insert
            int j = i - 1;
            // Shift elements of insertArr[0..i-1] that are greater than key to one position ahead
            while (j >= 0 && insertArr[j] > key) {
                insertArr[j + 1] = insertArr[j];
                j = j - 1;
            }
            // Place key after the last element smaller than it
            insertArr[j + 1] = key;
        }

        // Return the sorted array
        return insertArr;
    }
}
