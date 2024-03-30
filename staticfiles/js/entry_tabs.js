let current_box = document.getElementById('reading');
const entries = document.querySelectorAll('.entry-category-tab');
console.log(document.getElementById('srs'))

function setUpTabs() {
    entries.forEach((el) => {
        el.addEventListener('click', (e) => {
            let entry_box = document.getElementById(el.textContent.toLowerCase());
            current_box.style.display = 'none';
            entry_box.style.display = 'block';
            current_box = entry_box;
        })
    })
}

setUpTabs();
