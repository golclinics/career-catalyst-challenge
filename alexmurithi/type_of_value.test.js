// lets import our main function//
const typeOfValue = require("./type_of_value");

//lets define the values to test//
const values = [
  [1, "number"],
  [false, "boolean"],
  [{}, "object"],
  [null, "object"],
  ["string", "string"],
  [["array"], "object"],
];

//jest test each value //
test.each(values)("Type value", (value, result) =>
  expect(typeOfValue(value)).toBe(result)
);
