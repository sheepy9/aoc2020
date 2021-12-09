#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main()
{
    // READ AND PARSE TEXT
    std::ifstream infile("timetable");
    std::string data;
    std::vector<int> busIds;
    std::vector<int> offsets;

    // don't need first line
    infile >> data;
    infile >> data;

    int index = 0;
    std::string num;
    for(int i = 0; i < data.length(); i++)
    {
        if(data[i] == ',')
        {
            if(num == "")
                continue;
            std::cout << num << std::endl;
            busIds.push_back(std::stoi(num));
            offsets.push_back(index);
            num = "";
            index++;
        }
        else if(data[i] == 'x')
            index++;
        else
            num.push_back(data[i]);
    }
    if(data[data.length()-1] != 'x')
    {
        busIds.push_back(std::stoi(num));
        offsets.push_back(index);
    }


    // find max ID
    int max= 0;
    int max_index = 0;
    for(int i=0; i<busIds.size(); i++)
        if(busIds[i] > max)
        {
            max = busIds[i];
            max_index = i;
        }

    std::cout << busIds[max_index];

    unsigned long long multiplier = 1;
    unsigned long long myTime = 0;
    myTime = multiplier*busIds[max_index]-offsets[max_index];
    while(true)
    {
        myTime = myTime + busIds[max_index];
        // check if other busses are ok
        bool foundTime = true;
        for(int i=0; i<busIds.size(); i++)
        {
            if((myTime+offsets[i])%busIds[i])
            {
                foundTime = false;
                break;
            }
        }

        if(foundTime)
            break;

        multiplier++;
    }

    std::cout << "Found time is: " << myTime << std::endl;

    // DEBUG
    for(int i = 0; i < busIds.size(); i++)
        std::cout << busIds[i] << ",";

    std::cout << std::endl;
    for(int i = 0; i < offsets.size(); i++)
        std::cout << offsets[i] << ",";
    std::cout << std::endl;

    return 0;
}