#include <iostream>
#include <string>
using namespace std;

class Teacher {
private:
        double salary;    
public:
    string name;
    string dept;
    string subject;

    void changeDept(string newDept) {
        dept = newDept;
    }
//setter
    void setSalary(double s){
         salary = s;
}
//getter 
    double getsalary(){
         return salary;
    }
};


int main() {
    Teacher t1;
    t1.name = "Prince";
    t1.subject = "C++";
    t1.dept = "Computer Science";
    t1.setSalary(25000);

    cout << t1.name << endl;
   
    
    cout << t1.getsalary () << endl;
    


    return 0;
}
