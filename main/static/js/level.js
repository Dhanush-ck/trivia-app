const easyButton = document.querySelector('.easy-button');
const mediumButton = document.querySelector('.medium-button');
const hardButton = document.querySelector('.hard-button');

const easy = document.querySelector('.easy');
const medium = document.querySelector('.medium');
const hard = document.querySelector('.hard');

const levelButtons = document.querySelectorAll('.level-button');

easyButton.onclick = ()=> {
    easy.checked = true;
};

mediumButton.onclick = ()=> {
    medium.checked = true;
};

hardButton.onclick = ()=> {
    hard.checked = true;
};

levelButtons.forEach((levelButton)=> {
    levelButton.addEventListener('click', ()=> {
        levelButton.classList.add('checked');
        for(let button of levelButtons){
            if(button != levelButton){
                button.classList.remove('checked');
            }
        }
    });
});