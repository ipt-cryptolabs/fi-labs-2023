#include <iostream>
#include <fstream>
#include <vector>
#include <cwctype>
#include <map>
#include <wchar.h>
#include <cmath>

using namespace std;

wstring cleanText()
{
    std::wifstream inputFile("../text/text1.txt");

    std::locale loc("ru_RU.UTF-8");
    inputFile.imbue(loc);


    std::wcout.imbue(loc);
    std::wcout.setf(std::ios::boolalpha);

    std::wstring line;
    std::wstring text = L"";
    while (std::getline(inputFile, line))
    {
        for (auto c : line)
        {
            if (((c >= L'a' && c <= L'я') || c == L' ') && !(c>='a' && c<='z')
            && c!=L'©' && c!=L'«'&& c!= L'»' && c != L'á' && c != L'é' && c != L'ê' && c!=L'½')
            {
                text += static_cast<wchar_t >(std::towlower(c));
            }else if(c == L'-')
                text += L' ';
        }
        text += L' ';
    }
    inputFile.close();
    bool space = false;
    wstring formatted = L"";
    for(auto c : text)
    {
        if(c == L' ' && space == false)
        {
            space = true;
            formatted += ' ';
            continue;
        }

        if(c != L' ')
        {
            space = false;
            formatted += c;
        }
    }

    return formatted;
}

void H1(const wstring& text)
{
    map<wchar_t, int> gram;
    wcout<<'\n';
    for (auto c : text)
    {
        if(c != L' ')
            ++gram[c];
    }
    long long sum = 0;
    for (const auto& [key, value] : gram) {
        std::wcout << key << ": " << value << std::endl;
        sum+=value;
    }
    wcout<<'\n';
    double h1 = 0;
    for (const auto& [key, value] : gram) {
        double p = (double)value/(double)sum;
        h1 += p*log2(p);
    }
    h1 = (-1)*h1;
    wcout<<"H1 = "<<h1;
    wcout<<'\n';
}

wstring clearSpaces(const wstring& text)
{
    wstring result = L"";
    for (auto c : text)
    {
        if(c != L' ')
            result += c;
    }

    return result;
}


void H2(const wstring& text,const wstring& textWithoutSpaces)
{
    map<wstring, int> bigram;
    map<wstring, int> bigramWithoutSpaces;
    wcout<<'\n';
    wcout<<L"Біграми з перетином літер:\n";
    for(int i = 0; i < text.size() - 1; ++i)
    {
        if(text[i] != L' ' && text[i+1]!=L' ')
        {
            wchar_t* a = new wchar_t(text[i]);
            wchar_t* b = new wchar_t (text[i+1]);
            wstring tmp = static_cast<wstring>(a)+ static_cast<wstring>(b);
            bigram[tmp]++;
            delete a;
            delete b;
        }
    }
    wcout<<'\n';
    long long sum = 0;
    for (const auto& [key, value] : bigram) {
        std::wcout << key << ": " << value << std::endl;
        sum+=value;
    }

    wcout<<'\n';
    double h2 = 0;
    for (const auto& [key, value] : bigram) {
        double p = (double)value/(double)sum;
        h2 += p*log2(p);
    }
    h2 = (-1)*h2;
    wcout<<"H2 = "<<h2/2<<'\n';

    wcout<<L"Біграми без перетину літер:\n";
    for(int i = 0; i < textWithoutSpaces.size() - 1; ++i)
    {
        wchar_t* a = new wchar_t(textWithoutSpaces[i]);
        wchar_t* b = new wchar_t (textWithoutSpaces[i+1]);
        wstring tmp = static_cast<wstring>(a)+ static_cast<wstring>(b);
        bigramWithoutSpaces[tmp]++;
        delete a;
        delete b;
    }

    wcout<<'\n';
    sum = 0;
    for (const auto& [key, value] : bigramWithoutSpaces) {
        std::wcout << key << ": " << value << std::endl;
        sum += value;
    }
    wcout<<'\n';
    h2 = 0;
    for (const auto& [key, value] : bigramWithoutSpaces) {
        double p = (double)value/(double)sum;
        h2 += p*log2(p);
    }
    h2 = (-1)*h2;
    wcout<<"H2 = "<<h2/2<<'\n';

}



int main()
{
    setlocale(LC_ALL, "ru_RU.UTF-8");

    wstring cleaned = cleanText();
    H1(cleaned);
    H2(cleaned, clearSpaces(cleaned));


    return 0;
}
