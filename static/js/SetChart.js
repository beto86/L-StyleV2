//setting up all chart config

//---index
var metricsChart = document.getElementById('metricsChart').getContext('2d');

new Chart(metricsChart, {
    type: 'radar',
    data: {
        labels: ['EC', 'OR', 'CA', 'EA'],
        datasets: [
           {
            label: 'Assimilador',
            data: [30, 36, 30, 24],
            backgroundColor:
                'rgba(92, 87, 175, 0.5)',

            borderColor:
                'rgba(92, 87, 175, 0.5)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            r: {

            }
        }
    }
});