const navbar =document.getElementById('navbar')
function showsidebar(){
    navbar.style.display='flex'
}
function hidesidebar(){
    navbar.style.display='none'
}

const availableProducts=document.querySelector('.available-products')
const deliveredProducts=document.querySelector('.delivered-products')
const delivering=document.querySelector('.delivering')

// let times = 0;

//    let id = setInterval(function() {
//     availableProducts.textContent = times * 10;
//     deliveredProducts.textContent = times * 3;
//     delivering.textContent = times * 1;
//     times++;
//     if(times == 100){
//         window.clearInterval(id)
//     }
// }, 30);

const heading = document.querySelector ('.main-text');
let text = 'Assalam-u-Alaikum I\'m Muhammad Ahtisham Yousaf';
let texts = ['Assalam-u-Alaikum I\'m Muhammad Ahtisham Yousaf','Nice To Meet You']
let endvalue = 1;
isForwards = true;
textCount = 0;

let textId = setInterval(function(){
    heading.textContent = texts[textCount].substring(0,endvalue)
    if(isForwards){
    endvalue++;

    }
    else {
        endvalue--;
    }

    if(endvalue > texts.length + 50){
        isForwards = false;
    }
    if(endvalue < 0){
        isForwards = true;
        textCount++;
    }
    if(textCount == texts.length){
        textCount = 0;
    }
},100)