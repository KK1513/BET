// 使用 localStorage 模擬用戶數據存儲
let currentUser = null;

// 顯示登入模態框
function showLogin() {
    if (!document.getElementById('loginModal')) {
        createModals();
    }
    const loginModal = new bootstrap.Modal(document.getElementById('loginModal'));
    loginModal.show();
}

// 顯示註冊模態框
function showRegister() {
    if (!document.getElementById('registerModal')) {
        createModals();
    }
    const registerModal = new bootstrap.Modal(document.getElementById('registerModal'));
    registerModal.show();
}

// 顯示充值模態框
function showDeposit() {
    if (!document.getElementById('depositModal')) {
        createModals();
    }
    const depositModal = new bootstrap.Modal(document.getElementById('depositModal'));
    depositModal.show();
}

// 顯示提款模態框
function showWithdraw() {
    if (!document.getElementById('withdrawModal')) {
        createModals();
    }
    const withdrawModal = new bootstrap.Modal(document.getElementById('withdrawModal'));
    withdrawModal.show();
}

// 更新 UI
function updateUI() {
    const authButtons = document.getElementById('authButtons');
    const userMenu = document.getElementById('userMenu');
    const balanceSection = document.getElementById('balanceSection');
    
    if (authButtons && userMenu && balanceSection) {
        if (currentUser) {
            authButtons.style.display = 'none';
            userMenu.style.display = 'block';
            balanceSection.style.display = 'block';
            const usernameEl = document.getElementById('username');
            const balanceEl = document.getElementById('userBalance');
            if (usernameEl) usernameEl.textContent = currentUser.username;
            if (balanceEl) balanceEl.textContent = currentUser.balance.toLocaleString();
        } else {
            authButtons.style.display = 'block';
            userMenu.style.display = 'none';
            balanceSection.style.display = 'none';
        }
    }
}

// 登出功能
function logout() {
    currentUser = null;
    localStorage.removeItem('currentUser');
    alert('已成功登出');
    updateUI();
}

