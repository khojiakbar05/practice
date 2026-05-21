//git commit -m "feat: P-TASK (NodeJS) DONE!" 

// Shunday function yozing, u object qabul qilsin va arrayni object arrayga otkazib arrayni qaytarsin qaytarsin.
// MASALAN: objectToArray( {a: 10, b: 20}) return [['a', 10], ['b', 20]]
// Masalani Yechish:
 function objectArray(obj) {
    const object = []

    for (let key in obj) {
        object.push([key, obj[key]])
    }
    return object
 }
const result = objectArray({ a: 10, b: 20 });
console.log("objectArray: ", result);

 





// N-TASK (NodeJS)

// Shunday function yozing, u raqamlardan tashkil topgan array qabul qilsin va array ichidagi har bir raqam uchun raqamni ozi va hamda osha raqamni kvadratidan tashkil topgan object hosil qilib, hosil bolgan objectlarni array ichida qaytarsin.
// MASALAN: getSquareNumbers([1, 2, 3]) return [{number: 1, square: 1}, {number: 2, square: 4}, {number: 3, square: 9}];
// masalani yechish
// function getSquareNumbers(arr) {
//     return arr.map( num => {
//         return {
//             number: num,
//             square: num * num
//         };
//     });
// }

// console.log("Numbers: ", getSquareNumbers([1, 2, 3]));






// L-TASK (NodeJS)

// Shunday function yozing, u string qabul qilsin va string ichidagi hamma sozlarni chappasiga yozib va sozlar ketma-ketligini buzmasdan stringni qaytarsin.
// MASALAN: reverseSentence("we like coding!") return "ew ekil gnidoc";
// masalani yechish:

// function reverseSentence(str) {
//     return str.split(` `).map(word => word.split(``).reverse().join(``)).join(` `);
// }

// console.log(`Reversed sentence: `, reverseSentence("We like coding"));






// J-TASK (NodeJS)

// Shunday function yozing, u parametridagi array ichida eng kop takrorlangan raqamni topib qaytarsin.
// MASALAN: majorityElement([1,2,3,4,5,4,3,4]) return 4
// masalani yechish:
// function majorityElement(arr) {
//     let count = [];
//     let maxNum = 0;
//     let result = 0;

//     for(let num of arr) {
//         count[num] = (count[num] || 0) + 1;
//         if(count[num] > maxNum) {
//             maxNum = count[num];
//             result = num
//         }
//     }
//     return result;
// }
// console.log(`The majorityElement:`, majorityElement([1, 2, 3, 4, 5, 4, 3, 4]));




// H-TASK (NodeJS)

// shunday function tuzing, u integerlardan iborat arrayni argument sifatida qabul qilib, faqat positive qiymatlarni olib string holatda return qilsin
// MASALAN: getPositive([1, -4, 2]) return qiladi "12"
// masalani yechish

// function getPositive(arr) {
//     return arr.filter(num => num > 0).join("")
// }

// console.log("the result: ", getPositive([1, -4, 2]));

// F-TASK (NodeJS)

// Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, agar stringda bir hil harf qatnashgan bolsa true, qatnashmasa false qaytarishi kerak.
// MASALAN: getReverse("hello") return true return qiladi
// Masalani yechish:
// function findDoublers(str) {
//        const word = str.toLowerCase().split(``).sort();

//        for (i = 0; i < str.length -1; i++) {
//               if (word[i] === word[i + 1]) {
//                      return true
//               }
//        }
//        return false
// }
// console.log(findDoublers("hello"));



// E-TASK (NodeJS)

// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"
// Masalani yechish:

// function getReverse(str) {
//        return str.split(``).reverse().join(``)
// }

// console.log(getReverse("hello"))



// D-TASK (NodeJS)

// Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
// MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.

// masalani yechimi
// function getHighestIndex(arr) {f
//   let max = 0;
//   let maxIndex = [0];

//   for (let i = 1; i < arr.length; i++) {
//     if (arr[i] > max) {
//       max = arr[i]
//       maxIndex = i
//     }
//   }
//   return maxIndex
// }

// console.log(getHighestIndex([5, 21, 12, 21, 8]));




//.  C-TASK (NodeJS)
/*
Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;
 */
// masalani yechimi
// function checkContent(str1, str2) {
//   if (str1.length !== str2.length) {
//     return False;
//   }

//   const sortedStr1 = str1.toLowerCase().split(``).sort().join(``);
//   const sortedStr2 = str2.toLowerCase().split(``).sort().join(``);

//   return sortedStr1 === sortedStr2;
// }

// console.log(checkContent("mitgroup", "Ourgpimt"));




//. B-TASK (NodeJS)
/*
Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
 */

// masalani yechimi
// Define (parametr)
// function countDigits(str) {
//   let count = 0;
//   for (let i = 0; i < str.length; i++) {
//     if (str[i] >= "0" && str[i] <= "9") {
//       count++;
//     }
//   }
//   return count;
// }

// console.log(countDigits("ad2a54y79wet3sfgb9"));

// A-TASK (NodeJS)
/*
Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/
// Masalani yechimi
// Define (parametr)
// function countLetter(letter, word) {
//  let count = 0;
//   for (let i = 0; i < word.length; i++) {
//     if (word[i] === letter) {
//       count ++;
//     }
//   }
//   return count;
// }

// // Call (argument)
// console.log(countLetter("e", "engineer"));
