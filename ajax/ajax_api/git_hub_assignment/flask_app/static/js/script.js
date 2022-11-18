const CREATE_USER_FORM = document.querySelector('#create_user_form')
const USER_WRAPPER = document.querySelector('#user_wrapper')


CREATE_USER_FORM.addEventListener('submit', (e) => {
    e.preventDefault()
    const current_form = document.querySelector('#create_user_form')
    const form_data = new FormData(current_form)
    // console.log(document.querySelector('#first_name').value)
    // console.log(document.last_name.value)
    console.log(form_data)
    console.log(current_form)
    fetch('http://localhost:5000/user/create', {method: 'POST', body: new FormData(CREATE_USER_FORM)})
        .then(res => res.json())
        .then((jsonData) => {
            if(jsonData.status == 200) {
                let error_wrapper = document.querySelector('#error_message')
                error_wrapper.classList.add('d-none')
                update_user_table()
                CREATE_USER_FORM.reset()
            } else if(jsonData.status == 501) {
                let error_wrapper = document.querySelector('#error_message')
                error_wrapper.innerText = jsonData.message
                error_wrapper.classList.remove('d-none')
            }
        })
}) 

document.addEventListener('DOMContentLoaded', () => {
    console.log('Page is loaded')

    update_user_table()
})

function update_user_table() {
    console.log('Updating User Table')
    fetch('http://localhost:5000/user/get_all', {method: 'GET'})
        .then(response => response.json())
        .then((jsonData) => {
            removeAllChildNodes(USER_WRAPPER)

        for(let user in jsonData.all_users) {
            let row = document.createElement('tr')

            let first_name = document.createElement('td')
            first_name.innerText = jsonData.all_users[user].first_name
            row.appendChild(first_name)

            let last_name = document.createElement('td')
            last_name.innerText = jsonData.all_users[user].last_name
            row.appendChild(last_name)

            USER_WRAPPER.appendChild(row)
        }
    })
}

function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}
