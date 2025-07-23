// Input boxes styles for veg. page.

const choice_box1 = document.getElementById("vegetable");
const choice_box2 = document.getElementById("veg_gramm");
const choice_box3 = document.getElementById("meat");
const choice_box4 = document.getElementById("meat_gramm");
const choice_box5 = document.getElementById("grain")
const choice_box6 = document.getElementById("grain_gramm")

choice_box1.addEventListener("mouseover", () => {
    choice_box1.classList.add("lum");
});
choice_box1.addEventListener("mouseout", () => {
    choice_box1.classList.remove("lum");
});

choice_box2.addEventListener("mouseover", () => {
    choice_box2.classList.add("lum");
});
choice_box2.addEventListener("mouseout", () => {
    choice_box2.classList.remove("lum");
});

// Input boxes styles for meat page.

choice_box3.addEventListener("mouseover", () => {
    choice_box3.classList.add("lum");
});
choice_box3.addEventListener("mouseout", () => {
    choice_box3.classList.remove("lum");
});

choice_box4.addEventListener("mouseover", () => {
    choice_box4.classList.add("lum");
});
choice_box4.addEventListener("mouseout", () => {
    choice_box4.classList.remove("lum");
});

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