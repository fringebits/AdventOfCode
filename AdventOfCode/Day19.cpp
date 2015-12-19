#include "stdafx.h"
#include "CppUnitTest.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    class Fusion
    {
        std::map<std::string, std::vector<std::string>> g_fusionMap;
        std::string m_input;

        int SantaFusion(std::string input)
        {
            std::list<std::string> list;
            for (auto ii = 0u; ii != input.size(); ii++)
            {
                auto&& ch = input[ii];
                if (g_fusionMap.end() != g_fusionMap.find(ch))
                {
                    for (auto&& r : g_fusionMap[ch])
                    {
                        auto f = input.substr(0, ii) + r + input.substr(ii + 1);
                        list.push_back(f);
                    }
                }
            }

            list.sort();
            list.unique();

            return list.size();
        }

        void Parse(std::string filename)
        {
            TextFile file(filename.c_str());
            for (auto&& line : file)
            {
                auto args = Split(line, " =>");

                if (args.size() == 1)
                {
                    m_input = line;
                    continue;
                }

                g_fusionMap[args[0]].push_back(args[1]);
            }
        }
    };
}

namespace AdventOfCode
{
    TEST_CLASS(Day19)
    {
    public:
        Day19()
        {
            g_fusionMap['H'] = { "HO", "OH" };
            g_fusionMap['O'] = { "HH" };
        }

        TEST_METHOD(TestDay19)
        {
            auto ret = SantaFusion("HOH");
            Assert::AreEqual(4, ret);
        }

        TEST_METHOD(Day19Part1)
        {
            int result = -1;
            Assert::AreEqual(0, result);
        }

        TEST_METHOD(Day19Part2)
        {
            int result = -1;
            Assert::AreEqual(0, result);
        }
    };
}