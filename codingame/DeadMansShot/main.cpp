#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

/*
source: https://rosettacode.org/wiki/Ray-casting_algorithm#C.2B.2B
*/

const double epsilon = numeric_limits<float>().epsilon();
const numeric_limits<double> DOUBLE;
const double MIN = DOUBLE.min();
const double MAX = DOUBLE.max();

struct Point {
    double x, y;
};

struct Edge {
    Point a, b;

    Edge(Point a, Point b){
        this->a.x = a.x;
        this->a.y = a.y;
        this->b.x = b.x;
        this->b.y = b.y;
    }

    bool operator()(const Point& p) const
    {
        if (p.x == b.x && p.x > a.x) return false;
        if (a.y > b.y) return Edge{ b, a }(p);
        if (p.y == a.y || p.y == b.y) return operator()({ p.x, p.y + epsilon });
        if (p.y > b.y || p.y < a.y || p.x > max(a.x, b.x)) return false;
        if (p.x < min(a.x, b.x)) return true;
        auto blue = abs(a.x - p.x) > MIN ? (p.y - a.y) / (p.x - a.x) : MAX;
        auto red = abs(a.x - b.x) > MIN ? (b.y - a.y) / (b.x - a.x) : MAX;
        return blue >= red;
    }
};

struct Figure {
    vector<Edge> edges;

    bool contains(const Point& p) const
    {
        auto c = 0;
        for (auto e : edges) if (e(p)) {
            c++;
            cerr << e.a.x << ", " << e.a.y << "\t" << e.b.x << ", " << e.b.y << endl;
        }
        cerr << c << endl;
        return c % 2 != 0;
    }
};

int main()
{
    int N;
    cin >> N; cin.ignore();
    vector<Point> points;
    Figure shape;

    cerr << "shape" << endl;
    for (int i = 0; i < N; i++) {
        Point p;
        cin >> p.x >> p.y; cin.ignore();
        points.push_back(p);

        cerr << "(" << p.x << ", " << p.y << ")" << endl;
    }

    for (int i = 0; i < points.size(); i++){
        shape.edges.push_back(Edge(points[i], points[(i + 1) % N]));
    }

    cerr << "points" << endl;
    int M;
    cin >> M; cin.ignore();
    for (int i = 0; i < M; i++) {
        Point p;
        cin >> p.x >> p.y; cin.ignore();
        cout << (shape.contains(p) ? "hit" : "miss") << endl;
        cerr << "(" << p.x << ", " << p.y << ")" << endl;

    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;
}
