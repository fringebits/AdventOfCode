#include "stdafx.h"
#include "CppUnitTest.h"
#include "Point.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    class Grid
    {
        bool light[1000][1000];

    public:
        Grid()
        {
            Reset();
        }

        void Reset()
        {
            memset(light, 0, sizeof(light));
        }

        void Execute(const std::string& input)
        {
            //turn off 660, 55 through 986, 197
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
                TurnOff(a, b);
            }
            else if (cmd == "turn on")
            {
                TurnOn(a, b);
            }
            else if (cmd == "toggle")
            {
                Toggle(a, b);
            }
            else
            {
                Assert::IsTrue(false, L"Unrecognized command.");
            }
        }

        void TurnOn(Point a, Point b)
        {
            for (int ii = a.X; ii <= b.X; ii++)
            {
                for (int jj = a.Y; jj <= b.Y; jj++)
                {
                    light[ii][jj] = true;
                }
            }
        }

        void Toggle(Point a, Point b)
        {
            for (int ii = a.X; ii <= b.X; ii++)
            {
                for (int jj = a.Y; jj <= b.Y; jj++)
                {
                    light[ii][jj] = !light[ii][jj];
                }
            }
        }

        void TurnOff(Point a, Point b)
        {
            for (int ii = a.X; ii <= b.X; ii++)
            {
                for (int jj = a.Y; jj <= b.Y; jj++)
                {
                    light[ii][jj] = false;
                }
            }
        }

        int Count()
        {
            int count = 0;
            for (int ii = 0; ii < 1000; ii++)
            {
                for (int jj = 0; jj < 1000; jj++)
                {
                    if (light[ii][jj])
                    {
                        count++;
                    }
                }
            }
            return count;
        }
    };

    class BrightGrid
    {
        int* lights;

    public:
        BrightGrid()
        {
            lights = new int[1000 * 1000];
            Reset();
        }

        void Reset()
        {
            memset(lights, 0, sizeof(int)*1000*1000);
        }

        int Offset(int x, int y)
        {
            return x + y * 1000;
        }

        void Execute(const std::string& input)
        {
            //turn off 660, 55 through 986, 197
            Point a(0, 0);
            Point b(0, 0);

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
                TurnOff(a, b);
            }
            else if (cmd == "turn on")
            {
                TurnOn(a, b);
            }
            else if (cmd == "toggle")
            {
                Toggle(a, b);
            }
            else
            {
                Assert::IsTrue(false, L"Unrecognized command.");
            }
        }

        void TurnOn(Point a, Point b)
        {
            for (int ii = a.X; ii <= b.X; ii++)
            {
                for (int jj = a.Y; jj <= b.Y; jj++)
                {
                    lights[Offset(ii, jj)] += 1;
                }
            }
        }

        void Toggle(Point a, Point b)
        {
            for (int ii = a.X; ii <= b.X; ii++)
            {
                for (int jj = a.Y; jj <= b.Y; jj++)
                {
                    lights[Offset(ii, jj)] += 2;
                }
            }
        }

        void TurnOff(Point a, Point b)
        {
            for (int ii = a.X; ii <= b.X; ii++)
            {
                for (int jj = a.Y; jj <= b.Y; jj++)
                {
                    auto ofs = Offset(ii, jj);
                    lights[ofs] = std::max(0, lights[ofs] - 1);
                }
            }
        }

        int Count()
        {
            int count = 0;
            for (int ii = 0; ii < 1000 * 1000; ii++)
            {
                count += lights[ii];
            }
            return count;
        }
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
            Grid grid;

            Assert::AreEqual(0, grid.Count());
            grid.TurnOn(Point(0, 0), Point(999, 999));
            Assert::AreEqual(1000 * 1000, grid.Count());

            grid.Toggle(Point(0, 0), Point(499, 499));
            Assert::AreEqual(500 * 500 * 3, grid.Count());

            grid.Reset();
            grid.Execute("turn on 0,0 through 499,499");
            Assert::AreEqual(500 * 500, grid.Count());

            BrightGrid bright;
            Assert::AreEqual(0, bright.Count());

            bright.TurnOn(Point(0, 0), Point(999, 999));
            Assert::AreEqual(1000 * 1000, bright.Count());

            bright.Toggle(Point(0, 0), Point(999, 999));
            Assert::AreEqual(3 * 1000 * 1000, bright.Count());

            bright.TurnOff(Point(0, 0), Point(999, 999));
            Assert::AreEqual(2 * 1000 * 1000, bright.Count());
        }

        TEST_METHOD(Day06Part1)
        {
            int count = sizeof(InputData) / sizeof(std::string);
            Assert::AreEqual(300, count);

            Grid grid;
            for (int ii = 0; ii < count; ii++)
            {
                grid.Execute(InputData[ii]);
            }

            Assert::AreEqual(400410, grid.Count());
        }

        TEST_METHOD(Day06Part2)
        {
            int count = sizeof(InputData) / sizeof(std::string);
            Assert::AreEqual(300, count);

            BrightGrid grid;
            for (int ii = 0; ii < count; ii++)
            {
                grid.Execute(InputData[ii]);
            }

            Assert::AreEqual(15343601, grid.Count());
        }
    };
}