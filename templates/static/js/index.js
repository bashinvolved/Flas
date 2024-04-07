document.querySelector("#hamburger").addEventListener("click", () => {
    document.querySelector("#hamburger").classList.toggle("navigation-bar__hamburger_active")
    document.querySelector("#fullmenu").classList.toggle("navigation-bar__full-menu_active")
})

document.querySelector("#rent").addEventListener("click", () => {
    scrollTo({top: document.querySelector(".first-slide").offsetTop, behavior: "smooth"})
})

document.querySelector("#service").addEventListener("click", () => {
    scrollTo({top: document.querySelector(".third-slide").offsetTop, behavior: "smooth"})
})

document.querySelector("#rent2").addEventListener("click", () => {
    document.querySelector("#hamburger").classList.toggle("navigation-bar__hamburger_active")
    document.querySelector("#fullmenu").classList.toggle("navigation-bar__full-menu_active")
    scrollTo({top: document.querySelector(".first-slide").offsetTop, behavior: "smooth"})
})

document.querySelector("#service2").addEventListener("click", () => {
    document.querySelector("#hamburger").classList.toggle("navigation-bar__hamburger_active")
    document.querySelector("#fullmenu").classList.toggle("navigation-bar__full-menu_active")
    scrollTo({top: document.querySelector(".third-slide").offsetTop, behavior: "smooth"})
})

let universalObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show")
        } else {
            entry.target.classList.remove("show")
        }
    })
}, {root: null, rootMargin: "0px", threshold: 0})

for (elem of document.querySelectorAll(".observation")) {
    universalObserver.observe(elem)
}
