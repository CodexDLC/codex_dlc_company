(function () {
    var cfg       = document.getElementById('theme-css');
    var DARK_CSS  = cfg ? cfg.dataset.dark  : '';
    var LIGHT_CSS = cfg ? cfg.dataset.light : '';
    var themeBtn  = document.getElementById('theme-btn');

    function getTheme() {
        return document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
    }

    function applyTheme(theme) {
        if (theme === 'light') {
            document.documentElement.setAttribute('data-theme', 'light');
            if (cfg) cfg.href = LIGHT_CSS;
            if (themeBtn) themeBtn.textContent = '[ D ]';
        } else {
            document.documentElement.removeAttribute('data-theme');
            if (cfg) cfg.href = DARK_CSS;
            if (themeBtn) themeBtn.textContent = '[ L ]';
        }
        localStorage.setItem('codex-theme', theme);
    }

    window.toggleTheme = function () {
        applyTheme(getTheme() === 'dark' ? 'light' : 'dark');
    };

    // Init button label on load
    var current = getTheme();
    if (themeBtn) themeBtn.textContent = current === 'light' ? '[ D ]' : '[ L ]';
    if (current === 'light' && cfg) cfg.href = LIGHT_CSS;
})();
