#include "stdafx.h"
#include "CppUnitTest.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

// http://adventofcode.com/day/5

namespace
{
    bool IsVowel(char ch)
    {
        return
            (ch == 'a') ||
            (ch == 'e') ||
            (ch == 'i') ||
            (ch == 'o') ||
            (ch == 'u');
    }

    bool IsBanned(char a, char b)
    {
        return
            (a == 'a' && b == 'b') ||
            (a == 'c' && b == 'd') ||
            (a == 'p' && b == 'q') ||
            (a == 'x' && b == 'y');
    }

    bool StringIsNice(const std::string& input)
    {
        int vowelCount = 0;
        bool hasRepeatingLetter = false;
        char pc = 0;

        for (auto&& ch : input)
        {
            if (IsVowel(ch))
            {
                vowelCount++;
            }
            if (pc == ch)
            {
                hasRepeatingLetter = true;
            }

            if (IsBanned(pc, ch))
            {
                return false;
            }

            pc = ch;
        }

        return vowelCount >= 3 && hasRepeatingLetter;
    }

    // Part 2
    bool StringIsReallyNice(const std::string& input)
    {
        // Search for Camel Count
        int camelCount = 0;
        for (auto ii = 2u; ii < input.length(); ii++)
        {
            // Evaluate for aba or aaa
            if (input[ii - 2] == input[ii])
            {
                // This is a 'camelCount'
                camelCount++;
            }
        }

        if (camelCount == 0)
        {
            return false;
        }

        // Look for pair of two letters that appear twice in the string without overlapping.
        for (size_t ii = 1; ii < input.length(); ii++)
        {
            auto A = input[ii - 1];
            auto B = input[ii];

            for (size_t jj = ii + 2; jj < input.length(); jj++)
            {
                if (A == input[jj-1] && B == input[jj])
                {
                    return true;
                }
            }
        }

        return false;
    }

}

#include "Day05.h"

namespace AdventOfCode
{
    TEST_CLASS(Day05)
    {
    public:
        TEST_METHOD(TestDay05)
        {
            // Test Part 1
            Assert::IsTrue(StringIsNice("ugknbfddgicrmopn"));
            Assert::IsTrue(StringIsNice("aaa"));
            Assert::IsFalse(StringIsNice("jchzalrnumimnmhp"));
            Assert::IsFalse(StringIsNice("haegwjzuvuyypxyu"));
            Assert::IsFalse(StringIsNice("dvszwmarrgswjxmb"));

            // Test Part 2
            Assert::IsTrue(StringIsReallyNice("efef"));
            Assert::IsTrue(StringIsReallyNice("qjhvhtzxzqqjkmpb"));
            Assert::IsTrue(StringIsReallyNice("xxyxx"));
            Assert::IsFalse(StringIsReallyNice("uurcxstgmygtbstg"));
            Assert::IsFalse(StringIsReallyNice("ieodomkazucvgmuy"));
        }

        TEST_METHOD(Day05Part1)
        {
            int result = 0;
            Assert::AreEqual(1000u, InputData.size());

            for (auto&& line : InputData)
            {
                if (StringIsNice(line))
                {
                    result++;
                }
            }

            Assert::AreEqual(238, result);
        }

        TEST_METHOD(Day05Part2)
        {
            int result = 0;
            Assert::AreEqual(1000u, InputData.size());

            for (auto&& line : InputData)
            {
                if (StringIsReallyNice(line))
                {
                    result++;
                }
            }

            Assert::AreEqual(69, result);
        }
    };
}
