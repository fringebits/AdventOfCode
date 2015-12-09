#pragma once

#include <string>
#include <vector>
#include <fstream>

// Helper to read text file into a vector of lines.
class TextFile
{
public:
    TextFile(const char* filename)
    {
        std::ifstream ofs;
        ofs.open(filename, std::ios_base::in);

        for (std::string line; std::getline(ofs, line);)
        {
            m_lines.push_back(line);
        }

        ofs.close();
    }

    size_t LineCount() const
    {
        return m_lines.size();
    }

protected:
    std::vector<std::string> m_lines;
};

