#include "stdafx.h"
#include "CppUnitTest.h"
#include "FileHelper.h"
#include "StringHelper.h"
#include <numeric>

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    class Ingredient
    {
    public:
        int m_capacity;
        int m_durability;
        int m_flavor;
        int m_texture;
        int m_calories;
        std::string m_name;

    public:
        Ingredient()
            : m_capacity(0)
            , m_durability(0)
            , m_flavor(0)
            , m_texture(0)
            , m_calories(0)
        {
        }

        void Parse(std::string line)
        {
            auto args = Split(line, " :,");
            m_name = args[0];
            m_capacity = atol(args[2].c_str());
            m_durability = atol(args[4].c_str());
            m_flavor = atol(args[6].c_str());
            m_texture = atol(args[8].c_str());
            m_calories = atol(args[10].c_str());
        }
    };

    class Cupboard
    {
    public:
        std::vector<Ingredient> m_parts;
    public:
        void AddIngredient(std::string line)
        {
            Ingredient p;
            p.Parse(line);
            m_parts.push_back(p);
        }

        void Parse(std::string filename)
        {
            TextFile file(filename.c_str());
            for (auto&& line : file)
            {
                AddIngredient(line);
            }
        }

        int ScoreCookie(std::vector<int> recipe, int calorieTarget = 0)
        {
            Assert::AreEqual(m_parts.size(), recipe.size());

            Ingredient t;
            for (auto ii = 0u; ii < recipe.size(); ii++)
            {
                t.m_capacity += recipe[ii] * m_parts[ii].m_capacity;
                t.m_durability += recipe[ii] * m_parts[ii].m_durability;
                t.m_flavor += recipe[ii] * m_parts[ii].m_flavor;
                t.m_texture += recipe[ii] * m_parts[ii].m_texture;
                t.m_calories += recipe[ii] * m_parts[ii].m_calories;
            }

            if ((calorieTarget != 0) && (calorieTarget != t.m_calories))
            {
                return 0;
            }

            t.m_capacity = std::max(0, t.m_capacity);
            t.m_durability = std::max(0, t.m_durability);
            t.m_flavor = std::max(0, t.m_flavor);
            t.m_texture = std::max(0, t.m_texture);

            return t.m_capacity * t.m_durability * t.m_flavor * t.m_texture;
        }

        int BestRecipe(std::vector<int> partial, int calorieTarget)
        {
            int score = 0;
            auto len = partial.size();
            auto p = std::accumulate(partial.begin(), partial.end(), 0);

            if (len == m_parts.size() - 2)
            {
                // have only one last item to iterate on.
                partial.resize(m_parts.size());
                for (int ii = 0; ii <= (100 - p); ii++)
                {
                    partial[len] = ii;
                    partial[len+1] = 100 - ii - p;
                    auto ret = ScoreCookie(partial, calorieTarget);
                    score = std::max(score, ret);
                }
            }
            else
            {
                partial.push_back(0);
                for (int ii = 0; ii < (100 - p); ii++)
                {
                    partial[len] = ii;
                    auto ret = BestRecipe(partial, calorieTarget);
                    score = std::max(score, ret);
                }
            }

            return score;
        }

        int BestRecipe(int calorieTarget = 0)
        {
            int score = BestRecipe({}, calorieTarget);
            return score;
        }

    };

}

namespace AdventOfCode
{
    TEST_CLASS(Day15)
    {
    public:
        TEST_METHOD(TestDay15)
        {
            Cupboard c;
            c.AddIngredient("Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8");
            c.AddIngredient("Cinnamon : capacity 2, durability 3, flavor -2, texture -1, calories 3");
            Assert::AreEqual(62842880, c.BestRecipe());

            Assert::AreEqual(57600000, c.BestRecipe(500));
        }

        TEST_METHOD(Day15Part1)
        {
            Cupboard c;
            c.Parse("../InputData/Day15.txt");
            
            int result = c.BestRecipe();
            Assert::AreEqual(21367368, result);
        }

        TEST_METHOD(Day15Part2)
        {
            Cupboard c;
            c.Parse("../InputData/Day15.txt");

            int result = c.BestRecipe(500);
            Assert::AreEqual(1766400, result);
        }
    };
}