// Stack: Intro
#include <array>
#include <vector>
#include <assert.h>
#include <stack>
#include <queue>
using namespace std;

template < class T >
class Stack
{
	vector<T> storage;
public:
	// Constructor
	Stack()
	{

	}
	bool stack_empty() {
		return this->storage.empty();
	}
	void push(const T& x) {
		this->storage.push_back(x);
	}
	T pop() {
		if (stack_empty()) {
			throw "stack_underflow";
		}
		else {
			T& retval = this->storage[this->storage.size() - 1];
			this->storage.pop_back();
			return retval;
		}
	}
};

template < class T>
class Deque
{
	vector<T> storage;
public:
	// Constructor
	Deque()
	{

	}
	bool empty() {
		return this->storage.empty();
	}
	void push_tail(const T& x) {
		this->storage.push_back(x);
	}
	void push_head(const T& x) {
		this->storage.insert(0, x);
	}
	T pop_tail() {
		if (empty()) {
			throw "underflow";
		}
		else {
			T& retval = this->storage[this->storage.size() - 1];
			this->storage.pop_back();
			return retval;
		}
	}
	T pop_head() {
		if (empty()) {
			throw "underflow";
		}
		else {
			T& retval = this->storage[0];
			this->storage.erase(0);
			return retval;
		}
	}
};

template < class T, size_t size>
class deque_array
{
	array<T, size> storage;
	int head;
	int tail;
public:
	// Constructor
	deque_array()
	{
		head = 0;
		tail = 0;
	}
	bool empty() {
		if (head == tail) {
			return true;
		}
		else {
			return false;
		}
	}
	bool full() {
		if (tail + 1 == head || (tail == size-1 && head == 0)) {
			return true;
		}
		else {
			return false;
		}
	}
	void push_tail(const T& x) {
		if (full()) {
			throw "overflow";
		}
		else {
			storage[tail] = x;
			tail = (tail+1) % size;
		}
	}
	void push_head(const T& x) {
		if (full()) {
			throw "overflow";
		}
		else {
			head = (head+size-1) % size;
			storage[head] = x;
		}
	}
	T pop_tail() {
		if (empty()) {
			throw "underflow";
		}
		else {
			tail = (tail+size-1) % size;
			T& retval = storage[tail];
			return retval;
		}
	}
	T pop_head() {
		if (empty()) {
			throw "underflow";
		}
		else {
			T& retval = storage[head];
			head = (head+1) % size;
			return retval;
		}
	}
};


int main() {
	stack<int> test;
	test.push(15);
	test.push(6);
	test.push(2);
	test.push(9);
	assert(test.top() == 9);
	test.push(17);
	test.push(3);
	assert(test.top() == 3);
	queue<int> test2;
	Deque<int> test3;
	deque_array<int, 3> test4;
	test4.push_tail(9);
	test4.push_head(16);
	assert(test4.pop_tail() == 9);
	assert(test4.pop_tail() == 16);
	test4.push_tail(28);
	test4.push_tail(2);
	assert(test4.pop_head() == 28);
	assert(test4.pop_head() == 2);
	test4.push_head(5);
	test4.push_head(10);
	assert(test4.pop_tail() == 5);
	assert(test4.pop_tail() == 10);
	return 0;
}