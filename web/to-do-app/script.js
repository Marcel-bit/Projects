const inputBox = document.getElementById('input-box');
const listContainer = document.getElementById('list-container');

// Create a function called addTask
function addTask(){
    if(inputBox.value ===''){
        // if user pressed the button with no text to create a task with, shoes a pop-up
        alert('Write something');
    }
    else{
        // if user pressed the button with text in it, create a list element
        let li = document.createElement('li'); // create list element <li></li>
        li.innerHTML = inputBox.value; // adds text to already made list element
        listContainer.appendChild(li); // display this li under list container
        
        //creates an elemnt span
        let span = document.createElement('span');
        span.innerHTML = '\u00d7';//x symbol inside span
        li.appendChild(span); // displays x next to li element
    }
    inputBox.value = '';
    saveData();
}

//create a listener inside listContainer where we have the tasks stored
listContainer.addEventListener('click', function(e){
    if (e.target.tagName === 'LI'){
        e.target.classList.toggle('checked');// check if it is unchecked and vice versa, because of toggle
        saveData();
    }
    else if(e.target.tagName === 'SPAN'){
        e.target.parentElement.remove();// if x is clicked remove the parent element which is in this case the li element - the whole task
        saveData();
    }
}, false);

// function to save data
function saveData(){
    localStorage.setItem('data', listContainer.innerHTML);// saves data inside of list container to local storage
}

function showTask(){
    listContainer.innerHTML = localStorage.getItem('data');//shows the saved task when reloaded
}
showTask();