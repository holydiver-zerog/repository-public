"use strict";

document.addEventListener('DOMContentLoaded', function () {
    const hobbyContent = document.getElementById('hobbyContent');
    const skillContent = document.getElementById('skillContent');
    const toggleHobbies = document.getElementById('toggleHobbies');

    // 初期状態は趣味を表示
    hobbyContent.style.display = 'block';
    skillContent.style.display = 'none';

    // ボタンのクリックイベント
    toggleHobbies.addEventListener('click', function () {
        if (hobbyContent.style.display === 'block') {
            hobbyContent.style.display = 'none';      // 趣味を非表示
            skillContent.style.display = 'block';     // 特技を表示
            toggleHobbies.textContent = '趣味を表示'; // ボタンのテキストを変更
        } else {
            hobbyContent.style.display = 'block';     // 趣味を表示
            skillContent.style.display = 'none';      // 特技を非表示
            toggleHobbies.textContent = '特技を表示'; // ボタンのテキストを変更
        }
    });
});