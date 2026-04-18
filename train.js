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

//. B-TASK (NodeJS)
/*
Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
 */

// masalani yechimi
// Define (parametr)
function countDigits(str) {
  let count = 0;
  for (let i = 0; i < str.length; i++) {
    if (str[i] >= "0" && str[i] <= "9") {
      count++;
    }
  }
  return count;
}

console.log(countDigits("ad2a54y79wet3sfgb9"));
