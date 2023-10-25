let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7] },
        {searchable:false,targets: [0,] }

    ],
    pageLength: 15,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await initProgrammers();

    dataTable = $("#datatable-programmers").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};
const initProgrammers = async () => {
    try {
        const response = await fetch(listPrograUrl);
        const data = await response.json();

        let content = ``;
        data.programmers.forEach((programmer, index) => {
            content += `
                <tr>
                    <td>${index+1}</td>
                    <td>${programmer.titulo}</td>
                    <td>${programmer.fecha}</td>
                    <td>${programmer.sheij}</td>
                    <td>${programmer.novio}</td>
                    <td>${programmer.novia}</td>
                    <td>${programmer.guardian}</td>
                    <td>${programmer.testigos}</td>                 
                </tr>`;
        });
        document.getElementById("tableBody_programmers").innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};
window.addEventListener("load", async () => {
    await initDataTable();
});