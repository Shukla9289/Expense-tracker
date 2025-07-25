async function fetchExpenses() {
    const res = await fetch('/api/expenses');
    const data = await res.json();
    const list = document.getElementById('expenseList');
    list.innerHTML = '';
    data.forEach(exp => {
        const li = document.createElement('li');
        li.innerHTML = `${exp.name} - ₹${exp.amount} (${exp.category}) 
            <button onclick="deleteExpense('${exp._id}')">Delete</button>`;
        list.appendChild(li);
    });
}

async function addExpense() {
    const name = document.getElementById('name').value;
    const amount = document.getElementById('amount').value;
    const category = document.getElementById('category').value;

    await fetch('/api/expenses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, amount, category })
    });

    fetchExpenses();
}

async function deleteExpense(id) {
    await fetch(`/api/expenses/${id}`, { method: 'DELETE' });
    fetchExpenses();
}

window.onload = fetchExpenses;