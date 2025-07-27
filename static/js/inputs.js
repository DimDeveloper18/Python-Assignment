// Input boxes styles for veg. page.

const choice_box1 = document.getElementById("vegetable");
const choice_box2 = document.getElementById("veg_gramm");

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
