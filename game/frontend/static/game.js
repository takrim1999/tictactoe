const board = document.getElementById('board');
const statusText = document.getElementById('status');
const restartButton = document.getElementById('restartButton');

let currentPlayer = 'X';
let gameActive = true;
let boardState = Array(9).fill(null);

const winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
];

function initializeBoard() {
    board.innerHTML = '';
    boardState.fill(null);
    for (let i = 0; i < 9; i++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.dataset.index = i;
        cell.addEventListener('click', handleCellClick);
        board.appendChild(cell);
    }
    updateStatus();
}

function handleCellClick(event) {
    const cell = event.target;
    const index = cell.dataset.index;

    if (!gameActive || boardState[index] !== null) return;

    boardState[index] = currentPlayer;
    cell.textContent = currentPlayer;
    cell.classList.add('taken');

    if (checkWin()) {
        statusText.textContent = `Player ${currentPlayer} Wins!`;
        gameActive = false;
    } else if (boardState.every(cell => cell !== null)) {
        statusText.textContent = `It's a Draw!`;
        gameActive = false;
    } else {
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        updateStatus();
    }
}

function checkWin() {
    return winningConditions.some(condition =>
        condition.every(index => boardState[index] === currentPlayer)
    );
}

function updateStatus() {
    statusText.textContent = `Player ${currentPlayer}'s Turn`;
}

restartButton.addEventListener('click', () => {
    currentPlayer = 'X';
    gameActive = true;
    initializeBoard();
});

initializeBoard();
