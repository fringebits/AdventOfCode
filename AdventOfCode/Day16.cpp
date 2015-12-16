#include "stdafx.h"
#include "CppUnitTest.h"
#include "Nullable.h"
#include "StringHelper.h"
#include "FileHelper.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    static std::map<std::string, size_t> NameIndex = {
        { "children", 0 },
        { "cats", 1 },
        { "samoyeds", 2 },
        { "pomeranians", 3},
        { "akitas", 4 },
        { "vizslas", 5 },
        { "goldfish", 6 },
        { "trees", 7 },
        { "cars", 8 },
        { "perfumes", 9 },
    };

    typedef Nullable<int> Nint;

    struct AuntSue {
        std::vector<Nint> m_data;

        AuntSue() {
            m_data.resize(10);
        }

        AuntSue(const char* input) {
            m_data.resize(10);
            Parse(std::string(input));
        }

        AuntSue(std::vector<Nint> data)
            : m_data(data)
        {
        }


        int Parse(std::string line)
        {
            //Sue 1: goldfish: 6, trees : 9, akitas : 0

            auto args = Split(line, " :,");
            auto index = atol(args[1].c_str());
            for (auto ii = 2u; ii < args.size(); ii += 2)
            {
                m_data[NameIndex[args[ii]]] = atol(args[ii + 1].c_str());
            }
            return index;
        }

        bool IsPart1Match(AuntSue& ref)
        {
            Assert::AreEqual(m_data.size(), ref.m_data.size());
            for (auto ii = 0u; ii < m_data.size(); ii++)
            {
                Assert::IsTrue(m_data[ii].HasValue());
                if (!ref.m_data[ii].HasValue())
                {
                    continue;
                }
                if (m_data[ii].Value != ref.m_data[ii].Value)
                {
                    return false;
                }
            }

            return true;
        }

        bool IsPart2Match(AuntSue& ref)
        {
            Assert::AreEqual(m_data.size(), ref.m_data.size());
            for (auto ii = 0u; ii < m_data.size(); ii++)
            {
                Assert::IsTrue(m_data[ii].HasValue());
                if (!ref.m_data[ii].HasValue())
                {
                    continue;
                }
                switch (ii)
                {
                case 1:
                case 7:
                    //greater
                    if (ref.m_data[ii].Value <= m_data[ii].Value)
                    {
                        return false;
                    }
                    break;

                case 3:
                case 6:
                    // less than
                    if (ref.m_data[ii].Value >= m_data[ii].Value)
                    {
                        return false;
                    }
                    break;

                default:
                    if (m_data[ii].Value != ref.m_data[ii].Value)
                    {
                        return false;
                    }
                    break;
                }
            }

            return true;
        }
    };

}

namespace AdventOfCode
{
    TEST_CLASS(Day16)
    {
    public:
        TEST_METHOD(TestDay16)
        {
            AuntSue key({ 3, 7, 2, 3, 0, 0, 5, 3, 2, 1 });

            //children: 3, cats : 7, samoyeds : 2
          /*  pomeranians : 3
            akitas : 0
            vizslas : 0
            goldfish : 5
            trees : 3
            cars : 2
            perfumes : 1
          */  
            Assert::IsTrue(key.IsPart1Match(AuntSue("Sue 0: children: 3, cats : 7, samoyeds : 2")));
            //Assert::IsTrue(false);
        }

        TEST_METHOD(Day16Part1)
        {
            int result = 0;
            AuntSue key({ 3, 7, 2, 3, 0, 0, 5, 3, 2, 1 });
            TextFile file("../InputData/Day16.txt");
            for (auto&& line : file)
            {
                AuntSue c;
                result = c.Parse(line);
                if (key.IsPart1Match(c))
                {
                    break;
                }
            }

            Assert::AreEqual(103, result);
        }

        TEST_METHOD(Day16Part2)
        {
            int result = 0;
            AuntSue key({ 3, 7, 2, 3, 0, 0, 5, 3, 2, 1 });
            TextFile file("../InputData/Day16.txt");
            for (auto&& line : file)
            {
                AuntSue c;
                result = c.Parse(line);
                if (key.IsPart2Match(c))
                {
                    break;
                }
            }

            Assert::AreEqual(0, result);
        }
    };
}