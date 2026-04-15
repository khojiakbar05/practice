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
