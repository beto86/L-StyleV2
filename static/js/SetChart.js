//setting up all chart config

//---index
var metricsChart = document.getElementById('metricsChart').getContext('2d');

new Chart(metricsChart, {
    type: 'bar',
    data: {
        labels: ['EC', 'OR', 'CA', 'EA'],
        datasets: [{
            label: 'Tipos de aprendizado',
            data: [3, 4, 35, 70, 80],
            backgroundColor: [
                'rgba(98, 211, 219, 0.5)',
                'rgba(92, 87, 175, 0.5)',
                'rgba(229, 75, 75, 0.5)',
                'rgba(254, 204, 0, 0.5)'
                
            ],
            borderColor: [
                'rgba(98, 211, 219, 0.5)',
                'rgba(92, 87, 175, 0.5)',
                'rgba(229, 75, 75, 0.5)',
                'rgba(254, 204, 0, 0.5)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});