const tasks = document.getElementsByTagName("li")
const removeBtn = document.querySelector('.remove-complete-btn');

function line(){
   for(let i = 0;i < tasks.length; i++)
{
    tasks[i].addEventListener('click', function handleClick() {
        tasks[i].style.textDecoration = "line-through";
        tasks[i].style.color='red';
    });
}
}

removeBtn.addEventListener("click", () => {
    tasks.forEach(task => {
        const checked = task.querySelector('input').checked;
        if( checked ) {
            task.remove();
        }
    });
    //console.log(tasks);
});