#pragma once

class Point
{
public:
    int X;
    int Y;
    Point(int x, int y) : X(x), Y(y) { }
    bool operator==(const Point& p) const
    {
        return X == p.X && Y == p.Y;
    }
};

