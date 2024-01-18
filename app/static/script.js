// let currentPlayer = 0;
// let maxScore = 50;
// let playerScores = [0, 0, 0, 0];

// function updateGameStatus() {
//     document.getElementById('status').innerText = `Player ${currentPlayer + 1}'s Turn | Total Score: ${playerScores[currentPlayer]}`;
// }

// function startGame() {
//     currentPlayer = 0;
//     playerScores = [0, 0, 0, 0];
//     updateGameStatus();
// }

// function rollDice() {
    // Make an AJAX request to the server to get the dice roll result
    // Replace the URL with the appropriate endpoint in your Flask app
//     fetch('/roll')
//         .then(response => response.json())
//         .then(data => {
//             handleRollResult(data.value);
//         })
//         .catch(error => {
//             console.log('Error', error);
//         });
// }

// function handleRollResult(value) {
//     if (value === 1) {
//         alert('You rolled a 1! Turn done!');
//         playerScores[currentPlayer] = 0;
//         updateGameStatus();
//     }else {
//         playerScores[currentPlayer] += value;
//         alert(`You rolled a ${value}! Your score is now ${playerScores[currentPlayer]}`);
//         updateGameStatus();
//     }

//     if (playerScores[currentPlayer] >= maxScore) {
//         alert(`Player ${currentPlayer + 1} is the winner with a score of ${playerScores[currentPlayer]}!`);
//     }else {
        // move to the next player
// 

