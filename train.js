// D-TASK (NodeJS)

// Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
// MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.

// masalani yechimi
function getHighestIndex(arr) {
  let max = 0;
  let maxIndex = [0];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i]
      maxIndex = i
    }
  }
  return maxIndex
}

console.log(getHighestIndex([5, 21, 12, 21, 8]));




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
