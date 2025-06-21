#include <iostream>
#include <cstring>
using namespace std;

struct PayComponent {
    char desc[30];
    float amount;
};

class PayCalculator {
public:
    virtual float compute(const PayComponent* comps, int n) = 0;
};

class RegularPayCalculator : public PayCalculator {
public:
    float compute(const PayComponent* comps, int n) override {
        float sum = 0.0f;
        for (int i = 0; i < n; ++i)
            sum += comps[i].amount;
        return sum;
    }
};

class BonusPayCalculator : public PayCalculator {
public:
    float compute(const PayComponent* comps, int n) override {
        float sum = 0.0f;
        for (int i = 0; i < n; ++i)
            sum += comps[i].amount;
        return sum + 500.0f;
    }
};

int main() {
    PayComponent comps[2] = { {"Basic", 1000}, {"Transport", 300} };

    RegularPayCalculator regular;
    BonusPayCalculator bonus;

    cout << "Regular Pay: " << regular.compute(comps, 2) << endl;
    cout << "Bonus Pay: " << bonus.compute(comps, 2) << endl;

    return 0;
}

