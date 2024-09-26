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

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.clickable-row').forEach(function(row) {
        // ダブルクリックイベントを設定
        row.addEventListener('dblclick', function() {
            const target = this.dataset.bsTarget;
            const collapseElement = document.querySelector(target);

            // トグル機能: 開閉状態の確認
            if (collapseElement.classList.contains('show')) {
                collapseElement.classList.remove('show');  // 開いているなら閉じる
            } else {
                document.querySelectorAll('.collapse').forEach(function(el) {
                    el.classList.remove('show');  // 他の詳細は閉じる
                });
                collapseElement.classList.add('show');  // 対象の詳細を開く
            }
        });
    });
});