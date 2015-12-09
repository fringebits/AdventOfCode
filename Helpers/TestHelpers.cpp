#include "stdafx.h"
#include "CppUnitTest.h"
#include "Md5Helper.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace AdventOfCode
{
    TEST_CLASS(TestHelpers)
    {
    public:
        TEST_METHOD(TestMd5)
        {
            MD5 hash;

            hash.Compute("");
            Assert::AreEqual(hash.writeToString(), std::string("d41d8cd98f00b204e9800998ecf8427e"));

            hash.Compute("The quick brown fox jumps over the lazy dog");
            Assert::AreEqual(hash.writeToString(), std::string("9e107d9d372bb6826bd81d3542a419d6"));

            hash.Compute("The quick brown fox jumps over the lazy dog.");
            Assert::AreEqual(hash.writeToString(), std::string("e4d909c290d0fb1ca068ffaddf22cbd0"));
        }
    };
}