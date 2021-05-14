#include <cstdlib>

#include <iostream>

using namespace std;

int main() {
	n = cin << Введіть кількість чисел, яку потрібно згерерувати << endl;
	srand((unsigned) time(0));
	int randomNumber;
	for (int index = 0; index < n; index++) {
		randomNumber = (rand() % 100) + 1;
		cout << randomNumber << endl;
	}
}
