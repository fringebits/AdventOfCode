#include "stdafx.h"
#include "CppUnitTest.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    std::vector<int> LookAndSay(std::vector<int> input)
    {
        Assert::IsFalse(input.empty());

        std::vector<int> result;
        std::pair<int, int> run(0, input.front());

        for(auto&& digit: input)
        {
            if (run.second == digit)
            {
                // Extend current run.
                run.first++;
            }
            else
            {
                // Finish current run.
                result.emplace_back(run.first); // the count
                result.emplace_back(run.second); // the digit
                
                // We're starting a new run.
                run = std::pair<int, int>(1, digit);
            }
        }

        // Finish final run.
        Assert::IsTrue(run.first != 0);
        result.emplace_back(run.first); // the count
        result.emplace_back(run.second); // the digit

        return result;
    }
}

namespace AdventOfCode
{
    TEST_CLASS(Day10)
    {
    public:
        TEST_METHOD(TestDay10)
        {
            auto ret = LookAndSay({ 1 });
            Assert::AreEqual(2u, ret.size());

            ret = LookAndSay(ret);
            Assert::AreEqual(2u, ret.size());
        }

        TEST_METHOD(Day10Part1)
        {
            std::vector<int> ret = { 1, 1, 1, 3, 1, 2, 2, 1, 1, 3 };
            for (int ii = 0; ii < 40; ii++)
            {
                ret = LookAndSay(ret);
            }

            auto result = ret.size();
            Assert::AreEqual(360154u, result);
        }

        TEST_METHOD(Day10Part2)
        {
            std::vector<int> ret = { 1, 1, 1, 3, 1, 2, 2, 1, 1, 3 };
            for (int ii = 0; ii < 50; ii++)
            {
                ret = LookAndSay(ret);
            }

            auto result = ret.size();
            Assert::AreEqual(5103798u, result);
        }
    };
}