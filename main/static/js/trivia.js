const options = document.querySelectorAll('.option-btn');
let answer = document.querySelector('.answer').dataset.answer;
const submitButton = document.querySelector('.submit-button');

options.forEach((option)=>{
    option.addEventListener('click',()=>{
        if(option.dataset.value != answer) {
            option.classList.add('false');
        }
        options.forEach((e)=> {
            e.classList.add('disabled');
        });
        setTrue();
        submitButton.value = option.dataset.value;
        let time = 5;
        submitButton.innerHTML = `Next in ${time--}`;
        const count = setInterval(() => {
            submitButton.innerHTML = `Next in ${time--}`;
            if(time <= 0){
                clearInterval(count);
                submitButton.click();
            }
        }, 1000);
    });
});

function setTrue() {
    options.forEach((option)=> {
        if(option.dataset.value == answer) {
            option.classList.add('true');
        }
    });
}