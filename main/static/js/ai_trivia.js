
const rawData = document.getElementById('questions-data').textContent;
const quizData = JSON.parse(rawData);
const questions = quizData.questions;
// console.log(questions[0].question)

let currentIndex = 0;
let score = 0;

const question = document.getElementById('question');
const options = document.querySelectorAll('.option-btn');
const submitButton = document.querySelector('.submit-button');
const submissionButton = document.getElementById('submission-button');
submissionButton.dataset.value = 0
console.log(submissionButton.dataset.value)

let count;
options.forEach((option)=>{
    option.addEventListener('click',()=>{
        if(option.dataset.value != questions[currentIndex].correct_option) {
            option.classList.add('false');
        }
        else {
            ++score;
            console.log(score);
        }
        options.forEach((e)=> {
            e.classList.add('disabled');
        });
        setTrue();
        submitButton.value = option.dataset.value;
        let time = 5;
        submitButton.innerHTML = `Next in ${time--}`;
        count = setInterval(() => {
            submitButton.innerHTML = `Next in ${time--}`;
            if(time <= 0){
                clearInterval(count);
                clearLayers();
                nextQuestion();
            }
        }, 1000);
    });
});

function clearLayers() {
    submitButton.innerHTML = `Next`;
    options.forEach((option)=> {
        option.classList.remove('disabled');
        option.classList.remove('false');
        option.classList.remove('true');
    })
}

function setTrue() {
    options.forEach((option)=> {
        if(option.dataset.value == questions[currentIndex].correct_option) {
            option.classList.add('true');
        }
    });
}

function setQuestion() {
    question.innerHTML = questions[currentIndex].question
    options.forEach((option, index)=>{
        option.dataset.value = option.innerHTML = questions[currentIndex].options[index] 
    })
}

function nextQuestion() {
    if(currentIndex > 8) {
        submissionButton.value = score;
        submissionButton.click();
    }
    currentIndex++;
    setQuestion();
}

function next() {
    clearInterval(count)
    clearLayers();
    nextQuestion();
}

setQuestion();