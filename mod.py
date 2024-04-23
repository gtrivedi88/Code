.alias-table {
    display: block;
    width: 100%;
    max-width: 100%;
    overflow-x: auto;
    border-collapse: collapse;
    white-space: nowrap;
}

.alias-table-header,
.alias-table-row {
    display: table;
    width: 100%;
    table-layout: fixed;
}

.alias-table-cell {
    display: table-cell;
    padding: 8px;
    border: 1px solid #ddd;
    text-align: left;
}

.alias-table-header .alias-table-cell,
.alias-table-row .alias-table-cell:first-child {
    font-weight: bold;
    background-color: #f2f2f2;
}

.alias-table-row:nth-child(odd) {
    background-color: #f9f9f9;
}

.alias-table-row:hover {
    background-color: #eaeaea;
}

.parent-columns,
.notes-columns {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
