const tasks = document.getElementsByTagName("li")
const removeBtn = document.querySelector('.remove-complete-btn');
var array = [];

function line(){
   for(let i = 0;i < tasks.length; i++)
{
    tasks[i].addEventListener('click', function handleClick() {
        tasks[i].style.textDecoration = "line-through";
        tasks[i].style.color='red';
        array.push(tasks[i]);
        console.log(tasks[i]);

    });
}
}

//function removeComplete() {
////    if array.includes(tasks[i]) {
//        console.log('HEY!');
//    }
//}

//removeBtn.addEventListener("click", () => {
//    tasks.forEach(tasks => {
//        const checked = tasks.querySelector('input').checked;
//        if( checked ) {
////            tasks.remove();
//            console.log('checked!')
//        }
//    });
//    //console.log(tasks);
//});