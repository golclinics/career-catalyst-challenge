const assert = require('assert');
const returnType = (arg) => {
  return typeof arg;
};
const tests = () => {
  try {
    assert.strictEqual(returnType(1), typeof 0, `test failed`);
    assert.strictEqual(returnType('string'), typeof 'string', `test failed`);
    assert.strictEqual(returnType(['array']), typeof {}, `test failed`);
    console.log('all tests passed');
  } catch (err) {
    console.error(err);
  }
};
tests();
module.exports = returnType;
