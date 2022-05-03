const sum = (num1, num2) => {
    return num1+num2;
}


const result = sum(1, 2);
console.log(result);



const pow = x => x*x;

const result = pow(10);
console.log(result);



const printPie = () => 3.14;

const result = printPie;
console.log(result);



const getObject = () => ({
    name:'철수',
    age: 20
});
const obj = getObject();
console.log(obj.name)
