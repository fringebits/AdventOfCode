#include "stdafx.h"
#include "CppUnitTest.h"
#include <map>

#include "StringHelper.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace
{
    class Circuit;
    class Gate
    {
    public:
        Gate(std::string a, std::string out)
            : A(a), Out(out), hasValue(false) { }

        uint16_t Value(Circuit& circuit)
        {
            if (hasValue) {
                return value;
            }
            value = Evaluate(circuit);
            hasValue = true;
            return value;
        }

        virtual uint16_t Evaluate(Circuit& circuit) = 0;

    public:
        std::string A; // primary input
        std::string Out; // primary output
        bool hasValue;
        uint16_t value;
    };

    class Circuit
    {
    private:
        std::map<std::string, Gate*> m_circuit;

    public:
        void Reset()
        {
            for (auto&& wire : m_circuit)
            {
                wire.second->hasValue = false;
            }
        }

        void AssignGate(std::string wire, Gate* gate)
        {
            m_circuit[wire] = gate;
        }

        uint16_t Signal(const std::string& wire)
        {
            if (IsNumber(wire))
            {
                return atol(wire.c_str());
            }

            auto gate = m_circuit[wire]; // get the gate that produces the output
            return gate->Value(*this);
        }

        void Parse(const std::string& string);

    };

    class SetGate : public Gate
    {
    public:
        SetGate(std::string a, std::string out)
            : Gate(a, out)
        {
        }

        SetGate(std::string a, uint16_t out)
            : Gate(a, "Unknown")
        {
            hasValue = true;
            value = out;
        }

        uint16_t Evaluate(Circuit& c)
        {
            // a is the output
            Assert::IsFalse(hasValue, L"Already has value.");
            return c.Signal(this->A);
        }
    };

    class NotGate : public Gate
    {
    public:
        NotGate(std::string a, std::string out)
            : Gate(a, out)
        {
        }

        uint16_t Evaluate(Circuit& c)
        {
            // a is the output
            return ~c.Signal(A);
        }
    };

    class BinaryGate : public Gate
    {
    public:
        BinaryGate(std::string a, std::string b, std::string op, std::string out)
            : Gate(a, out), B(b), Op(op)
        {
        }

        std::string B;
        std::string Op;

        uint16_t Evaluate(Circuit& c)
        {
            uint16_t result = 0;

            if (Op == "AND")
            {
                result = c.Signal(A) & c.Signal(B);
            }
            else if (Op == "OR")
            {
                result = c.Signal(A) | c.Signal(B);
            }
            else if (Op == "LSHIFT")
            {
                result = c.Signal(A) << c.Signal(B);
            }
            else if (Op == "RSHIFT")
            {
                result = c.Signal(A) >> c.Signal(B);
            }
            else
            {
                Assert::Fail(L"Unkown gate.");
            }
            return result;
        }
    };

    void Circuit::Parse(const std::string& string)
    {
        auto args = Split(string, " ->");
        auto wire = args.back();

        if (args.size() == 2)
        {
            m_circuit[wire] = new SetGate(args[0], wire);
        }
        else if (args[0] == "NOT")
        {
            m_circuit[wire] = new NotGate(args[1], wire);
        }
        else
        {
            // putting a value on a wire:
            // x GATE y -> w
            Assert::AreEqual<size_t>(4u, args.size(), L"GATE requires 4 arguments.");
            m_circuit[wire] = new BinaryGate(args[0], args[2], args[1], wire);
        }
    }



}

#include "Day07.h"

namespace AdventOfCode
{
    TEST_CLASS(Day07)
    {
    public:
        TEST_METHOD(TestDay07)
        {
            std::vector<std::string> SampleInput = {
                "x AND y->d",
                "x OR y->e",
                "x LSHIFT 2->f",
                "y RSHIFT 2->g",
                "NOT x->h",
                "NOT y->i",
                "123->x",
                "456->y"
            };

            Circuit circut;
            for (auto&& line : SampleInput) 
            {
                circut.Parse(line);
            }

            Assert::AreEqual<uint16_t>(72, circut.Signal("d"));
            Assert::AreEqual<uint16_t>(507, circut.Signal("e"));
            Assert::AreEqual<uint16_t>(492, circut.Signal("f"));
            Assert::AreEqual<uint16_t>(114, circut.Signal("g"));
            Assert::AreEqual<uint16_t>(65412, circut.Signal("h"));
            Assert::AreEqual<uint16_t>(65079, circut.Signal("i"));
            Assert::AreEqual<uint16_t>(123, circut.Signal("x"));
            Assert::AreEqual<uint16_t>(456, circut.Signal("y"));
        }

        TEST_METHOD(TestDay07a)
        {
            Circuit circuit;
            //Assert::AreEqual<uint16_t>(0, circuit.Parse("1 AND 2 -> a"));
            //Assert::AreEqual<uint16_t>(1, circuit.Parse("1 AND 3 -> a"));
            //Assert::AreEqual<uint16_t>(65535, circuit.Parse("NOT 0 -> b"));
            //Assert::AreEqual<uint16_t>(65535, circuit.Parse("NOT a -> c"));
        }

        TEST_METHOD(Day07Part1)
        {
            Circuit circut;
            for (auto&& line : InputData)
            {
                circut.Parse(line);
            }

            auto result = circut.Signal("a");

            Assert::AreEqual<uint16_t>(3176, result);
        }

        TEST_METHOD(Day07Part2)
        {
            Circuit circut;
            for (auto&& line : InputData)
            {
                circut.Parse(line);
            }

            auto result = circut.Signal("a");

            circut.Reset();
            circut.AssignGate("b", new SetGate("b", result));
            Assert::AreEqual<uint16_t>(result, circut.Signal("b"));

            result = circut.Signal("a");

            Assert::AreEqual<uint16_t>(14710, result);
        }
    };
}