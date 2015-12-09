#include "stdafx.h"
#include "CppUnitTest.h"
#include "Point.h"
#include "functional"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

// http://adventofcode.com/day/6

namespace
{
    template <typename T, int D>
    class Grid
    {
        T* m_lights;

        std::function<T(T)> m_turnOn;
        std::function<T(T)> m_turnOff;
        std::function<T(T)> m_toggle;
        std::function<int(T)> m_count;

    public:
        Grid(std::function<T(T)> turnOn, std::function<T(T)> turnOff, std::function<T(T)> toggle, std::function<int(T)> count) :
            m_turnOn(turnOn),
            m_turnOff(turnOff),
            m_toggle(toggle), 
            m_count(count)
        {
            m_lights = new T[D * D];
            Reset();
        }

        ~Grid()
        {
            delete[] m_lights;
        }

        void Reset()
        {
            memset(m_lights, 0, sizeof(T) * D * D);
        }

        void Execute(const std::string& input)
        {
            Point a(0,0);
            Point b(0,0);

            auto pos = input.find_first_of("0123456789");
            auto cmd = input.substr(0, pos - 1);

            char* mark = nullptr;

            a.X = strtol(&input[pos], &mark, 10);
            a.Y = strtol(mark + 1, nullptr, 10);

            pos = input.find_first_of("0123456789", input.find("through"));
            b.X = strtol(&input[pos], &mark, 10);
            b.Y = strtol(mark + 1, nullptr, 10);

            if (cmd == "turn off")
            {
                Execute(a, b, m_turnOff);
            }
            else if (cmd == "turn on")
            {
                Execute(a, b, m_turnOn);
            }
            else if (cmd == "toggle")
            {
                Execute(a, b, m_toggle);
            }
            else
            {
                Assert::IsTrue(false, L"Unrecognized command.");
            }
        }

        int Count() const
        {
            int result = 0;
            for (int ii = 0; ii < D; ii++)
            {
                for (int jj = 0; jj < D; jj++)
                {
                    result += m_count(m_lights[ii + jj * D]);
                }
            }
            return result;
        }

    private:
        void Execute(Point a, Point b, std::function<T(T)> func)
        {
            for (int ii = a.X; ii <= b.X; ii++)
            {
                for (int jj = a.Y; jj <= b.Y; jj++)
                {
                    m_lights[ii + jj * D] = func(m_lights[ii + jj * D]);
                }
            }
        }
    };

    class BinaryGrid : public Grid<bool, 1000>
    {
    public:
        BinaryGrid() :
            Grid([](bool state) -> bool { return true; },
                [](bool state) -> bool { return false; },
                [](bool state) -> bool { return !state; },
                [](bool state) -> int { return state ? 1 : 0; })
        {}
    };

    class BrightGrid : public Grid<int, 1000>
    {
    public:
        BrightGrid() :
            Grid([](int state) -> int { return state + 1; },
                [](int state) -> int { return std::max(0, state - 1); },
                [](int state) -> int { return state + 2; },
                [](int state) -> int { return state; })
        {}
    };

}

#include "Day06.h"

namespace AdventOfCode
{
    TEST_CLASS(Day06)
    {
    public:
        TEST_METHOD(TestDay06)
        {
            BinaryGrid grid;

            grid.Execute("turn on 0,0 through 499,499");
            Assert::AreEqual(500 * 500, grid.Count());

            BrightGrid bright;
            Assert::AreEqual(0, bright.Count());

            bright.Execute("turn on 0,0 through 999,999");
            Assert::AreEqual(1000 * 1000, bright.Count());

            bright.Execute("toggle 0,0 through 999,999");
            Assert::AreEqual(3 * 1000 * 1000, bright.Count());

            bright.Execute("turn off 0,0 through 999,999");
            Assert::AreEqual(2 * 1000 * 1000, bright.Count());
        }

        TEST_METHOD(Day06Part1)
        {
            Assert::AreEqual(300u, InputData.size());

            BinaryGrid grid;
            for(auto&& line: InputData)
            {
                grid.Execute(line);
            }

            Assert::AreEqual(400410, grid.Count());
        }

        TEST_METHOD(Day06Part2)
        {
            Assert::AreEqual(300u, InputData.size());

            BrightGrid grid;
            for (auto&& line : InputData)
            {
                grid.Execute(line);
            }

            Assert::AreEqual(15343601, grid.Count());
        }
    };
}