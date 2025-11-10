// Source - https://stackoverflow.com/a/145649
// Posted by Florian Bösch, modified by community. See post 'Timeline' for change history
// Retrieved 2025-11-09, License - CC BY-SA 4.0

#include <iostream>
#include <thread>
#include <cmath>

class Foo{
	public:
		void bar(){
			std::cout << "Hello" << std::endl;
		}
		double heavy_calculation(int n) {
			double result = 0.0;
			for(int i = 0; i < n; ++i) {
				result += std::sqrt(i) * std::sin(i);
			}
			printf("Heavy calculation done: %f\n", result);
			return result;
		}
};

// Source - https://stackoverflow.com/a/145649
// Posted by Florian Bösch, modified by community. See post 'Timeline' for change history
// Retrieved 2025-11-09, License - CC BY-SA 4.0

extern "C" {
	Foo* Foo_new(){ return new Foo(); }
	void Foo_bar(Foo* foo){ foo->bar(); }
	double Foo_heavy_calculation(Foo* foo, int n) { return foo->heavy_calculation(n); }
}
