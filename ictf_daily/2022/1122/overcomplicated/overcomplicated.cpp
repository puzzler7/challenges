#include <iostream>

using namespace std;

class my_int {
public:
    int val;
    my_int(int i)
    {
        val = i;
    }

    my_int operator^ (const my_int & other) const
    {
        return my_int(val ^ other.val);
    }

    friend ostream& operator<< (ostream &os, const my_int &s) {
        (os << s.val);
        return os;
    }

    bool operator== (const my_int & other) const
    {
        return val == other.val;
    }

    bool operator!= (const my_int & other) const
    {
        return val != other.val;
    }

    my_int operator+ (const my_int & other) const
    {
        return my_int(val + other.val);
    }

    bool operator<= (const my_int & other) const
    {
        return val <= other.val;
    }

};

int main()
{
    string user_input;
    my_int ct[71] = {my_int(43), my_int(33), my_int(54), my_int(36), my_int(57), my_int(11), my_int(29), my_int(48), my_int(39), my_int(35), my_int(46), my_int(46), my_int(59), my_int(29), my_int(42), my_int(45), my_int(50), my_int(39), my_int(29), my_int(54), my_int(42), my_int(43), my_int(49), my_int(29), my_int(39), my_int(44), my_int(38), my_int(49), my_int(29), my_int(55), my_int(50), my_int(29), my_int(32), my_int(39), my_int(43), my_int(44), my_int(37), my_int(29), my_int(54), my_int(42), my_int(39), my_int(29), my_int(48), my_int(43), my_int(37), my_int(42), my_int(54), my_int(29), my_int(35), my_int(47), my_int(45), my_int(55), my_int(44), my_int(54), my_int(29), my_int(45), my_int(36), my_int(29), my_int(33), my_int(45), my_int(47), my_int(50), my_int(46), my_int(43), my_int(33), my_int(35), my_int(54), my_int(39), my_int(38), my_int(63), my_int(66)};
    my_int dead = my_int(0);

    cout << ">>> ";
    getline(cin, user_input);

    for (my_int i = 0; i <= my_int(user_input.length()); i = i + my_int(1)) {
        if ((my_int(user_input[i.val])^ ct[i.val]) != my_int(0x42)) {
            dead = my_int(1);
        }
    }

    if (dead == my_int(1)) {
        cout << "Nope!" << endl;
    } else {
        cout << "Yup!" << endl;
    }
    
    return 0;
}