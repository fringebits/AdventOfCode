#include "stdafx.h"
#include "CppUnitTest.h"
#include "FileHelper.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    class Solution : public TextFile
    {
    public:
        Solution(const char* filename)
            : TextFile(filename)
        {
        }

        int PartOne()
        {
            int memory = 0;
            int count = 0;

            for (auto&& line : m_lines)
            {
                memory += line.size();
                count += DecodeString(line);
            }

            return memory - count;
        }

        int PartTwo()
        {
            int memory = 0;
            int count = 0;

            for (auto&& line : m_lines)
            {
                memory += line.size();
                count += EncodeString(line);
            }

            return count - memory;
        }


        int DecodeLine(size_t lineIndex)
        {
            return lineIndex < m_lines.size() ? DecodeString(m_lines[lineIndex]) : -1;
        }

        int EncodeLine(size_t lineIndex)
        {
            return lineIndex < m_lines.size() ? EncodeString(m_lines[lineIndex]) : -1;
        }

        // Part 1: Count characters of decoded string.
        static int DecodeString(const std::string& input)
        {
            int count = 0;
            for (int ii = 0; ii < input.size(); ii++)
            {
                auto&& ch = input[ii];
                if (ch == '"')
                {
                    continue;
                }
                else if (ch == '\\')
                {
                    auto peek = input[ii + 1];
                    if (peek == 'x')
                    {
                        ii += 3;
                        count++;
                    }
                    else
                    {
                        ii++;
                        count++;
                    }
                }
                else
                {
                    count++;
                }
            }

            return count;
        }

        // Part 2: Count characters of encoded size
        static int EncodeString(const std::string& input)
        {
            // Encode "" -> "\"\"" (2 -> 6) characters
            // Encode "abc" => "\"abc\"" (5 -> 9) characters

            int count = 2 + input.size();
            for (int ii = 0; ii < input.size(); ii++)
            {
                auto&& ch = input[ii];
                if (ch == '"')
                {
                    count++;
                }
                else if (ch == '\\')
                {
                    count++;
                }
            }
            return count;
        }


    };

}

namespace AdventOfCode
{
    TEST_CLASS(Day08)
    {
    public:
        TEST_METHOD(TestDay08)
        {
            Solution sln("../Day08Test.txt");
            Assert::AreEqual<size_t>(4, sln.LineCount());
            Assert::AreEqual(0, sln.DecodeLine(0));
            Assert::AreEqual(3, sln.DecodeLine(1));
            Assert::AreEqual(7, sln.DecodeLine(2));
            Assert::AreEqual(1, sln.DecodeLine(3));

            Assert::AreEqual(12, sln.PartOne());

            Assert::AreEqual(6, sln.EncodeLine(0));
            Assert::AreEqual(9, sln.EncodeLine(1));
            Assert::AreEqual(16, sln.EncodeLine(2));
            Assert::AreEqual(11, sln.EncodeLine(3));

            Assert::AreEqual(19, sln.PartTwo());
        }

        TEST_METHOD(Day08Part1)
        {
            Solution sln("../Day08.txt");
            Assert::AreEqual<size_t>(300, sln.LineCount());
          
            Assert::AreEqual(1371, sln.PartOne());
        }

        TEST_METHOD(Day08Part2)
        {
            Solution sln("../Day08.txt");
            Assert::AreEqual<size_t>(300, sln.LineCount());

            Assert::AreEqual(2117, sln.PartTwo());
        }
    };
}