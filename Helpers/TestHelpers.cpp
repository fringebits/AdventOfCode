#include "stdafx.h"
#include "CppUnitTest.h"
#include "Md5Helper.h"
#include "StateMachine.h"

enum TestState {
    A, B, C, D, E
};

enum TestTrigger {
    X, Y, Z
};

void ConfigureStateMachine(StateMachine<TestState, TestTrigger>& sm)
{
    sm.ConfigureState(A,
        [](const Transition<TestState, TestTrigger>& t) { },
        [](const Transition<TestState, TestTrigger>& t) { });
    sm.AddStateTrigger(A, B, X);
    sm.AddStateTrigger(A, C, Y);
    sm.AddStateTrigger(A, D, Z);

    sm.ConfigureState(B,
        [&sm](const Transition<TestState, TestTrigger>& t) { },
        [&sm](const Transition<TestState, TestTrigger>& t) { 
        if (t.GetTrigger() == X)
        {
            // If we are exiting "B" with trigger X, we also want to fire trigger Y.
            sm.FireTrigger(Y);
        }
    });
    sm.AddStateTrigger(B, C, X);
    sm.AddStateTrigger(B, D, Y);
    sm.AddStateTrigger(B, A, Z);

    sm.ConfigureState(C,
        [](const Transition<TestState, TestTrigger>& t) { },
        [](const Transition<TestState, TestTrigger>& t) { });
    sm.AddStateTrigger(C, B, X);
    sm.AddStateTrigger(C, D, Y);

    sm.ConfigureState(D,
        [&sm](const Transition<TestState, TestTrigger>& t) { sm.FireTrigger(X);  },
        [](const Transition<TestState, TestTrigger>& t) {});
    sm.AddStateTrigger(D, A, X);
    sm.AddStateTrigger(D, B, Y);
}

namespace Microsoft
{
    namespace VisualStudio
    {
        namespace CppUnitTestFramework
        {
            template<> std::wstring ToString<TestState>(const TestState& q)
            {
                std::wstringstream stream;
                stream << q;
                return stream.str();
            }
        }
    }
}



using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace AdventOfCode
{
    TEST_CLASS(TestHelpers)
    {
    public:
        TEST_METHOD(TestMd5)
        {
            MD5 hash;

            hash.Compute("");
            Assert::AreEqual(hash.writeToString(), std::string("d41d8cd98f00b204e9800998ecf8427e"));

            hash.Compute("The quick brown fox jumps over the lazy dog");
            Assert::AreEqual(hash.writeToString(), std::string("9e107d9d372bb6826bd81d3542a419d6"));

            hash.Compute("The quick brown fox jumps over the lazy dog.");
            Assert::AreEqual(hash.writeToString(), std::string("e4d909c290d0fb1ca068ffaddf22cbd0"));
        }

        TEST_METHOD(TestStateMachineA)
        {
            StateMachine<TestState, TestTrigger> sm(A);
            ConfigureStateMachine(sm);

            Assert::AreEqual(A, sm.CurrentState());

            sm.FireTrigger(X);
            Assert::AreEqual(B, sm.CurrentState());

            sm.FireTrigger(X);
            Assert::AreEqual(A, sm.CurrentState());
        }

    };
}