void mergeInPlace(int arr[], int n) {
    int mid = n / 2;
    int i = 0;
    int j = mid;

    while (i < j && j < n) {
        if (arr[i] <= arr[j]) {
            i++;
        } else {
            int value = arr[j];
            int index = j;

            // Shift all elements between i and j to the right by 1
            while (index > i) {
                arr[index] = arr[index - 1];
                index--;
            }
            arr[i] = value;

            // Update pointers
            i++;
            j++;
        }
    }
}
