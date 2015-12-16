#include "stdafx.h"
#include "CppUnitTest.h"
#include "FileHelper.h"
#include "StringHelper.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    class Reindeer {
    public:
        Reindeer(int s, int m, int r)
            : m_speed(s)
            , m_move(m)
            , m_rest(r)
        {
        }

        int m_speed;
        int m_move;  // move time
        int m_rest;  // rest time

        int DistanceAtTime(int t)
        {
            auto cycles = (t / (m_move + m_rest)) * (m_move * m_speed);
            auto partial = std::min(m_move, t % (m_move + m_rest)) * m_speed;
            return cycles + partial;
        }
    };

    typedef std::shared_ptr<Reindeer> ReindeerPtr;

    class Fleet {
    public:
        std::map<std::string, ReindeerPtr> m_map;
        std::map<std::string, int> m_score;

    public:
        void Parse(std::string filename)
        {
            TextFile file(filename.c_str());
            for (auto&& line : file)
            {
                auto arg = Split(line, " ");
                m_map[arg[0]] = std::make_shared<Reindeer>(atol(arg[3].c_str()), atol(arg[6].c_str()), atol(arg[13].c_str()));
            }
        }

        int MaxDistanceAtTime(int time)
        {
            int result = 0;
            for (auto&& p : m_map)
            {
                result = std::max(result, p.second->DistanceAtTime(time));
            }
            return result;
        }

        std::vector<std::string> LeadersAtTime(int time)
        {
            int result = 0;
            std::vector<std::string> leader;
            for (auto&& p : m_map)
            {
                auto r = p.second->DistanceAtTime(time);
                if (r > result)
                {
                    result = r;
                    leader.clear();
                    leader.push_back(p.first);
                }
                else if (r == result)
                {
                    leader.push_back(p.first);
                }
            }

            return leader;
        }

        int TopScoreAtTime(int time)
        {
            m_score.clear();
            for (int ii = 1; ii < time; ii++)
            {
                auto leaders = LeadersAtTime(ii);
                for(auto&& r: leaders)
                {
                    m_score[r] += 1;
                }
            }

            int result = 0;
            for (auto&& p : m_score)
            {
                result = std::max(result, p.second);
            }

            return result;
        }


    };
}

namespace AdventOfCode
{
    TEST_CLASS(Day14)
    {
    public:
        TEST_METHOD(TestDay14)
        {
            Fleet f;
            f.m_map["comet"] = std::make_shared<Reindeer>(14, 10, 127);
            f.m_map["dancer"] = std::make_shared<Reindeer>(16, 11, 162);

            Assert::AreEqual(140, f.m_map["comet"]->DistanceAtTime(10));
            Assert::AreEqual(160, f.m_map["dancer"]->DistanceAtTime(10));

            Assert::AreEqual(1120, f.m_map["comet"]->DistanceAtTime(1000));
            Assert::AreEqual(1056, f.m_map["dancer"]->DistanceAtTime(1000));

            auto r = f.TopScoreAtTime(1000);
            Assert::AreEqual(689, r);
        }

        TEST_METHOD(Day14Part1)
        {
            Fleet f;
            f.Parse("../InputData/Day14.txt");

            Assert::AreEqual(2655, f.MaxDistanceAtTime(2503));
        }

        TEST_METHOD(Day14Part2)
        {
            Fleet f;
            f.Parse("../InputData/Day14.txt");

            Assert::AreEqual(1059, f.TopScoreAtTime(2503));
        }
    };
}