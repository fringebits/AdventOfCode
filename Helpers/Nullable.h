#pragma once

#include <cstddef>

template <typename T>
class Nullable final
{
    template <typename T2>
    friend bool operator==(const Nullable<T2> &op1, const Nullable<T2> &op2);

    template <typename T2>
    friend bool operator==(const Nullable<T2> &op, const T2 &value);

    template <typename T2>
    friend bool operator==(const T2 &value, const Nullable<T2> &op);

    template <typename T2>
    friend bool operator==(const Nullable<T2> &op, nullptr_t nullpointer);

    template <typename T2>
    friend bool operator==(nullptr_t nullpointer, const Nullable<T2> &op);

public:
    Nullable();
    Nullable(const T &value);
    Nullable(nullptr_t nullpointer);
    const Nullable<T> & operator=(const Nullable<T> &value);
    const Nullable<T> & operator=(const T &value);
    const Nullable<T> & operator=(nullptr_t nullpointer);

    const bool HasValue() const {
        return m_hasValue;
    }

private:
    bool m_hasValue;
    T m_value;

public:
    const T & Value;
};

template <typename T>
Nullable<T>::Nullable()
    : m_hasValue(false), m_value(T()), Value(m_value) { }

template <typename T>
Nullable<T>::Nullable(const T &value)
    : m_hasValue(true), m_value(value), Value(m_value) { }

template <typename T>
Nullable<T>::Nullable(nullptr_t nullpointer)
    : m_hasValue(false), m_value(T()), Value(m_value)
{
    (void)nullpointer;
}

template <typename T>
bool operator==(const Nullable<T> &op1, const Nullable<T> &op2)
{
    if (op1.m_hasValue != op2.m_hasValue)
        return false;

    if (op1.m_hasValue)
        return op1.m_value == op2.m_value;
    else
        return true;
}

template <typename T>
bool operator==(const Nullable<T> &op, const T &value)
{
    if (!op.m_hasValue)
        return false;

    return op.m_value == value;
}

template <typename T>
bool operator==(const T &value, const Nullable<T> &op)
{
    if (!op.m_hasValue)
        return false;

    return op.m_value == value;
}

template <typename T>
bool operator==(const Nullable<T> &op, nullptr_t nullpointer)
{
    (void)nullpointer;
    if (op.m_hasValue)
        return false;
    else
        return true;
}

template <typename T>
bool operator==(nullptr_t nullpointer, const Nullable<T> &op)
{
    (void)nullpointer;
    if (op.m_hasValue)
        return false;
    else
        return true;
}

template <typename T>
const Nullable<T> & Nullable<T>::operator=(const Nullable<T> &value)
{
    m_hasValue = value.m_hasValue;
    m_value = value.m_value;
    return *this;
}

template <typename T>
const Nullable<T> & Nullable<T>::operator=(const T &value)
{
    m_hasValue = true;
    m_value = value;
    return *this;
}

template <typename T>
const Nullable<T> & Nullable<T>::operator=(nullptr_t nullpointer)
{
    (void)nullpointer;
    m_hasValue = false;
    m_value = T();
    return *this;
}