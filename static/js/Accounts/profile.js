(function () {
    const tabs = document.querySelectorAll('#settings-tabs a');
    const panels = { account: 'tab-account', security: 'tab-security'};

    tabs.forEach(tab => {
        tab.addEventListener('click', function (e) {
            e.preventDefault();
            tabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
            const target = this.dataset.tab;
            Object.values(panels).forEach(id => document.getElementById(id).classList.remove('active'));
            document.getElementById(panels[target]).classList.add('active');
        });
    });

    const openForm = "{{ open_form|default:'' }}";
    if (openForm === 'password') {
        document.querySelector('[data-tab="security"]').click();
    }

    const avatarInput = document.getElementById('avatar-input');
    const avatarImg = document.getElementById('profile-avatar');

    if (avatarInput) {
        avatarInput.addEventListener('change', function (e) {
            const file = e.target.files[0];
            if (!file) return;
            const formData = new FormData();
            formData.append('avatar', file);
            fetch('/Accounts/profile/avatar/', {
                method: 'POST',
                headers: { 'X-CSRFToken': getCSRFToken() },
                body: formData
            })
            .then(r => r.json())
            .then(data => { if (data.url) avatarImg.src = data.url; });
        });
    }

    const passwordForm = document.getElementById('password-form');
    if (passwordForm) {
        passwordForm.addEventListener('submit', function (e) {
            const newPass = document.getElementById('new-password').value.trim();
            const confirmPass = document.getElementById('confirm-pass').value.trim();
            const errDiv = document.getElementById('pass-error');

            errDiv.classList.add('d-none');
            errDiv.innerText = '';

            if (newPass !== confirmPass) {
                errDiv.innerText = 'Passwords do not match';
                errDiv.classList.remove('d-none');
                e.preventDefault();
                return;
            }
            if (newPass.length < 6) {
                errDiv.innerText = 'Password must be at least 6 characters';
                errDiv.classList.remove('d-none');
                e.preventDefault();
            }
        });
    }

    function getCSRFToken() {
        const cookies = document.cookie.split(';');
        for (let c of cookies) {
            c = c.trim();
            if (c.startsWith('csrftoken=')) return decodeURIComponent(c.substring(10));
        }
        return null;
    }
})();
