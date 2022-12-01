#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

int main()
{
    string FILE_NAME = "input.txt";
    vector<int> data;

    ifstream inputFile(FILE_NAME);
    if (inputFile.is_open())
    {
        string line;
        vector<int> calories;
        while (getline(inputFile, line))
        {
            if (line.empty())
            {
                int sum = accumulate(calories.begin(), calories.end(), 0);
                data.push_back(sum);
                calories.clear();
            }
            else
            {
                calories.push_back(stoi(line));
            }
        }
        inputFile.close();
    }
    else
    {
        cout << "Unable to open file";
        return -1;
    }

    int max = *max_element(data.begin(), data.end());
    cout << max << endl;
}
