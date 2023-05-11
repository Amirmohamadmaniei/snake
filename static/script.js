const playBoard = document.querySelector(".play-board");
const scoreElement = document.querySelector(".score");
const highScoreElement = document.querySelector(".high-score");
const controls = document.querySelectorAll(".controls i");
const scoreHiddenElement = document.getElementById('score')

let gameOver = false;
let foodX, foodY;
let snakeX = 5, snakeY = 5;
let snakeBody = [];
let vlocityX = 0, vlocityY = 0;
let setIntervalId;
let score = 0;





// let highScore = localStorage.getItem("high-score") || 0;
let highScore = document.getElementById('high-score').value;
highScoreElement.innerHTML = `High Score : ${highScore}`;


const changeFoodPosition = () => {
    foodX = Math.floor(Math.random() * 30) + 1;
    foodY = Math.floor(Math.random() * 30) + 1;
}


const handleGameOver = () => {
    clearInterval(setIntervalId);
    alert("Game Over ...");
    location.reload();
}


const changeDirection = (e) => {
    if(e.key === "ArrowUp" && vlocityY != 1){
        vlocityX = 0;
        vlocityY = -1;
    }else if (e.key === "ArrowDown" && vlocityY != -1){
        vlocityX = 0;
        vlocityY = 1;
    }else if (e.key === "ArrowRight" && vlocityX != -1){
        vlocityX = 1;
        vlocityY = 0;
    }else if (e.key === "ArrowLeft" && vlocityX != 1){
        vlocityX = -1;
        vlocityY = 0;
    }
}

controls.forEach(key => {
    key.addEventListener("click", () => changeDirection({ key: key.dataset.key }));
});

const initGame = () => {
    if (gameOver) return handleGameOver();
    let htmlMarkup = `<div class="food" style="grid-area: ${foodY} / ${foodX}"> </div>`;


    if (snakeX === foodX && snakeY === foodY) {
        changeFoodPosition();
        snakeBody.push([foodX, foodY]);

        score++;
        
        highScore = score >= highScore ? score : highScore;
        localStorage.setItem("high-score", highScore);

        scoreElement.innerHTML = `Score : ${score}`;
        highScoreElement.innerHTML = `High Score : ${highScore}`;
    }


    for (let i = snakeBody.length - 1; i > 0; i--) {
        snakeBody[i] = snakeBody[i - 1];
    }

    snakeBody[0] = [snakeX, snakeY];

    snakeX += vlocityX;
    snakeY += vlocityY;

    if (snakeX <= 0 || snakeX > 30 || snakeY <= 0 || snakeY > 30) {
        gameOver = true;

        scoreHiddenElement.value = score
        document.getElementById("form-score").submit();
    }

    for (let i = 0; i < snakeBody.length; i++) {
        htmlMarkup += `<div class="head" style="grid-area: ${snakeBody[i][1]} / ${snakeBody[i][0]}"> </div>`;

        if (i !== 0 && snakeBody[0][1] === snakeBody[i][1] && i !== 0 && snakeBody[0][0] === snakeBody[i][0]) {
            gameOver = true;

            scoreHiddenElement.value = score
            document.getElementById("form-score").submit();
        }
    }
    playBoard.innerHTML = htmlMarkup;
}



changeFoodPosition();
setIntervalId = setInterval(initGame, 125);
document.addEventListener("keydown", changeDirection);