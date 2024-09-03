#include <iostream>
#include <vector>
#include <cmath>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#define matrix std::vector<std::vector<double>>

matrix dot(const matrix& A, const matrix& B) {
  matrix C(2, std::vector<double>(2));
  C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0];
  C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1];
  C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0];
  C[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1];
  return C;
}

void add(matrix& A, const matrix& B) {
  A[0][0] += B[0][0];
  A[0][1] += B[0][1];
  A[1][0] += B[1][0];
  A[1][1] += B[1][1];
}

void scale(matrix& A, double f) {
  A[0][0] *= f;
  A[0][1] *= f;
  A[1][0] *= f;
  A[1][1] *= f;
}

matrix mexp(double b, const matrix& M, double limit=1e6) {
  matrix T = {
    {1, 0},
    {0, 1}
  };

  matrix S = {
    {1, 0},
    {0, 1}
  };

  for (double t = 1.0; t < limit; t += 1.0) {
    T = dot(T, M);
    scale(T, log(b)/t);
    add(S, T);
  }

  return S;
}

matrix mzeta(matrix& M, double limit=10.0) {

  matrix S = {{0, 0}, {0, 0}};
  scale(M, -1.0);
  for (double t = 1; t <= limit; t += 1.0) {
    add(S, mexp(t, M, 1e3));
  }
  return S;
}

void display(const matrix& A) {
  for (int y = 0; y < 2; ++y) {
    for (int x = 0; x < 2; ++x) {
      std::cout << A[y][x] << '\t';
    }std::cout << '\n';
  }
}
PYBIND11_MODULE(cheat, handle){
	handle.doc() = "matrix expo";
	
	pybind11::module std = handle.def_submodule("std", "consists the random functions");
	std.def("dot", &dot);
	std.def("add", &add);
	std.def("scale", &scale);
	std.def("mexp", &mexp);
	std.def("mzeta", &mzeta);
	std.def("display", &display);

}

