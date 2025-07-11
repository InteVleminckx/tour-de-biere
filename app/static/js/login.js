const socket = io();

document.addEventListener("DOMContentLoaded", async () => {

    const res = await fetch("/api/users");
    const users = await res.json();

    const table = document.createElement("table");

    users.forEach(user => {
        const row = document.createElement("tr");

        const cell = document.createElement("td");
        cell.textContent = user.username;

        row.appendChild(cell);
        table.appendChild(row);

        row.addEventListener("click", () => {
            socket.emit("user_select", {user_id: user.user_id, username: user.username});
        });
    });

    document.body.appendChild(table);
});

socket.on('user_added', (data) => {
    const username = data.username;
    // Todo: send user to its overview page
})