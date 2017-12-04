#include "stdafx.h"
#include "CppUnitTest.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    bool IsValidPassword(std::string input);

    std::string NextPassword(std::string input)
    {
        do
        {
            size_t ii = input.size() - 1;
            
            while (true)
            {
                auto ch = input[ii];

                if (ch == 'z')
                {
                    input[ii] = 'a';
                    ii = ii - 1;
                    continue;
                }

                input[ii] = ch + 1;
                break;
            }

        } while (!IsValidPassword(input));

        return input;
    }

    bool IsValidPassword(std::string input)
    {
        // Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz.They cannot skip letters; abd doesn't count.
        // Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
        // Passwords must contain at least two pairs of letters, like aa, bb, or zz.
        bool hasStraight = false;
        int pairCount = 0;

        for (size_t ii = 0; ii < input.size(); ii++)
        {
            auto&& ch = input[ii];
            if ((ch == 'i') || (ch == 'l') || (ch == 'o'))
            {
                return false;
            }

            if (ii >= 1)
            {
                if ((input[ii - 1] == ch) && 
                    ((ii >= 2) && (input[ii - 2] != ch)))
                {
                    pairCount++;
                }
            }

            if (!hasStraight && (ii >= 2))
            {
                if ((input[ii - 1] == ch - 1) && (input[ii - 2] == ch - 2))
                {
                    hasStraight = true;
                }
            }
        }

        return hasStraight && pairCount >= 2;

    }
}

namespace AdventOfCode
{
    TEST_CLASS(Day11)
    {
    public:
        TEST_METHOD(TestDay11)
        {
            Assert::IsFalse(IsValidPassword("hijklmmn"));
            Assert::IsFalse(IsValidPassword("abbceffg"));
            Assert::IsTrue(IsValidPassword("abceffgg"));

            Assert::AreEqual(std::string("abcdffaa"), NextPassword("abcdefgh"));
        }

        TEST_METHOD(Day11Part1)
        {
            Assert::AreEqual(std::string("cqjxxyzz"), NextPassword("cqjxjnds"));
        }

        TEST_METHOD(Day11Part2)
        {
            auto ret = NextPassword("cqjxjnds");
            Assert::AreEqual(std::string("cqkaabcc"), NextPassword(ret));
        }
    };
}