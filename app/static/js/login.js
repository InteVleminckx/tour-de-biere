document.addEventListener("DOMContentLoaded", async () => {
    const socket = io();

    const res = await fetch("/api/users");
    const users = await res.json();

    const table = document.createElement("table");
    table.className = "table-auto border border-collapse border-gray-300 mt-4";

    users.forEach(user => {
        const row = document.createElement("tr");
        row.className = "cursor-pointer hover:bg-gray-100";

        const cell = document.createElement("td");
        cell.textContent = user.user_name;
        cell.className = "p-2 border";

        row.appendChild(cell);
        table.appendChild(row);

        row.addEventListener("click", () => {
            socket.emit("select_user", {user_id: user.user_id});

            // Optional: Store locally for page reloads
            localStorage.setItem("user_id", user.user_id);
        });
    });

    document.body.appendChild(table);

    socket.on("user_selected", data => {
        console.log("✅ User session set on backend:", data);
        alert(`Logged in as ${data.user_name}`);
    });

    // Auto reselect user if previously stored
    const storedId = localStorage.getItem("user_id");
    if (storedId) {
        socket.emit("select_user", {user_id: parseInt(storedId)});
    }
});
