#include "stdafx.h"
#include "CppUnitTest.h"
#include "StringHelper.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    class Node
    {
    public:
        Node(const std::string& n) : m_name(n) { }
        const std::string& GetName() const {
            return m_name;
        }

    private:
        std::string m_name;
    };

    class Edge
    {
    public:
        Edge(Node* a, Node* b, int dist)
            : m_dist(dist)
        { 
            m_node[0] = a;
            m_node[1] = b;
        }

        bool HasNodes(Node* a, Node* b) const
        {
            return (a == m_node[0] && b == m_node[1]) ||
                (a == m_node[1] && b == m_node[0]);
        }

        int Distance() const {
            return m_dist;
        }

    public:
        int   m_dist;
        Node* m_node[2];
    };

    class Graph
    {
    public:
        void AddEdge(const std::string& a, const std::string& b, int dist)
        {
            auto nodeA = AddNode(a);
            auto nodeB = AddNode(b);
            m_edges.push_back(Edge(nodeA, nodeB, dist));
        }

        void AddEdge(const std::string& line)
        {
            // Parse the input line format
            auto args = Split(line, " =");
            AddEdge(args[0], args[2], atol(args[3].c_str()));
        }

        size_t GetNodeCount() const 
        {
            return m_nodes.size();
        }

        int ComputeShortestRoute()
        {
            int distance = 1 << 16;
            for (auto&& tip : m_nodes)
            {
                for (auto&& tail : m_nodes)
                {
                    if (tip == tail) {
                        continue;
                    }
                       
                    int len = ComputeShortestRoute(tip, tail);
                    distance = std::min(distance, len);
                }
            }
            return distance;
        }

        int ComputeLongestRoute()
        {
            int distance = 0;
            for (auto&& tip : m_nodes)
            {
                for (auto&& tail : m_nodes)
                {
                    if (tip == tail) {
                        continue;
                    }

                    int len = ComputeLongestRoute(tip, tail);
                    distance = std::max(distance, len);
                }
            }
            return distance;
        }

        // Compute the shortest route between provied start/finish points.
        int ComputeShortestRoute(Node* start, Node* finish)
        {
            std::list<Node*> open;

            for (auto&& n : m_nodes)
            {
                if (n != start && n != finish)
                {
                    open.push_back(n);
                }
            }

            int distance = 0;

            while (!open.empty())
            {
                int leg = 1 << 16;
                Node* next = nullptr;
                for (auto&& n : open)
                {
                    int ret = FindEdge(start, n).Distance();
                    if (ret < leg)
                    {
                        next = n;
                        leg = ret;
                    }
                }
                open.remove(next);
                distance += leg;
                start = next;
            }

            // Need to add in the final leg (note, at this point start has changed, if the open set wasn't empty!)
            distance += FindEdge(start, finish).Distance();

            return distance;
        }

        // Compute the longest route between provied start/finish points.
        int ComputeLongestRoute(Node* start, Node* finish)
        {
            std::list<Node*> open;

            for (auto&& n : m_nodes)
            {
                if (n != start && n != finish)
                {
                    open.push_back(n);
                }
            }

            int distance = 0;

            while (!open.empty())
            {
                int leg = 0;
                Node* next = nullptr;
                for (auto&& n : open)
                {
                    int ret = FindEdge(start, n).Distance();
                    if (ret > leg)
                    {
                        next = n;
                        leg = ret;
                    }
                }
                open.remove(next);
                distance += leg;
                start = next;
            }

            // Need to add in the final leg (note, at this point start has changed, if the open set wasn't empty!)
            distance += FindEdge(start, finish).Distance();

            return distance;
        }

        Node* GetNode(const std::string& n)
        {
            auto it = std::find_if(m_nodes.begin(), m_nodes.end(), [n](const Node* node) { return node->GetName() == n; });
            return (it != m_nodes.end()) ? *it : nullptr;
        }

    private:
        Edge& FindEdge(Node* a, Node* b)
        {
            auto it = std::find_if(m_edges.begin(), m_edges.end(), 
                [a, b](const Edge& edge) { return edge.HasNodes(a, b); });

            return *it;
        }

        Node* AddNode(const std::string& n)
        {
            auto it = std::find_if(m_nodes.begin(), m_nodes.end(), [n](const Node* node) { return node->GetName() == n; });
            if (it == m_nodes.end())
            {
                auto node = new Node(n);
                m_nodes.push_back(node);
                return node;
            }

            return *it;
        }

        std::list<Node*> m_nodes; // records the shortest exit (for a given node)
        std::list<Edge> m_edges;
    };
}

std::vector<std::string> InputData = {
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

            g.AddEdge("London", "Dublin", 464);
            g.AddEdge("London", "Belfast", 518);
            g.AddEdge("Dublin", "Belfast", 141);

            auto nc = g.GetNodeCount();

            Assert::AreEqual(3u, nc);

            Assert::AreEqual(605, g.ComputeShortestRoute());
            Assert::AreEqual(982, g.ComputeLongestRoute());

            g.AddEdge("Tacoma", "London", 10);
            g.AddEdge("Tacoma", "Dublin", 10);
            g.AddEdge("Tacoma", "Belfast", 10);
            Assert::AreEqual(161, g.ComputeShortestRoute());

            {
                // Test parser
                Graph p;
                p.AddEdge("London to Dublin = 464");
                p.AddEdge("London to Belfast = 518");
                p.AddEdge("Dublin to Belfast = 140");
                Assert::AreEqual(604, p.ComputeShortestRoute());
            }
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