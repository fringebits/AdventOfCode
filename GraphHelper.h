#pragma once

#include <string>
#include <list>
#include <map>

class Edge
{
public:
    Edge(const std::string& s, const std::string& target, int dist)
        : m_dist(dist)
        , m_source(s)
        , m_target(t)
    {
    }
    
public:
    int m_dist;
    std::string m_source;
    std::string m_target;
};

class Graph
{
public:
    void AddEdge(const std::string& source, const std::string& target, int distance)
    {
        m_edges.push_back(new Edge(source, target, distance));
    }

    std::list <std::string> Edges(const std::string& source)
    {
        std::list<Edge*> list;
        for (auto&& edge : m_edges)
        {
            if (edge->m_source == source)
            {
                list.push_back(edge);
            }
        }
    }



    

private:
    std::list<Edge*> m_edges;
};
    