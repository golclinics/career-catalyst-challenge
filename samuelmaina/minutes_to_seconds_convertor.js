
const assert= require('assert');
const multiplier= 60;

//The upperlimit must be divided by multiplier since the function is returning the 
//minutes*multiplier.if the upperlimit is just the max value then multiplying  it by multiplier
//would cause an overflow.
//get the floor to make it an int.
const upperLimit= Math.floor(Number.MAX_SAFE_INTEGER/multiplier);

//assuming that the minutes that can be converted in the real world are
//only non-negative.
const lowerLimit=0;


function minutesToSecondsConverter(minutes){
    const error= "Minutes value must be a whole number between  " + lowerLimit + " and " + upperLimit;
    if(!Number.isInteger(minutes)) throw new Error(error);
    if(!(minutes>=lowerLimit && minutes<=upperLimit)){
        throw new Error(error);
    }
    return minutes* multiplier;
}



const expectedError= "Minutes value must be a whole number between  " + lowerLimit + " and " + upperLimit;


//should throw for non-numeric inputs
const nonNumeric= '5';
assert.throws(()=>{
    minutesToSecondsConverter(nonNumeric);
},constructErrorObjectFromMessage(expectedError));




//should throw for float values
const float= 0.001;
assert.throws(()=>{
    minutesToSecondsConverter(float);
},constructErrorObjectFromMessage(expectedError));

//Applying Boundary value analysis Testing
//since they are int, the delta value must be 1.
const deltaValue=1;

//test to see that it throw when minutes are lower than lowerlimit.
assert.throws(()=>{
    minutesToSecondsConverter(lowerLimit-deltaValue);
},constructErrorObjectFromMessage(expectedError));



//should not throw exactly at lowerLimit 
assert.doesNotThrow(()=>{
    minutesToSecondsConverter(lowerLimit);
});

//assert that it calculates the correct for the lowerlimit  exaltly.
assert.equal(lowerLimit*multiplier,minutesToSecondsConverter(lowerLimit));


//should not throw exactly at UpperLimit
assert.doesNotThrow(()=>{
    minutesToSecondsConverter(upperLimit);
});


//assert that it calculates the correct for the upperlimit exaltly.
assert.equal(upperLimit*multiplier,minutesToSecondsConverter(upperLimit));





//should throw when upper limit is exceeded.
assert.throws(()=>{
    minutesToSecondsConverter(upperLimit + deltaValue);
},constructErrorObjectFromMessage (expectedError));




//had to construct the function since , the interpreter is complaining that 
//the error message and the Error are the same.
function constructErrorObjectFromMessage(msg){
    return new Error(msg);
}