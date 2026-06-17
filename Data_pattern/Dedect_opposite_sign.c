#include <stdbool.h>

bool haveOppositeSigns(int a, int b) {
    return (a ^ b) < 0;
}
