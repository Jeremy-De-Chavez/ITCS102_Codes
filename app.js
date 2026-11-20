const form = document.querySelector("#task-form");
const input = document.querySelector("task-input");
const list = document.querySelector("#task-list")

let task = [];

function savetasks() {
    localStorage.setItem("task", JSON.stringify(task));
}

function addtask(text) {
    if (text === "") return;
    const task = {  id: crypto.randomUUID(), text: text, done: false};
    task.push(task);
    savetasks();
    renderTasks();
}

function render() {
    list.innerHTML = ""

    task.forEach((task)=>{
        const li = document.createElement('li')
        const text = document.createElement
        ("span")
        text.textContent = task.text
        if(task.done) {
            text.style.textDecoration = "line-through"
        }
        const doneBtn = document.createElement
        ('button')
        doneBtn.textContent = task.done ?
        "undo" : "done"
        doneBtn.addEventListener("click", () => {
            toggleTask(task.id)
            console.log("test")
        })
        const deleteBtn = document.createElement("button")
        deleteBtn.textContent = "Delete"
        deleteBtn.addEventListener("click", () => {
            toggleTask(task.id)
            console.log("test")
        })
        li.appendChild(text)
        li.appendChild(doneBtn)
        li.appendChild(deleteBtn)
        list.appendChild(li)
    })
}
function toggleTask(id) {
    const task = task.find(t => t.id === id)
    if(!task) return task.done = !task.done
    savetasks()
    renderTask()
}

function toggleTask(id) {
    const task = task.find(t=>t.id !== id)
    savetasks()
    renderTask()
}
form.addEventListener("submit", (e)=> {
    e.preventDefault()
    const text = input.value.trim()
    addtask(task)
    input.value = ""
})

rendertask()

