#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

float entropy(float array[], int size)
{
    float sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum = sum + array[i] * log2(array[i]);
    }
    return sum;
}

int main() {
    entropy([0.3, 0.2, 0.1], 3);
}