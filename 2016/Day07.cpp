#include "stdafx.h"
#include "CppUnitTest.h"
#include <map>
#include "StringHelper.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

// http://adventofcode.com/day/7

namespace
{
    class Circuit;

    class Gate
    {
    public:
        Gate(std::string a, std::string out)
            : m_inputA(a), m_out(out), m_hasValue(false) { }

        void Reset()
        {
            m_hasValue = false;
        }

        uint16_t Value(Circuit& circuit)
        {
            if (!m_hasValue) 
            {
                SetValue(Evaluate(circuit));
            }
            return m_value;
        }
        
        virtual uint16_t Evaluate(Circuit& circuit) = 0;

    protected:
        void SetValue(uint16_t value)
        {
            m_value = value;
            m_hasValue = true;
        }

    protected:
        std::string m_inputA;   // primary input
        std::string m_out;      // primary output
        bool        m_hasValue; // has a cached value
        uint16_t    m_value;    // value
    };

    typedef std::shared_ptr<Gate> GatePtr;

    class Circuit
    {
    private:
        std::map<std::string, GatePtr> m_circuit;

    public:
        void Reset()
        {
            for (auto&& wire : m_circuit)
            {
                wire.second->Reset();
            }
        }

        void AssignGate(std::string wire, GatePtr gate)
        {
            // replace a gate.
            m_circuit[wire] = gate;
        }

        uint16_t Signal(const std::string& wire)
        {
            if (IsNumber(wire))
            {
                return static_cast<uint16_t>(atol(wire.c_str()));
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
            SetValue(out);
        }

        uint16_t Evaluate(Circuit& c)
        {
            // a is the output
            Assert::IsFalse(m_hasValue, L"Already has value.");
            return c.Signal(this->m_inputA);
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
            return ~c.Signal(m_inputA);
        }
    };

    class BinaryGate : public Gate
    {
    public:
        BinaryGate(std::string a, std::string b, std::string op, std::string out)
            : Gate(a, out), m_inputB(b), m_op(op)
        {
        }

        uint16_t Evaluate(Circuit& c)
        {
            uint16_t result = 0;

            if (m_op == "AND")
            {
                result = c.Signal(m_inputA) & c.Signal(m_inputB);
            }
            else if (m_op == "OR")
            {
                result = c.Signal(m_inputA) | c.Signal(m_inputB);
            }
            else if (m_op == "LSHIFT")
            {
                result = c.Signal(m_inputA) << c.Signal(m_inputB);
            }
            else if (m_op == "RSHIFT")
            {
                result = c.Signal(m_inputA) >> c.Signal(m_inputB);
            }
            else
            {
                Assert::Fail(L"Unkown gate.");
            }
            return result;
        }

    private:
        std::string m_inputB;
        std::string m_op;
    };

    void Circuit::Parse(const std::string& string)
    {
        auto args = Split(string, " ->");
        auto wire = args.back();

        if (args.size() == 2)
        {
            m_circuit[wire] = std::make_shared<SetGate>(args[0], wire);
        }
        else if (args[0] == "NOT")
        {
            m_circuit[wire] = std::make_shared<NotGate>(args[1], wire);
        }
        else
        {
            // putting a value on a wire:
            // x GATE y -> w
            Assert::AreEqual<size_t>(4u, args.size(), L"GATE requires 4 arguments.");
            m_circuit[wire] = std::make_shared<BinaryGate>(args[0], args[2], args[1], wire);
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
            circut.AssignGate("b", std::make_shared<SetGate>("b", result));
            Assert::AreEqual<uint16_t>(result, circut.Signal("b"));

            result = circut.Signal("a");

            Assert::AreEqual<uint16_t>(14710, result);
        }
    };
}