const tasks = document.getElementsByTagName("li")
const removeBtn = document.querySelector('.remove-complete-btn');

function line(){
   for(let i = 0;i < tasks.length; i++){
    tasks[i].addEventListener('click', function() {
    tasks[i].classList.toggle("linethrough");

    });
}
}
