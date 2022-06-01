#include <iostream>
#include<string>
using namespace std;

int main()
{
  string alp[2][3] = {
    {"A", "B", "C"},
    {"D", "E", "F"}
  };
  
  for(int i = 0; i < 2; i++) {
    for(int j = 0; j < 3; j++) {
      cout <<alp[i][j] << "\n";
    }
  }
  return 0;
}