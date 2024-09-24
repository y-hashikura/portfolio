window.addEventListener('scroll', function() {
    const nav = document.querySelector('.nav-container');
    const profileSectionHeight = document.querySelector('.profile-section').offsetHeight;

    if (window.scrollY > profileSectionHeight) {
        nav.classList.add('fixed');
        document.body.style.paddingTop = nav.offsetHeight + 'px'; // メニュー分のパディングを追加
    } else {
        nav.classList.remove('fixed');
        document.body.style.paddingTop = '0';
    }
});