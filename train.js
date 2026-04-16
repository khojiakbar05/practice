// A-TASK (NodeJS)
/*
Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/
// Masalani yechimi
// Define (parametr)
function countLetter(letter, word) {
 let count = 0;
  for (let i = 0; i < word.length; i++) {
    if (word[i] === letter) {
      count ++;
    }
  }
  return count;
}

// Call (argument)
console.log(countLetter("e", "engineer")); 
