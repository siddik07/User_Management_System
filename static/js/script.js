
document.addEventListener('DOMContentLoaded', (event) => {
    const openPopupBtn = document.getElementById('openPopupBtn');
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popup = document.getElementById('userreg');
    const openPopupBtn1 = document.getElementById('openPopupBtn1');
    const closePopupBtn1 = document.getElementById('closePopupBtn1');
    const popup1 = document.getElementById('useredit');
    const success =document.getElementById('success');
    const submit =document.getElementById('submit');

    openPopupBtn.addEventListener('click', () => {
        console.log("clickable")
        popup.classList.remove('hidden');
        popup.classList.add('visible');
    });

    closePopupBtn.addEventListener('click', () => {
        popup.classList.remove('visible');
        popup.classList.add('hidden');
    });

     openPopupBtn1.addEventListener('click', () => {
        console.log("clickable")
        popup.classList.remove('hidden');
        popup.classList.add('visible');
    });

    closePopupBtn1.addEventListener('click', () => {
        popup.classList.remove('visible');
        popup.classList.add('hidden');
    });


    // Optional: Close the popup if user clicks outside of it
    window.addEventListener('click', (event) => {
        if (event.target === popup) {
            popup.classList.remove('visible');
            popup.classList.add('hidden');
        }
    });
});
