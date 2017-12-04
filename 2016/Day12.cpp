#include "stdafx.h"
#include "CppUnitTest.h"
#include "FileHelper.h"
#include "StringHelper.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    int SumNumbers(std::string input)
    {
        int sum = 0;
        auto pos = input.find_first_of("-1234567890");
        while (pos != std::string::npos)
        {
            char* mark = nullptr;
            auto val = strtol(&input[pos], &mark, 10);
            sum += val;
            pos += (mark - &input[pos]); // this is a problem if mark is null.
            pos = input.find_first_of("-1234567890", pos);
        }
        return sum;
    }

    size_t FindPreviousBrace(const std::string& input, size_t pos)
    {
        int depth = 0;
        while (pos != 0)
        {
            if (input[pos] == '}')
            {
                depth++;
            }
            if (input[pos] == '{')
            {
                depth--;
                if (depth == -1)
                    return pos;
            }
            pos--;
        }
        return pos;
    }

    size_t FindNextBrace(const std::string& input, size_t pos)
    {
        int depth = 0;
        while (pos < input.size())
        {
            if (input[pos] == '{')
            {
                depth++;
            }
            if (input[pos] == '}')
            {
                depth--;
                if (depth == -1)
                    return pos;
            }
            pos++;
        }
        return pos;
    }

    int SumNumbersWithoutRed(std::string input)
    {
        size_t pos = 0;
        while (std::string::npos != (pos = input.find(":\"red\"")))
        {
            // we've found a 'red' property.  Find the parent 
            auto tip = FindPreviousBrace(input, pos);
            auto tail = FindNextBrace(input, pos);
            input = input.substr(0, tip) + std::string("X") + input.substr(tail+1);
        }

        return SumNumbers(input);
    }
}

namespace AdventOfCode
{
    TEST_CLASS(Day12)
    {
    public:
        TEST_METHOD(TestDay12)
        {
            Assert::AreEqual(6, SumNumbers("[1, 2, 3]"));
            Assert::AreEqual(0, SumNumbers("[1, 2, -3]"));
            Assert::AreEqual(10, SumNumbers("[1, 2, -3, 10]"));

            TextFile file("../InputData/Day12.txt");
            Assert::AreEqual(28, SumNumbers(file.at(1)));
            Assert::AreEqual(5, SumNumbersWithoutRed(file.at(1)));
            Assert::AreEqual(5, SumNumbersWithoutRed(file.at(2)));
        }

        TEST_METHOD(Day12Part1)
        {
            TextFile file("../InputData/Day12.txt");
            auto result = SumNumbers(file.at(0));
            Assert::AreEqual(111754, result);
        }

        TEST_METHOD(Day12Part2)
        {
            TextFile file("../InputData/Day12.txt");
            auto result = SumNumbersWithoutRed(file.at(0));
            Assert::AreEqual(65402, result);
        }
    };
}
