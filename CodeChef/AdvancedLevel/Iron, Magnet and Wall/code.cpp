#include <iostream>
#include <vector>
using namespace std;


int main(){
    //diff approach
    int T,n,k,match,counter,p;
    string s;
    cin >> T;
    for (int i =0; i<T; i++) {
        cin >>n>>k;
        cin >>s;
        match = 0;
        counter = 0;
        vector<vector<int>> mag;
        vector<vector<int>> iron;
        for (int j = 0; j < s.length(); j++) {
            char c = s[j];
            if (c == '_') {
                continue;
            }
            else if (c == ':'){
                counter++;
            }
            else if (c == 'X'){
                mag.clear();
                iron.clear();
                counter = 0;
            }
            else if (c == 'M'){
                bool flagA = true;
                if (iron.size() == 0) {
                    mag.push_back({j,counter});
                    flagA = false;
                }
                else{
                    while (iron.size() != 0) {
                        p = k+1-abs(j-iron[0][0])-(counter-iron[0][1]);
                        if (p <= 0) {
                            iron.erase(iron.begin());
                        }
                        else{
                            iron.erase(iron.begin());
                            match++;
                            flagA = false;
                            break;
                        }
                    }
                }
                if(flagA){
                    mag.push_back({j,counter});
                }
            }
            else if (c == 'I'){
                // Pi,j = K+1−|i-j|−delta counter
                bool flagB = true;
                if (mag.size() == 0) {
                    iron.push_back({j,counter});
                    flagB = false;
                }
                while (mag.size() != 0) {
                    p = k+1-abs(j-mag[0][0])-(counter-mag[0][1]);
                    if (p <= 0) {
                        mag.erase(mag.begin());
                    }
                    else{
                        mag.erase(mag.begin());
                        match++;
                        flagB = false;
                        break;
                    }
                }
                if (flagB) {
                    iron.push_back({j,counter});
                }
            }

        }
        cout<<match<<endl;
    }
    return 0;
}
