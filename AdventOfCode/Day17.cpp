#include "stdafx.h"
#include "CppUnitTest.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    class Combination
    {
    public:
        std::vector<int> m_combination;
        std::vector<int> m_containers;

    public:

        int FillBuckets(std::vector<int> bucket, int volume)
        {
            m_combination.clear();
            m_containers.clear();
            m_containers.resize(bucket.size() + 1);

            int count = 0;

            for (auto ii = 1u; ii < bucket.size(); ii++)
            {
                Fill(bucket, 0, ii, [=,&count]() {
                    auto sum = std::accumulate(m_combination.begin(), m_combination.end(), 0);
                    if (sum == volume)
                    {
                        count++;
                        m_containers[m_combination.size()]++;
                    }
                    return true;
                });
            }
            return count;
        }

        int FindMinContainers(std::vector<int> bucket, int volume)
        {
            FillBuckets(bucket, volume);
            for (auto ii = 1u; ii < m_containers.size(); ii++)
            {
                if (m_containers[ii] != 0)
                {
                    return m_containers[ii];
                }
            }
            return -1;
        }

    private:
        void Fill(std::vector<int>& bucket, size_t offset, int k, std::function<void()> func)
        {
            if (k == 0)
            {
                // We've got a combination with k items
                func();
                return;
            }

            for (auto ii = offset; ii <= bucket.size() - k; ++ii)
            {
                m_combination.push_back(bucket[ii]);
                Fill(bucket, ii + 1, k - 1, func);
                m_combination.pop_back();
            }
        }
    };
}

namespace AdventOfCode
{
    TEST_CLASS(Day17)
    {
    public:
        TEST_METHOD(TestDay17)
        {
            Combination c;
            auto ret = c.FillBuckets({ 20, 15, 10, 5, 5 }, 25);
            Assert::AreEqual(4, ret);

            auto count = c.FindMinContainers({ 20, 15, 10, 5, 5 }, 25);
            Assert::AreEqual(3, count);
        }

        TEST_METHOD(Day17Part1)
        {
            Combination c;
            auto result = c.FillBuckets({ 11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3}, 150);
            Assert::AreEqual(4372, result);
        }

        TEST_METHOD(Day17Part2)
        {
            Combination c;
            auto result = c.FindMinContainers({ 11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3 }, 150);
            Assert::AreEqual(4, result);
        }
    };
}