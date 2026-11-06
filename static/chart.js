const placed = 39;
const notPlaced = 61;

// Pie Chart
new Chart(document.getElementById("pieChart"), {
    type: "pie",
    data: {
        labels: ["Placed", "Not Placed"],
        datasets: [{
            data: [placed, notPlaced],
            backgroundColor: [
                "#4CAF50",
                "#F44336"
            ]
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

// Bar Chart
new Chart(document.getElementById("barChart"), {
    type: "bar",
    data: {
        labels: ["Students", "Placed", "Not Placed"],
        datasets: [{
            label: "Statistics",
            data: [100, placed, notPlaced],
            backgroundColor: [
                "#2196F3",
                "#4CAF50",
                "#F44336"
            ]
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: false
            }
        }
    }
});