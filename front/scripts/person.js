function showPerson (persons) {
    persons = JSON.parse(persons)
    for (let person of persons) {
        let name = person.name
        let age = person.age
        console.log(name, age)
    }
}



// console.log(persons)
// console.log(data)