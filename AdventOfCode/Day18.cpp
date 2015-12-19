#include "stdafx.h"
#include "CppUnitTest.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    template <typename T>
    class Grid
    {
    protected:
        int m_dim;
        std::vector<T> m_lights;

    public:
        Grid(int dim)
            : m_dim(dim)
        {
            m_lights.resize(m_dim * m_dim);
        }

        void ParseLine(int row, std::string line)
        {
            Assert::AreEqual<size_t>(line.size(), m_dim);
            int col = 0;
            for (auto&& ch : line)
            {
                Set(col++, row, (ch == '#') ? 1 : 0);
            }
        }

        void Parse(std::string filename)
        {
            TextFile file(filename.c_str());
            Assert::AreEqual<size_t>(file.size(), m_dim);
            int ii = 0;
            for (auto&& line : file)
            {
                ParseLine(ii++, line);
            }
        }

        int Count()
        {
            return Animate(0, nullptr);
        }

        int Animate(int nsteps, std::function<void()> f)
        {
            for (int ii = 0; ii < nsteps; ii++)
            {
                f();
            }

            int count = 0;
            for (auto&& cell : m_lights)
            {
                count += cell;
            }
            return count;
        }

        int CountNeighbors(int x, int y)
        {
            int ret =
                Get(x - 1, y - 1)
                + Get(x - 1, y)
                + Get(x - 1, y + 1)
                + Get(x, y - 1)
                + Get(x, y + 1)
                + Get(x + 1, y - 1)
                + Get(x + 1, y)
                + Get(x + 1, y + 1);
            return ret;
        }

    protected:
        void Set(int x, int y, T value)
        {
            if ((x < 0) || (x >= m_dim))
            {
                return;
            }
            if ((y < 0) || (y >= m_dim))
            {
                return;
            }
            m_lights[x + y * m_dim] = value;
        }

        T Get(int x, int y)
        {
            if ((x < 0) || (x >= m_dim))
            {
                return 0;
            }
            if ((y < 0) || (y >= m_dim))
            {
                return 0;
            }
            return m_lights[x + y * m_dim];
        }
    };

    class GridPart1 : public Grid<int>
    {
    public:
        GridPart1(int d) : Grid<int>(d) { }
        int Animate(int nsteps)
        {
            return Grid<int>::Animate(nsteps, [=]() {
                std::vector<int> next(m_dim * m_dim);

                for (auto xx = 0; xx < m_dim; xx++)
                {
                    for (auto yy = 0; yy < m_dim; yy++)
                    {
                        int n = this->CountNeighbors(xx, yy);
                        if (this->Get(xx, yy))
                        {
                            // light stays on iff 2|3 nighbors
                            next[xx + yy * m_dim] = ((n == 2) || (n == 3)) ? 1 : 0;
                        }
                        else
                        {
                            next[xx + yy * m_dim] = (n == 3) ? 1 : 0;
                        }
                    }
                }

                std::swap(m_lights, next);
            });
        }

    };

    class GridPart2 : public Grid<int>
    {
    public:
        GridPart2(int d) : Grid<int>(d) { }

        bool IsCorner(int xx, int yy)
        {
            return ((xx == 0) && (yy == 0)) || ((xx == m_dim - 1) && (yy == 0)) || ((xx == m_dim - 1) && (yy == m_dim - 1)) || ((xx == 0) && (yy == m_dim - 1));
        }

        std::string Format(int row)
        {
            std::string line(m_dim, '.');
            for (int ii = 0; ii < m_dim; ii++)
            {
                if (Get(ii, row))
                {
                    line[ii] = '#';
                }
            }
            return line;
        }

        int Animate(int nsteps)
        {
            return Grid<int>::Animate(nsteps, [=]() {
                std::vector<int> next(m_dim * m_dim);

                for (auto xx = 0; xx < m_dim; xx++)
                {
                    for (auto yy = 0; yy < m_dim; yy++)
                    {
                        auto v = this->Get(xx, yy);

                        if (IsCorner(xx, yy))
                        {
                            // corner lights are stuck on.
                            next[xx + yy * m_dim] = 1;
                        }
                        else
                        {
                            int n = this->CountNeighbors(xx, yy);
                            auto nv = v;

                            if (v)
                            {
                                nv = ((n < 2) || (n > 3)) ? 0 : 1;
                            }
                            else
                            {
                                nv = (n == 3) ? 1 : 0;
                            }

                            next[xx + yy * m_dim] = nv;
                        }
                    }
                }

                std::swap(m_lights, next);
            });
        }

    };




}

namespace AdventOfCode
{
    TEST_CLASS(Day18)
    {
    public:
        TEST_METHOD(TestDay18)
        {
            GridPart1 g(6);

            g.ParseLine(0, ".#.#.#");
            g.ParseLine(1, "...##.");
            g.ParseLine(2, "#....#");
            g.ParseLine(3, "..#...");
            g.ParseLine(4, "#.#..#");
            g.ParseLine(5, "####..");

            Assert::AreEqual(15, g.Count());

            Assert::AreEqual(4, g.Animate(4));

            GridPart2 h(6);

            h.ParseLine(0, "##.#.#");
            h.ParseLine(1, "...##.");
            h.ParseLine(2, "#....#");
            h.ParseLine(3, "..#...");
            h.ParseLine(4, "#.#..#");
            h.ParseLine(5, "####.#");

            Assert::AreEqual(17, h.Count());
            Assert::AreEqual(17, h.Animate(5));
        }

        TEST_METHOD(Day18Part1)
        {
            GridPart1 g(100);
            g.Parse("../InputData/Day18.txt");
            auto result = g.Animate(100);
            Assert::AreEqual(1061, result);
        }

        TEST_METHOD(Day18Part2)
        {
            GridPart2 g(100);
            g.Parse("../InputData/Day18.txt");
            auto result = g.Animate(100);
            Assert::AreEqual(1006, result);
        }
    };
}