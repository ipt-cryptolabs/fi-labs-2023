#include <iostream>
#include <fstream>
#include <vector>
#include <cwctype>
#include <map>
#include <wchar.h>

using namespace std;

wstring cleanText()
{
    std::wifstream inputFile("../text/text1.txt");

    std::locale loc("ru_RU.UTF-8");
    inputFile.imbue(loc);


    std::wcout.imbue(loc);
    std::wcout.setf(std::ios::boolalpha);

    std::wstring line;
    std::wstring formattedText = L"";
    while (std::getline(inputFile, line)) {
        // Виводити лише символи кирилиці від 'а' до 'я' та пробіли
        for (auto c : line)
        {
            if (((c >= L'a' && c <= L'я') || c == L' ') && !(c>='a' && c<='z')
            && c!=L'©' && c!=L'«'&& c!= L'»' && c != L'á' && c != L'é' && c != L'ê' && c!=L'½')
            {
                formattedText += static_cast<wchar_t >(std::towlower(c));
            }
            //std::wcout << c;
        }
        formattedText += L' ';
    }
    inputFile.close();

    std::wcout << formattedText;
    return formattedText;

}


int main()
{
    setlocale(LC_ALL, "ru_RU.UTF-8");
    std::locale loc("ru_RU.UTF-8");
    wstring cleaned = cleanText();
    map<wchar_t, int> gram;
    map<wstring, int> bigram;
    wcout<<'\n';
    for (auto c : cleaned)
    {
        if(c != L' ')
            ++gram[c];
    }

    for (const auto& [key, value] : gram) {
        std::wcout << key << ": " << value << std::endl;
    }
    for(int i = 0; i < cleaned.size(); ++i)
    {
        if(cleaned[i] != L' ' && cleaned[i+1]!=L' ')
        {
            wchar_t* a = new wchar_t(cleaned[i]);
            wchar_t* b = new wchar_t (cleaned[i+1]);
            wstring tmp = static_cast<wstring>(a)+ static_cast<wstring>(b);
            bigram[tmp]++;
            delete a;
            delete b;
        }
    }
    wcout<<'\n';
    for (const auto& [key, value] : bigram) {
        std::wcout << key << ": " << value << std::endl;
    }
    //std::wcout << result << std::endl;
    //cleanText("text.txt");

    return 0;
}
