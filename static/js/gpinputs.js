const choice_box5 = document.getElementById("grain")
const choice_box6 = document.getElementById("grain_gramm")

// Input boxes styles for grain page.

choice_box5.addEventListener("mouseover", () => {
    choice_box5.classList.add("lum");
});
choice_box5.addEventListener("mouseout", () => {
    choice_box5.classList.remove("lum");
});

choice_box6.addEventListener("mouseover", () => {
    choice_box6.classList.add("lum");
});
choice_box6.addEventListener("mouseout", () => {
    choice_box6.classList.remove("lum");
});