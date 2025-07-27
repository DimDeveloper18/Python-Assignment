const choice_box3 = document.getElementById("meat");
const choice_box4 = document.getElementById("meat_gramm");

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