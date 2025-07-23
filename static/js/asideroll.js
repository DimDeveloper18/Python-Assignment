const aside_roll = document.querySelectorAll(".roll");

if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches){
    addAnimation();
}

function addAnimation(){
    aside_roll.forEach(roll => {
        roll.setAttribute("data-animated", true);

        const inroll2 = roll.querySelector('.inroll');
        const roll_cont = Array.from(inroll2.children);

        roll_cont.forEach(item => {
            const duplicatedItem = item.cloneNode(true);
            duplicatedItem.setAttribute("ariahidden", true);
            inroll2.appendChild(duplicatedItem);
        });
    });
}