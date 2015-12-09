#include "stdafx.h"
#include "CppUnitTest.h"
#include "HelperMd5.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    int MineAdventCoins(const std::string& code)
    {
        MD5 hash;
        int key = 0;

        while (true)
        {
            std::ostringstream os;
            os << code << key;
            hash.Compute(os.str());

            if ((hash.digest[0] == '0') &&
                (hash.digest[1] == '0') &&
                (hash.digest[2] == '0') &&
                (hash.digest[3] == '0') &&
                (hash.digest[4] == '0'))
            {
                break;
            }

            key++;
        }

        return key;
    }

    int MineAdventCoinsPart2(const std::string& code)
    {
        MD5 hash;
        int key = 0;

        while (true)
        {
            std::ostringstream os;
            os << code << key;
            hash.Compute(os.str());

            if ((hash.digest[0] == '0') &&
                (hash.digest[1] == '0') &&
                (hash.digest[2] == '0') &&
                (hash.digest[3] == '0') &&
                (hash.digest[4] == '0') && 
                (hash.digest[5] == '0'))
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