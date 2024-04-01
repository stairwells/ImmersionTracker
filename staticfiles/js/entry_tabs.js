let current_box = document.getElementById('reading');
const entry_tabs = document.querySelectorAll('.entry-category-tab');

function setUpTabs() {
    entry_tabs.forEach((el) => {
        el.addEventListener('click', (e) => {
            let entry_box = document.getElementById(el.textContent.toLowerCase());
            current_box.style.display = 'none';
            entry_box.style.display = 'block';
            current_box = entry_box;
        })
    })
}

setUpTabs();