// 創建模態框
function createModals() {
    const modalsHTML = `
        <!-- Login Modal -->
        <div class="modal fade" id="loginModal" tabindex="-1">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title"><i class="fas fa-sign-in-alt me-2"></i>會員登入</h5>
                        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <form id="loginForm">
                            <div class="mb-3">
                                <label class="form-label">帳號</label>
                                <input type="text" class="form-control" id="loginUsername" placeholder="請輸入帳號" required>
                            </div>
                            <div class="mb-3">
                                <label class="form-label">密碼</label>
                                <input type="password" class="form-control" id="loginPassword" placeholder="請輸入密碼" required>
                            </div>
                            <button type="submit" class="btn btn-register w-100 py-2">登入</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <!-- Register Modal -->
        <div class="modal fade" id="registerModal" tabindex="-1">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title"><i class="fas fa-user-plus me-2"></i>會員註冊</h5>
                        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <form id="registerForm">
                            <div class="mb-3">
                                <label class="form-label">帳號</label>
                                <input type="text" class="form-control" id="regUsername" placeholder="6-12位英文或數字" required>
                            </div>
                            <div class="mb-3">
                                <label class="form-label">密碼</label>
                                <input type="password" class="form-control" id="regPassword" placeholder="6-16位密碼" required>
                            </div>
                            <div class="mb-3">
                                <label class="form-label">確認密碼</label>
                                <input type="password" class="form-control" id="regConfirmPassword" placeholder="再次輸入密碼" required>
                            </div>
                            <div class="mb-3">
                                <label class="form-label">手機號碼</label>
                                <input type="tel" class="form-control" id="regPhone" placeholder="請輸入手機號碼" required>
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Email</label>
                                <input type="email" class="form-control" id="regEmail" placeholder="請輸入Email" required>
                            </div>
                            <button type="submit" class="btn btn-register w-100 py-2">立即註冊</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <!-- Deposit Modal -->
        <div class="modal fade" id="depositModal" tabindex="-1">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title"><i class="fas fa-plus-circle me-2"></i>充值</h5>
                        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <form id="depositForm">
                            <div class="mb-3">
                                <label class="form-label">充值金額</label>
                                <input type="number" class="form-control" id="depositAmount" placeholder="請輸入充值金額" min="100" required>
                            </div>
                            <div class="mb-3">
                                <label class="form-label">支付方式</label>
                                <select class="form-select" id="depositMethod" required>
                                    <option value="">請選擇支付方式</option>
                                    <option value="bank">銀行轉帳</option>
                                    <option value="alipay">支付寶</option>
                                    <option value="wechat">微信支付</option>
                                </select>
                            </div>
                            <button type="submit" class="btn btn-register w-100 py-2">確認充值</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <!-- Withdraw Modal -->
        <div class="modal fade" id="withdrawModal" tabindex="-1">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title"><i class="fas fa-minus-circle me-2"></i>提款</h5>
                        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <form id="withdrawForm">
                            <div class="mb-3">
                                <label class="form-label">提款金額</label>
                                <input type="number" class="form-control" id="withdrawAmount" placeholder="請輸入提款金額" min="100" required>
                            </div>
                            <div class="mb-3">
                                <label class="form-label">銀行帳號</label>
                                <input type="text" class="form-control" id="bankAccount" placeholder="請輸入銀行帳號" required>
                            </div>
                            <button type="submit" class="btn btn-register w-100 py-2">確認提款</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', modalsHTML);
    setupForms();
}

// 設置表單事件
function setupForms() {
    // 登入表單
    const loginForm = document.getElementById('loginForm');
    if (loginForm && !loginForm.dataset.setup) {
        loginForm.dataset.setup = 'true';
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const username = document.getElementById('loginUsername').value;
            const password = document.getElementById('loginPassword').value;
            const users = JSON.parse(localStorage.getItem('users') || '[]');
            const user = users.find(u => u.username === username && u.password === password);
            
            if (user) {
                currentUser = user;
                localStorage.setItem('currentUser', JSON.stringify(currentUser));
                alert('登入成功！');
                bootstrap.Modal.getInstance(document.getElementById('loginModal')).hide();
                loginForm.reset();
                updateUI();
            } else {
                alert('帳號或密碼錯誤');
            }
        });
    }

    // 註冊表單
    const registerForm = document.getElementById('registerForm');
    if (registerForm && !registerForm.dataset.setup) {
        registerForm.dataset.setup = 'true';
        registerForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const username = document.getElementById('regUsername').value;
            const password = document.getElementById('regPassword').value;
            const confirmPassword = document.getElementById('regConfirmPassword').value;
            const phone = document.getElementById('regPhone').value;
            const email = document.getElementById('regEmail').value;
            
            if (username.length < 6 || username.length > 12) {
                alert('帳號長度必須為 6-12 位');
                return;
            }
            if (password.length < 6 || password.length > 16) {
                alert('密碼長度必須為 6-16 位');
                return;
            }
            if (password !== confirmPassword) {
                alert('兩次輸入的密碼不一致');
                return;
            }
            if (!/^09\d{8}$/.test(phone)) {
                alert('請輸入有效的手機號碼（10位數字，以09開頭）');
                return;
            }
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                alert('請輸入有效的 Email 地址');
                return;
            }
            
            const existingUsers = JSON.parse(localStorage.getItem('users') || '[]');
            if (existingUsers.some(user => user.username === username)) {
                alert('該帳號已被註冊');
                return;
            }
            
            const newUser = {
                username: username,
                password: password,
                phone: phone,
                email: email,
                balance: 0,
                createdAt: new Date().toISOString()
            };
            
            existingUsers.push(newUser);
            localStorage.setItem('users', JSON.stringify(existingUsers));
            alert('註冊成功！');
            bootstrap.Modal.getInstance(document.getElementById('registerModal')).hide();
            registerForm.reset();
            currentUser = newUser;
            localStorage.setItem('currentUser', JSON.stringify(currentUser));
            updateUI();
        });
    }

    // 充值表單
    const depositForm = document.getElementById('depositForm');
    if (depositForm && !depositForm.dataset.setup) {
        depositForm.dataset.setup = 'true';
        depositForm.addEventListener('submit', function(e) {
            e.preventDefault();
            if (!currentUser) {
                alert('請先登入');
                return;
            }
            const amount = parseFloat(document.getElementById('depositAmount').value);
            if (amount < 100) {
                alert('最低充值金額為 100 元');
                return;
            }
            const users = JSON.parse(localStorage.getItem('users') || '[]');
            const userIndex = users.findIndex(u => u.username === currentUser.username);
            if (userIndex !== -1) {
                users[userIndex].balance += amount;
                localStorage.setItem('users', JSON.stringify(users));
                currentUser = users[userIndex];
                localStorage.setItem('currentUser', JSON.stringify(currentUser));
            }
            alert(`充值成功！已充值 ${amount} 元`);
            bootstrap.Modal.getInstance(document.getElementById('depositModal')).hide();
            depositForm.reset();
            updateUI();
        });
    }

    // 提款表單
    const withdrawForm = document.getElementById('withdrawForm');
    if (withdrawForm && !withdrawForm.dataset.setup) {
        withdrawForm.dataset.setup = 'true';
        withdrawForm.addEventListener('submit', function(e) {
            e.preventDefault();
            if (!currentUser) {
                alert('請先登入');
                return;
            }
            const amount = parseFloat(document.getElementById('withdrawAmount').value);
            if (amount < 100) {
                alert('最低提款金額為 100 元');
                return;
            }
            if (amount > currentUser.balance) {
                alert('餘額不足');
                return;
            }
            const users = JSON.parse(localStorage.getItem('users') || '[]');
            const userIndex = users.findIndex(u => u.username === currentUser.username);
            if (userIndex !== -1) {
                users[userIndex].balance -= amount;
                localStorage.setItem('users', JSON.stringify(users));
                currentUser = users[userIndex];
                localStorage.setItem('currentUser', JSON.stringify(currentUser));
            }
            alert(`提款申請已提交！提款金額：${amount} 元`);
            bootstrap.Modal.getInstance(document.getElementById('withdrawModal')).hide();
            withdrawForm.reset();
            updateUI();
        });
    }
}

// 頁面載入時初始化
window.addEventListener('DOMContentLoaded', function() {
    const savedUser = localStorage.getItem('currentUser');
    if (savedUser) {
        currentUser = JSON.parse(savedUser);
        const users = JSON.parse(localStorage.getItem('users') || '[]');
        const user = users.find(u => u.username === currentUser.username);
        if (user) {
            currentUser = user;
            localStorage.setItem('currentUser', JSON.stringify(currentUser));
        }
    }
    updateUI();
});


