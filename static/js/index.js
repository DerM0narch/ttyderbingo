const title = document.querySelector('h1');
const container = document.querySelector('.fireworks')
const fireworks = new Fireworks.default(container)
// Array to keep track of selected cells
let selectedCells = [];

// Function to check for bingo
function checkForBingo() {
    // Check rows
    for (let row = 0; row < 5; row++) {
        let bingo = true;
        for (let col = 0; col < 5; col++) {
            if (!selectedCells.includes(row * 5 + col)) {
                bingo = false;
                break;
            }
        }
        if (bingo) {
            toggleVictoryPopup();
            return;
        }
    }

    // Check columns
    for (let col = 0; col < 5; col++) {
        let bingo = true;
        for (let row = 0; row < 5; row++) {
            if (!selectedCells.includes(row * 5 + col)) {
                bingo = false;
                break;
            }
        }
        if (bingo) {
            toggleVictoryPopup();
            return;
        }
    }

    // Check diagonals
    let diagonal1 = true;
    let diagonal2 = true;
    for (let i = 0; i < 5; i++) {
        if (!selectedCells.includes(i * 5 + i)) {
            diagonal1 = false;
        }
        if (!selectedCells.includes(i * 5 + (4 - i))) {
            diagonal2 = false;
        }
    }
    if (diagonal1 || diagonal2) {
        toggleVictoryPopup();
        return;
    }

    fireworks.stop();
}

// Grey out the image if it is clicked and cross out the alt text
document.querySelectorAll('td').forEach(item => {
    item.addEventListener('click', event => {
        // Toggle the class of the image
        item.classList.toggle('selected');
        // Toggle the alt text if img element inside
        if (item.querySelector('img')) {
            item.querySelector('img').style.textDecoration = item.querySelector('img').style.textDecoration === 'line-through' ? 'none' : 'line-through';
        }


        // Update the selectedCells array
        const cellId = parseInt(item.id);
        const index = selectedCells.indexOf(cellId);
        if (index === -1) {
            selectedCells.push(cellId);
        } else {
            selectedCells.splice(index, 1);
        }

        // Check for bingo after each click
        checkForBingo();
    });
});

function toggleVictoryPopup() {
    fireworks.start();
    var popup = document.getElementById("popup");
    popup.innerHTML = `<div>
    <div class="popuptext" id="victoryPopup">
      <h1>CONGRATULATIONS!</h1>
      <p>You got a bingo!</p>
      <a href="/"><button>New game</button></a>
    </div>
  </div>`;
    popup.style.alignContent = "center";
    popup.style.verticalAlign = "center";
    popup.style.paddingBottom = "5%";
        setTimeout(() => {
        fireworks.stop();
    }, 10000);
}