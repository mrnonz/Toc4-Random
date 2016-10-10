#include <iostream>
#include "math.h"
#include <fstream>
#include <string>

using namespace std;

unsigned int PRNG()
{
    // our initial starting seed is 5323
    static unsigned int nSeed = 5323;

    // Take the current seed and generate a new value from it
    // Due to our use of large constants and overflow, it would be
    // very hard for someone to predict what the next number is
    // going to be from the previous one.
    nSeed = (8253729 * nSeed + 2396403);

    // Take the seed and return a value between 0 and 32767
    return nSeed  % 100000;
}


int main()
{
    int Number = pow(10, 5);
    int Randomtime = pow(10, 8);

    int data[100000] = {0};

    for (int i = 0 ; i < Randomtime; i++) {
        data[PRNG()%Number]++;
    }

    ofstream myfile;
    myfile.open ("/Users/MrNonz/Documents/CE/3D/Term1/Toc4-Random/data-4.txt");

    for (int i = 0; i < Number; i++) {
        string stri = to_string(i);
        string strdata = to_string(data[i]);

        std::string str;
        str.append(stri);
        str.append(" ");
        str.append(strdata);
        str.append("\n");

        myfile << str;
    }

    myfile.close();

}
