#include <iostream>
#include <cstring>
using namespace std;

struct PayComponent {
    char desc[30];
    float amount;
};

float computeWithBonus(const PayComponent* comps, int n) {
    float sum = 0.0f;
    const PayComponent* p = comps;
    for (int i = 0; i < n; ++i, ++p) {
        sum += p->amount;
    }
    return sum + 500.0f;
}

int main() {
    PayComponent comps[2] = { {"Basic", 900}, {"Housing", 250} };
    cout << "Total Pay (with bonus): " << computeWithBonus(comps, 2) << endl;
    return 0;
}

