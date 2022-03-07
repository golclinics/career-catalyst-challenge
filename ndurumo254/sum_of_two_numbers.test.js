const addition = require("./sum_of_two_numbers");

//test cases for sum of two numbers//

test("Should return sum of two numbers", () => {
  expect(addition(2,3)).toBe(5);
});

test("Should return sum of two numbers", () => {
  expect(addition(-3, -6)).toBe(-9);
});

test("Should return sum of two numbers", () => {
  expect(addition(7, 3)).toBe(10);
});
