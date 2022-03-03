const myFunction = require("./minutes_to_seconds");

//test samples
const samples = [
  [5, 300],
  [3, 180],
  [2, 120],
];
//the results should match the expected values//
test.each(samples)("Should convert minutes to seconds", (sample, result) =>
  expect(myFunction(sample)).toBe(result)
);
