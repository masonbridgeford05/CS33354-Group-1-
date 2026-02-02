package SortingAlgorithms;

public class Swap {

    // Swaps the elements at indices x and y in the given array
    public static void swap(int[] arr, int x, int y)
    {
        int temp = arr[x];
        arr[x] = arr[y];
        arr[y] = temp;
    }
}
