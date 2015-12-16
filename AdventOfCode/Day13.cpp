#include "stdafx.h"
#include "CppUnitTest.h"
#include "FileHelper.h"
#include "StringHelper.h"
#include <map>

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    class SeatingChart
    {
    public:
        std::vector<std::string> m_people;
        std::map<std::pair<std::string, std::string>, int> m_map;

        int ComputeCost(std::vector<std::string> seats)
        {
            int cost = 0;
            auto count = seats.size();
            seats.push_back(seats.front()); // push the first seat to the back

            for (auto ii = 0u; ii < count; ii++)
            {
                cost += m_map[std::pair<std::string, std::string>(seats[ii], seats[ii + 1])];
                cost += m_map[std::pair<std::string, std::string>(seats[ii+1], seats[ii])];
            }

            return cost;
        }

        void AddSelf()
        {
            auto self = std::string("Self");
            for (auto&& p : m_people)
            {
                m_map[std::pair<std::string, std::string>(self, p)] = 0;
                m_map[std::pair<std::string, std::string>(p, self)] = 0;
            }
            m_people.push_back(self);
        }

        void Parse(std::string filename)
        {
            TextFile file(filename.c_str());
            for (auto&& line : file)
            {
                auto args = Split(line, " .");
                m_map[std::pair<std::string, std::string>(args[0], args[10])] = (args[2] == "lose" ? -1 : +1) * atol(args[3].c_str());
                if (m_people.end() == std::find(m_people.begin(), m_people.end(), args[0]))
                {
                    // add unique person
                    m_people.push_back(args[0]);
                }
            }

            Assert::AreEqual(m_people.size() * (m_people.size() - 1), m_map.size(), L"Incorrect number of people.");
        }

        int EvaluateBestSeats()
        {
            int result = INT_MIN;
            auto& p = m_people;
            std::sort(p.begin(), p.end());
            do {
                result = std::max(result, ComputeCost(p));
            } while (std::next_permutation(p.begin(), p.end()));
            return result;
        }
    };

}

namespace AdventOfCode
{
    TEST_CLASS(Day13)
    {
    public:
        TEST_METHOD(TestDay13)
        {
            SeatingChart chart;
            chart.Parse("../InputData/Day13Test.txt");

            Assert::AreEqual(330, chart.EvaluateBestSeats());
        }

        TEST_METHOD(Day13Part1)
        {
            SeatingChart chart;
            chart.Parse("../InputData/Day13.txt");

            Assert::AreEqual(733, chart.EvaluateBestSeats());
        }

        TEST_METHOD(Day13Part2)
        {
            SeatingChart chart;
            chart.Parse("../InputData/Day13.txt");

            chart.AddSelf();

            Assert::AreEqual(725, chart.EvaluateBestSeats());
        }
    };
}