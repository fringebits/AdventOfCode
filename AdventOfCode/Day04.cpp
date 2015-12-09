#include "stdafx.h"
#include "CppUnitTest.h"
#include "Md5Helper.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

// http://adventofcode.com/day/4

// Todo: I really don't like the brute force approach, but it works.
// Starting the key off for each of these with at least the number of 
// zeros we're looking for will satisfy the problem but I haven't taken
// the time to come up with a proof.

namespace
{
    int MineAdventCoins(const std::string& code)
    {
        int key = 0; // Can I start this early; like: 100000 (5 zeros)
        MD5 start;
        start.Init();
        start.Update(reinterpret_cast<const unsigned char*>(code.c_str()), code.size());

        while (true)
        {
            MD5 hash = start;
            std::ostringstream os;
            os << key;
            auto&& value = os.str();

            hash.Update(reinterpret_cast<const unsigned char*>(value.c_str()), value.size());
            hash.Final();

            if ((hash.digestRaw[0] == 0) && // two digits
                (hash.digestRaw[1] == 0) && // two more digitis
                (hash.digestRaw[2] < 0x10)) // last digit
            {
                break;
            }

            key++;
        }

        return key;
    }

    int MineAdventCoinsPart2(const std::string& code)
    {
        int key = 0; // Can I start this early; like: 1000000 (6 zeros)
        MD5 start;
        start.Init();
        start.Update(reinterpret_cast<const unsigned char*>(code.c_str()), code.size());

        while (true)
        {
            MD5 hash = start;
            std::ostringstream os;
            os << key;
            auto&& value = os.str();

            hash.Update(reinterpret_cast<const unsigned char*>(value.c_str()), value.size());
            hash.Final();

            if ((hash.digestRaw[0] == 0) && // two digits
                (hash.digestRaw[1] == 0) && // two more digitis
                (hash.digestRaw[2] == 0)) // last digit
            {
                break;
            }

            key++;
        }

        return key;
    }

}

namespace AdventOfCode
{
    TEST_CLASS(Day04)
    {
    public:
        TEST_METHOD(TestDay04)
        {
            auto ret = MineAdventCoins("abcdef");
            Assert::AreEqual(609043, ret);

            ret = MineAdventCoins("pqrstuv");
            Assert::AreEqual(1048970, ret);
        }

        TEST_METHOD(Day04Part1)
        {
            int result = MineAdventCoins("bgvyzdsv");
            Assert::AreEqual(254575, result);
        }

        TEST_METHOD(Day04Part2)
        {
            int result = MineAdventCoinsPart2("bgvyzdsv");
            Assert::AreEqual(1038736, result);
        }
    };
}