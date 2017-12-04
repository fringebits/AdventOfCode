#include "stdafx.h"
#include "CppUnitTest.h"
#include "StringHelper.h"
#include "map"
#include "functional"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

// http://adventofcode.com/day/9

namespace
{
    typedef std::string Node;
    typedef std::tuple<std::string, std::string> Edge;

    class Graph
    {
    private:
        std::map< std::tuple<Node, Node>, int > m_graph;
        std::list<Node> m_nodes; // Unique set of all nodes.

    public:
        void AddEdge(const std::string& line)
        {
            // Parse the input line format
            auto args = Split(line, " =");
            m_graph[Edge(args[0], args[2])] = atol(args[3].c_str());
            m_graph[Edge(args[2], args[0])] = atol(args[3].c_str());
            AddNode(args[0]);
            AddNode(args[2]);
        }

        int Distance(Node a, Node b)
        {
            return m_graph[Edge(a, b)];
        }

        size_t GetNodeCount() const 
        {
            return m_nodes.size();
        }

        int ComputeShortestRoute()
        {
            return EvaluateRoutes(INT_MAX, [](int a, int b) -> bool { return a < b; });
        }

        int ComputeLongestRoute()
        {
            return EvaluateRoutes(0, [](int a, int b) -> bool { return a > b; });
        }

        int EvaluateRoutes(int v0, std::function<bool(int, int)> func)
        {
            int best = v0;
            for (auto&& tip : m_nodes)
            {
                for (auto&& tail : m_nodes)
                {
                    if (tip == tail) {
                        continue;
                    }

                    auto ret = ComputeBestRoute(tip, tail, v0, func);
                    if (func(ret, best))
                    {
                        best = ret;
                    }
                }
            }
            return best;
        }

        // Compute the shortest route between provied start/finish points.
        int ComputeBestRoute(Node start, Node finish, int v0, std::function<bool(int,int)> func)
        {
            std::list<Node> open;

            // List of all the nodes to evaluate (except start, finish)
            for (auto&& n : m_nodes)
            {
                if (n == start || n == finish)
                    continue;
                open.push_back(n);
            }

            int distance = 0;
            while (!open.empty())
            {
                int leg = v0;
                Node next;
                for (auto&& n : open)
                {
                    int ret = Distance(start, n);
                    if (func(ret, leg))
                    {
                        next = n;
                        leg = ret;
                    }
                }
                open.remove(next);
                distance += leg;
                start = next;
            }

            // Need to add in the final leg.
            distance += Distance(start, finish);

            return distance;
        }

    private:
        void AddNode(std::string n)
        {
            if (m_nodes.end() == std::find(m_nodes.begin(), m_nodes.end(), n))
            {
                m_nodes.push_back(n);
            }
        }
    };
}

const std::vector<std::string> InputData = {
    "Tristram to AlphaCentauri = 34",
    "Tristram to Snowdin = 100",
    "Tristram to Tambi = 63",
    "Tristram to Faerun = 108",
    "Tristram to Norrath = 111",
    "Tristram to Straylight = 89",
    "Tristram to Arbre = 132",
    "AlphaCentauri to Snowdin = 4",
    "AlphaCentauri to Tambi = 79",
    "AlphaCentauri to Faerun = 44",
    "AlphaCentauri to Norrath = 147",
    "AlphaCentauri to Straylight = 133",
    "AlphaCentauri to Arbre = 74",
    "Snowdin to Tambi = 105",
    "Snowdin to Faerun = 95",
    "Snowdin to Norrath = 48",
    "Snowdin to Straylight = 88",
    "Snowdin to Arbre = 7",
    "Tambi to Faerun = 68",
    "Tambi to Norrath = 134",
    "Tambi to Straylight = 107",
    "Tambi to Arbre = 40",
    "Faerun to Norrath = 11",
    "Faerun to Straylight = 66",
    "Faerun to Arbre = 144",
    "Norrath to Straylight = 115",
    "Norrath to Arbre = 135",
    "Straylight to Arbre = 127",
};

namespace AdventOfCode
{
    TEST_CLASS(Day09)
    {
    public:
        TEST_METHOD(TestDay09)
        {
            Graph g;

            g.AddEdge("London to Dublin = 464");
            g.AddEdge("London to Belfast = 518");
            g.AddEdge("Dublin to Belfast = 141");

            auto nc = g.GetNodeCount();

            Assert::AreEqual(3u, nc);

            Assert::AreEqual(605, g.ComputeShortestRoute());
            Assert::AreEqual(982, g.ComputeLongestRoute());

            g.AddEdge("Tacoma to London = 10");
            g.AddEdge("Tacoma to Dublin = 10");
            g.AddEdge("Tacoma to Belfast = 10");
            Assert::AreEqual(161, g.ComputeShortestRoute());
        }

        TEST_METHOD(Day09Part1)
        {
            Graph g;
            for (auto&& line : InputData)
            {
                g.AddEdge(line);
            }

            auto nc = g.GetNodeCount();
            Assert::AreEqual(8u, nc);

            Assert::AreEqual(251, g.ComputeShortestRoute());
        }

        TEST_METHOD(Day09Part2)
        {
            Graph g;
            for (auto&& line : InputData)
            {
                g.AddEdge(line);
            }

            auto nc = g.GetNodeCount();
            Assert::AreEqual(8u, nc);

            Assert::AreEqual(898, g.ComputeLongestRoute());
        }
    };
}