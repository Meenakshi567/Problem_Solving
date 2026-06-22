#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

// Function prototypes
void display(int arr[], int size);
void insert(int arr[], int *size);
void deleteItem(int arr[], int *size);
void search(int arr[], int size);

int main() {
    int arr[MAX_SIZE];
    int size = 0;
    int choice;

    // Pre-populating the array with initial values for easier testing
    arr[0] = 10;
    arr[1] = 20;
    arr[2] = 30;
    size = 3;

    while (1) {
        printf("\n--- ARRAY OPERATIONS MENU ---\n");
        printf("1. Display Array\n");
        printf("2. Insert Element\n");
        printf("3. Delete Element\n");
        printf("4. Search Element\n");
        printf("5. Exit\n");
        printf("Enter your choice (1-5): ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                display(arr, size);
                break;
            case 2:
                insert(arr, &size);
                break;
            case 3:
                deleteItem(arr, &size);
                break;
            case 4:
                search(arr, size);
                break;
            case 5:
                printf("Exiting program. Goodbye!\n");
                exit(0);
            default:
                printf("Invalid choice! Please enter a number between 1 and 5.\n");
        }
    }
    return 0;
}

// 1. Function to display the array
void display(int arr[], int size) {
    if (size == 0) {
        printf("Array is empty.\n");
        return;
    }
    printf("Current Array: ");
    for (int i = 0; i < size; i++) {
        printf("[%d]:%d ", i, arr[i]);
    }
    printf("\nTotal elements: %d\n", size);
}

// 2. Function to insert an element
void insert(int arr[], int *size) {
    int element, index;

    if (*size >= MAX_SIZE) {
        printf("Error: Array Overflow. Cannot insert more elements.\n");
        return;
    }

    printf("Enter element to insert: ");
    scanf("%d", &element);
    printf("Enter index position (0 to %d): ", *size);
    scanf("%d", &index);

    if (index < 0 || index > *size) {
        printf("Error: Invalid position!\n");
        return;
    }

    // Shift elements to the right
    for (int i = *size; i > index; i--) {
        arr[i] = arr[i - 1];
    }

    arr[index] = element;
    (*size)++;
    printf("Element inserted successfully.\n");
}

// 3. Function to delete an element
void deleteItem(int arr[], int *size) {
    int index;

    if (*size == 0) {
        printf("Error: Array Underflow. Nothing to delete.\n");
        return;
    }

    printf("Enter index to delete (0 to %d): ", *size - 1);
    scanf("%d", &index);

    if (index < 0 || index >= *size) {
        printf("Error: Invalid position!\n");
        return;
    }

    int removedValue = arr[index];

    // Shift elements to the left
    for (int i = index; i < *size - 1; i++) {
        arr[i] = arr[i + 1];
    }

    (*size)--;
    printf("Deleted element %d from index %d.\n", removedValue, index);
}

// 4. Function to search for an element
void search(int arr[], int size) {
    int target, found = 0;

    if (size == 0) {
        printf("Array is empty. Search cannot be performed.\n");
        return;
    }

    printf("Enter element to search for: ");
    scanf("%d", &target);

    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            printf("Success: Element %d found at index %d.\n", target, i);
            found = 1;
            break; // Stop searching once found
        }
    }

    if (!found) {
        printf("Element %d not found in the array.\n", target);
    }
}
