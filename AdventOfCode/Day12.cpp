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

    int ParseArray(std::string input)
    {
        // [ ]
        Assert::AreEqual('[', input[0]);
        Assert::AreEqual(']', input.back());
        
        auto tokens = Split(input.substr(1, input.size() - 2), ",");
        std::vector<std::string> kvp;

        for (auto&& tok : tokens)
        {
            //if (tok[0] == '[')
            //{
            //    ParseArray(tok);
            //}
            //else if (tok[0] == '{')
            //{
            //    ParseObject(tok);
            //}
            //else
            //{
            //    kvp.push_back(tok);
            //}
        }
    }

    int ParseObject(std::string input)
    {
        // { }
        Assert::AreEqual('{', input[0]);
        Assert::AreEqual('}', input.back());

        auto tokens = Split(input.substr(1, input.size()-2), ",");
        std::vector<std::string> kvp;

        for (auto&& tok : tokens)
        {
            if (tok[0] == '[')
            {
                ParseArray(tok);
            }
            else if (tok[0] == '{')
            {
                ParseObject(tok);
            }
            else
            {
                kvp.push_back(tok);
            }
        }
    }

    int ParseString(std::string input)
    {
        // string should start with '[' or '{'

        if (input[0] == '[')
        {
            ParseArray(input);
        }
        else if (input[0] = '{')
        {
            ParseObject(input);
        }

        int depth = 0;
        int result = 0;
        size_t pos = 0;

        while (pos < input.size())
        {
            if (input[pos] == '[')
            {
            }
            else if (input[pos] == ']')
            {
            }
        }

        return result;
    }


}

namespace AdventOfCode
{
    TEST_CLASS(Day12)
    {
    public:
        TEST_METHOD(TestDay12)
        {
            Assert::AreEqual(6, SumNumbers("[1, 2, 3]")); // and {"a":2, "b" : 4}
            Assert::AreEqual(0, SumNumbers("[1, 2, -3]")); // and {"a":2, "b" : 4}
            Assert::AreEqual(10, SumNumbers("[1, 2, -3, 10]")); // and {"a":2, "b" : 4}
        }

        TEST_METHOD(Day12Part1)
        {

            TextFile file("../InputData/Day12.txt");
            Assert::AreEqual<size_t>(1, file.LineCount());
            int result = 0;
            for (auto&& line : file)
            {
                result += SumNumbers(line);
            }
            Assert::AreEqual(0, result);
        }

        TEST_METHOD(Day12Part2)
        {
            int result = -1;
            Assert::AreEqual(0, result);
        }
    };
}
