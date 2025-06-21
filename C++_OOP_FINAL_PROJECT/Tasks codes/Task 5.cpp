#include <iostream>
#include <cstring>
using namespace std;

struct PayComponent {
    char desc[30];
    float amount;
};

class Employee {
private:
    PayComponent* comps;
    int n;

public:
    Employee() : comps(NULL), n(0) {}

    void addComponent(const PayComponent& comp) {
        PayComponent* newComps = new PayComponent[n + 1];
        for (int i = 0; i < n; ++i)
            newComps[i] = comps[i];
        newComps[n] = comp;
        delete[] comps;
        comps = newComps;
        ++n;
    }

    void removeComponent(int index) {
        if (index < 0 || index >= n) return;
        PayComponent* newComps = new PayComponent[n - 1];
        for (int i = 0, j = 0; i < n; ++i) {
            if (i != index)
                newComps[j++] = comps[i];
        }
        delete[] comps;
        comps = newComps;
        --n;
    }

    void display() const {
        for (int i = 0; i < n; ++i)
            cout << comps[i].desc << ": " << comps[i].amount << endl;
    }

    ~Employee() {
        delete[] comps;
    }
};

int main() {
    Employee emp;
    PayComponent pc1 = {"Basic", 1500};
    PayComponent pc2 = {"Transport", 300};
    PayComponent pc3 = {"Medical", 200};

    emp.addComponent(pc1);
    emp.addComponent(pc2);
    emp.addComponent(pc3);

    cout << "Before removal:\n";
    emp.display();

    emp.removeComponent(1);  // Remove "Transport"
    
    cout << "\nAfter removal:\n";
    emp.display();

    return 0;
}

