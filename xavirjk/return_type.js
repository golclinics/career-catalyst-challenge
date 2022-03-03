function returnType(arg) {
  return typeof arg;
}

const test = (arg1, arg2, arg3) => {
  let type = returnType(arg1);
  if (type !== arg2)
    console.log(`test ${arg3} failed expected ${arg2} but received ${arg1} `);
  else console.log(`test ${arg3} passed`);
};
test('', typeof '', 1);
test({}, typeof {}, 2);
test(1, typeof 1, 3);

module.exports = returnType;
