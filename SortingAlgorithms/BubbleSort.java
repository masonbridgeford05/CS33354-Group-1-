package SortingAlgorithms;

// Import the swap utility function
import static SortingAlgorithms.Swap.swap;

/*
 Implements the Bubble Sort algorithm for integer arrays.
 This class provides a static method to sort an array using Bubble Sort.
 */
public class BubbleSort {
    
    // Sorts a copy of the input array using Bubble Sort and returns the sorted array.
    public static int[] BubbleFunc(int[] arr, int SIZE) {
        // Create a copy of the input array to avoid modifying the original
        int bubbleArr[] = new int[SIZE];
        for (int i = 0; i < SIZE; i++) {
            bubbleArr[i] = arr[i];
        }

        // Perform Bubble Sort
        for (int i = 0; i < SIZE - 1; i++) {
            // After each pass, the largest element in the unsorted portion bubbles to the end
            for (int j = 0; j < SIZE - 1 - i; j++) {
                // Compare adjacent elements and swap if out of order
                if (bubbleArr[j] > bubbleArr[j + 1]) {
                    swap(bubbleArr, j, j + 1);
                }
            }
        }

        // Return the sorted array
        return bubbleArr;
    }
}
