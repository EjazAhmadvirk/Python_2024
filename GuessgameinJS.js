let secretNumber = Math.floor(Math.random() * 100) + 1;
let guess;
let attempts = 0;

while (guess !== secretNumber) {
  guess = parseInt(prompt("Guess a number between 1 and 100:"));
  attempts++;

  if (guess < secretNumber) {
    alert("Too low! Try again.");
  } else if (guess > secretNumber) {
    alert("Too high! Try again.");
  } else {
    alert(`🎉 Correct! The number was ${secretNumber}. You guessed it in ${attempts} tries!`);
  }
}
