const apiRandomDogImg   = 'https://dog.ceo/api/breeds/image/random/45'
const apiAllBreeds      = 'https://dog.ceo/api/breeds/list/all'
const request1          = new XMLHttpRequest()
const request2          = new XMLHttpRequest()
const header            = document.getElementById('header')
const main              = document.getElementById('main') 
const input             = document.getElementById('filter-text')
const button            = document.getElementById('filter-btn')
const select            = document.getElementById('filter-select')
const more              = document.getElementById('more')
const toTheTop          = document.getElementById('toTheTop')
const resetBtn          = document.getElementById('reset-btn')
const currentDogs       = []

function displayDogs(item){
    const dogImgDiv = document.createElement("div")
        dogImgDiv.classList.add("flex-item")
        dogImgDiv.innerHTML = `
            <img src=${item}>
        `
        main.appendChild(dogImgDiv)
}

function seclectDogs(){
    request2.open("get", apiAllBreeds)
    request2.addEventListener("load", function(){
        const response = JSON.parse(request2.response)
        Object.keys(response.message).forEach(function(item){
            const option = document.createElement("option")
            option.textContent = item
            option.value = item
            select.appendChild(option)            
        });
    })
    request2.send()
}


window.addEventListener("load", function(){

    request1.open("get", apiRandomDogImg)
    request1.addEventListener("load", function(){
        const response = JSON.parse(request1.response)
        response.message.forEach(function(item){
            currentDogs.push(item)
            displayDogs(item)
        })
    })
    request1.send()

    seclectDogs()
})

button.addEventListener("click", function(){
    main.innerHTML = ""
    let filteredDogs = currentDogs.filter(function(item){
        return item.indexOf(input.value) !== -1
    })
    input.value = ""

    filteredDogs.forEach(function(item){
        displayDogs(item)
    })
})

select.addEventListener("change", function(){
    main.innerHTML = ""
    let filteredDogs = currentDogs.filter(function(item){
        return item.indexOf(select.value) !== -1
    })
    
    filteredDogs.forEach(function(item){
        displayDogs(item)
    })
})


more.addEventListener("click", function(){
    request1.open("get", apiRandomDogImg)
    request1.addEventListener("load", function(){
        const response = JSON.parse(request1.response)
        response.message.forEach(function(item){
            currentDogs.push(item)
            displayDogs(item)
        })
    })
    request1.send()
})


toTheTop.addEventListener("click", function(){
    window.scrollTo({top: 0})
})


resetBtn.addEventListener("click", function(){
    request1.open("get", apiRandomDogImg)
    request1.addEventListener("load", function(){
        const response = JSON.parse(request1.response)
        main.innerHTML = ""
        response.message.forEach(function(item){
            currentDogs.push(item)
            displayDogs(item)
        })
    })
    request1.send()
    seclectDogs()
})