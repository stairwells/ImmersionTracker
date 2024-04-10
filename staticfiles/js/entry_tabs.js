let current_box = document.getElementById('reading');
const tabs = document.querySelectorAll('.category-tab');

function setUpTabs() {
    let box;
    tabs.forEach((el) => {
        el.addEventListener('click', () => {
            box = document.getElementById(el.textContent.toLowerCase());
            current_box.style.display = 'none';
            box.style.display = 'block';
            current_box = box;
        })
    })
}

setUpTabs();
