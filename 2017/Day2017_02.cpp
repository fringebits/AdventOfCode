#include "stdafx.h"
#include "CppUnitTest.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    class Sheet : public std::vector<std::vector<int>> 
    {
    public:
        Sheet() { }
        Sheet(std::vector<std::vector<int>>& input)
        {
            reserve(input.size());
            for(auto&& row: input)
            {
                push_back(row);
            }
        }

        Sheet(TextFile& input)
        {
            reserve(input.size());
            for(auto&& row: input)
            {
                push_back(SplitInt(row));
            }
        }
    };

    int ComputeChecksum_Part1(const Sheet& sheet)
    {
        int result = 0;

        for(auto&& row: sheet)
        {
            int largest = INT_MIN;
            int smallest = INT_MAX;

            for(auto&& col: row)
            {
                largest = std::max(largest, col);
                smallest = std::min(smallest, col);
            }

            result += (largest - smallest);
        }

        return result;
    }
}

namespace AdventOfCode
{
    TEST_CLASS(Day2017_Day02)
    {
    public:
        TEST_METHOD(Day2017_02)
        {
            Sheet sheet(std::vector<std::vector<int>>({ { 5, 1, 9, 5 }, { 7, 5, 3 }, { 2, 4, 6, 8 } }));

            Assert::AreEqual(18, ComputeChecksum_Part1(sheet));
        }

        TEST_METHOD(Day2017_02Part1)
        {
            TextFile file("2017/InputData/Day2017_02.txt");
            Sheet sheet(file);

            Assert::AreEqual(-1, ComputeChecksum_Part1(sheet));
        }

        TEST_METHOD(Day2017_02Part2)
        {
            int result = -1;
            Assert::AreEqual(0, result);
        }
    };
}