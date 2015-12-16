#pragma once

#include <list>
#include <vector>
#include <string>

inline bool IsNumber(const std::string& input)
{
    auto pos = input.find_first_of("0123456789");
    return (pos == 0);
}

//inline std::vector<std::string> ReadFromFile(const char* filename)
//{
//}

inline std::vector<std::string> Split(std::string _string, const char* key)
{
    std::vector<std::string> list;

    if (!_string.empty())
    {
        size_t pos = 0;
        do
        {
            size_t end = _string.find_first_of(key, pos);
            if (pos != end)
            {
                std::string part = _string.substr(pos, (end - pos));
                if (part.length() > 0)
                {
                    list.push_back(part);
                }
            }

            pos = end + 1;
        } while (pos != 0);
    }

    return list;
}
