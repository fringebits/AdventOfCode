#include "stdafx.h"
#include "CppUnitTest.h"
#include "StringHelper.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

// http://adventofcode.com/day/2

namespace 
{
    int ComputeWrappingPaper(int length, int width, int height)
    {
        auto a = length * width;
        auto b = width * height;
        auto c = height * length;

        auto area = 2 * a + 2 * b + 2 * c;
        auto extra = std::min(a, std::min(b, c));

        return area + extra;
    }

    int ComputeRibbon(int length, int width, int height)
    {
        auto a = 2 * (length + width);
        auto b = 2 * (width + height);
        auto c = 2 * (height + length);

        auto len = std::min(a, std::min(b, c));
        auto bow = length * width * height;

        return len + bow;
    }

    void ParseLine(const std::string& line, int& length, int& width, int& height)
    {
        auto args = Split(line, "x");
        length = atol(args[0].c_str());
        width = atol(args[1].c_str());
        height = atol(args[2].c_str());
    }

    int ComputeWrappingPaper(const std::string& line)
    {
        int length = 0;
        int width = 0;
        int height = 0;
        ParseLine(line, length, width, height);
        return ComputeWrappingPaper(length, width, height);
    }

    int ComputeRibbon(const std::string& line)
    {
        int length = 0;
        int width = 0;
        int height = 0;
        ParseLine(line, length, width, height);
        return ComputeRibbon(length, width, height);
    }
}

#include "Day02.h"

namespace AdventOfCode
{		
	TEST_CLASS(Day02)
	{
	public:
        TEST_METHOD(TestDay02)
        {
            Assert::AreEqual(58, ComputeWrappingPaper(2, 3, 4));
            Assert::AreEqual(58, ComputeWrappingPaper(4, 3, 2));
            Assert::AreEqual(43, ComputeWrappingPaper(1, 1, 10));

            int l, w, h;
            ParseLine("2x3x4", l, w, h);
            Assert::AreEqual(2, l);
            Assert::AreEqual(3, w);
            Assert::AreEqual(4, h);
            Assert::AreEqual(58, ComputeWrappingPaper(l, w, h));

            Assert::AreEqual(34, ComputeRibbon(l, w, h));
            Assert::AreEqual(14, ComputeRibbon("1x1x10"));
        }

        TEST_METHOD(Day02Part1)
        {
            int count = sizeof(InputData) / sizeof(std::string);
            Assert::AreEqual(1000, count);

            int total = 0;
            for (int ii = 0; ii < count; ii++)
            {
                int val = ComputeWrappingPaper(InputData[ii]);
                total += val;
            }

            Assert::AreEqual(1586300, total);
        }

        TEST_METHOD(Day02Part2)
        {
            int count = sizeof(InputData) / sizeof(std::string);
            Assert::AreEqual(1000, count);

            int total = 0;
            for (int ii = 0; ii < count; ii++)
            {
                int val = ComputeRibbon(InputData[ii]);
                total += val;
            }

            Assert::AreEqual(3737498, total);
        }
    };
}