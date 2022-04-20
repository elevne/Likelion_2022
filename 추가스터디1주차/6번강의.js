let str = "abc"; // 큰따옴표
let str2 = 'def'; //작은따옴표

console.log(str, str2);

let str = "I'm Fine Thank you!"; // 큰따옴표가 포함되어져 있으면 작은따옴표로 문자열 작성
let str2 = 'I"m Fine Thank you!'; // 반대의 경우도 마찬가지

console.log(str, str2);

// 둘 다 있으면? 
let str = "I'm Fine Thank you! \"and you?\""; // \(역슬래시) 사용하여 escape
console.log(str);