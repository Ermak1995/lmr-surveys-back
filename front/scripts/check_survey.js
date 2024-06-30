function check_survey() {
    // alert('Вы прошли опрос')
    // get user's answers
    let list_task = document.getElementsByClassName('list-task')[0]
    var list_users_answers = new Map()
    for (let question of list_task.children) {
        // console.log(question.id)
        let list_answers = question.getElementsByClassName("button_text")
        // console.log(list_answers)
        for (let answer of list_answers) {
            if (answer.firstChild.checked) {
                list_users_answers.set(question.id, answer.innerText)
            }
        }
    }
    let params = new URLSearchParams(location.search)
    let uuid = params.get('uuid')
    console.log(JSON.stringify(Object.fromEntries(list_users_answers)))
    fetch(
        `http://127.0.0.1:8000/check-survey?uuid=${uuid}`, 
        {
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(Object.fromEntries(list_users_answers)),
        }
    )
    .then(res => res.json())
    .then(data => {
        alert(`Опрос успешно пройден. Ваш результат ${data["counter"]} из ${data["max_counter"]}`)
        window.location.href = 'file:///D:/Survey/front/index.html'

    })
}
