const clear = document.querySelector('.cancel');
const card = document.querySelector('main')

clear.addEventListener('click', close);

function close(){
card.remove()
/*console.log('cleared')*/
}