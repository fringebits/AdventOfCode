#pragma once

#include <string>
#include <list>

namespace Microsoft 
{
    namespace VisualStudio 
    {
        namespace CppUnitTestFramework 
        {
            template<> std::wstring ToString<int64_t>(const int64_t& q)
            {
                std::wstringstream stream;
                stream << q;
                return stream.str();
            }

            template<> std::wstring ToString<uint16_t>(const uint16_t& q)
            {
                std::wstringstream stream;
                stream << q;
                return stream.str();
            }

            template<> std::wstring ToString<std::list<int>>(const std::list<int>& q)
            {
                return std::wstring(L"X");
            }
        }
    }
}
