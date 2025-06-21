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
    virtual ~PayCalculator() {}
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
    PayComponent comps[2] = { {"Basic", 1200}, {"Allowance", 400} };

    PayCalculator** calculators = new PayCalculator*[2];
    calculators[0] = new RegularPayCalculator();
    calculators[1] = new BonusPayCalculator();

    cout << "Using calculators[0] (Regular): " << calculators[0]->compute(comps, 2) << endl;
    cout << "Using calculators[1] (Bonus):   " << calculators[1]->compute(comps, 2) << endl;

    delete calculators[0];
    delete calculators[1];
    delete[] calculators;
    return 0;
}

