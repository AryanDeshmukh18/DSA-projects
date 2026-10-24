
#include <chrono>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <limits>

using namespace std;
using namespace std::chrono;

struct Student
{
    int roll_no;
    string name;
    float CGPA;
};

vector<Student> students;

void addStudent()
{
    int n;

    cout << "How many students do you want to add: ";
    if (!(cin >> n) || n <= 0)
    {
        cout << "Invalid number of students.\n";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        return;
    }

    for (int i = 0; i < n; ++i)
    {
        Student s;

        cout << "\nEnter details for student "
             << students.size() + 1 << ":\n";

        cout << "Roll no: ";
        if (!(cin >> s.roll_no))
        {
            cout << "Invalid roll number. Operation stopped.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return;
        }

        cout << "Name: ";
        getline(cin >> ws, s.name);

        cout << "CGPA: ";
        if (!(cin >> s.CGPA) || s.CGPA < 0 || s.CGPA > 10)
        {
            cout << "Invalid CGPA. Enter a value from 0 to 10.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return;
        }

        students.push_back(s);
    }
}

void displayStudents()
{
    if (students.empty())
    {
        cout << "No student records available.\n";
        return;
    }

    cout << "\nRoll No\tName\t\tCGPA\n";

    for (const auto& student : students)
    {
        cout << student.roll_no << "\t"
             << student.name << "\t\t"
             << student.CGPA << '\n';
    }
}

void sortByName()
{
    if (students.empty())
    {
        cout << "No student records to sort.\n";
        return;
    }

    sort(students.begin(), students.end(),
         [](const Student& a, const Student& b)
         {
             return a.name < b.name;
         });

    cout << "Sorted by Name.\n";
}

void sortByCGPA(bool ascending = true)
{
    if (students.empty())
    {
        cout << "No student records to sort.\n";
        return;
    }

    sort(students.begin(), students.end(),
         [ascending](const Student& a, const Student& b)
         {
             if (ascending)
                 return a.CGPA < b.CGPA;

             return a.CGPA > b.CGPA;
         });

    cout << "Sorted by CGPA ("
         << (ascending ? "Ascending" : "Descending")
         << ").\n";
}

void sortByRollNo()
{
    if (students.empty())
    {
        cout << "No student records to sort.\n";
        return;
    }

    sort(students.begin(), students.end(),
         [](const Student& a, const Student& b)
         {
             return a.roll_no < b.roll_no;
         });

    cout << "Sorted by Roll Number.\n";
}

void linearSearch(int key)
{
    auto start = high_resolution_clock::now();

    for (const auto& student : students)
    {
        if (student.roll_no == key)
        {
            auto end = high_resolution_clock::now();

            cout << "Student Found: " << student.name
                 << ", CGPA: " << student.CGPA << '\n';

            cout << "Linear Search Time: "
                 << duration_cast<nanoseconds>(
                        end - start).count()
                 << " ns\n";
            return;
        }
    }

    auto end = high_resolution_clock::now();

    cout << "Student not found (Linear Search).\n";
    cout << "Linear Search Time: "
         << duration_cast<nanoseconds>(
                end - start).count()
         << " ns\n";
}

void binarySearch(int key)
{
    if (students.empty())
    {
        cout << "No students available for binary search.\n";
        return;
    }

    // Create a sorted copy so the original order is preserved.
    vector<Student> sortedStudents = students;

    sort(sortedStudents.begin(), sortedStudents.end(),
         [](const Student& a, const Student& b)
         {
             return a.roll_no < b.roll_no;
         });

    auto start = high_resolution_clock::now();

    int low = 0;
    int high = static_cast<int>(sortedStudents.size()) - 1;

    while (low <= high)
    {
        int mid = low + (high - low) / 2;

        if (sortedStudents[mid].roll_no == key)
        {
            auto end = high_resolution_clock::now();

            cout << "Student Found: "
                 << sortedStudents[mid].name
                 << ", CGPA: " << sortedStudents[mid].CGPA << '\n';

            cout << "Binary Search Time: "
                 << duration_cast<nanoseconds>(
                        end - start).count()
                 << " ns\n";
            return;
        }

        if (key < sortedStudents[mid].roll_no)
            high = mid - 1;
        else
            low = mid + 1;
    }

    auto end = high_resolution_clock::now();

    cout << "Student not found (Binary Search).\n";
    cout << "Binary Search Time: "
         << duration_cast<nanoseconds>(
                end - start).count()
         << " ns\n";
}

int main()
{
    int choice;

    do
    {
        cout << "\n--- Student Management System ---\n";
        cout << "1. Add Student\n";
        cout << "2. Display Students\n";
        cout << "3. Sort by Name\n";
        cout << "4. Sort by CGPA\n";
        cout << "5. Sort by Roll Number\n";
        cout << "6. Linear Search\n";
        cout << "7. Binary Search\n";
        cout << "0. Exit\n";
        cout << "Enter your choice: ";

        if (!(cin >> choice))
        {
            cout << "Invalid input. Please enter a number.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        switch (choice)
        {
            case 1:
                addStudent();
                break;

            case 2:
                displayStudents();
                break;

            case 3:
                sortByName();
                break;

            case 4:
                sortByCGPA(true);
                break;

            case 5:
                sortByRollNo();
                break;

            case 6:
            case 7:
            {
                int key;

                cout << "Enter roll number to search: ";

                if (!(cin >> key))
                {
                    cout << "Invalid roll number.\n";
                    cin.clear();
                    cin.ignore(
                        numeric_limits<streamsize>::max(), '\n');
                    break;
                }

                if (choice == 6)
                    linearSearch(key);
                else
                    binarySearch(key);

                break;
            }

            case 0:
                cout << "Exiting program.\n";
                break;

            default:
                cout << "Invalid choice.\n";
        }

    } while (choice != 0);

    return 0;
}
