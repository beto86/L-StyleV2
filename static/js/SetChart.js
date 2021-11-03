//setting up all chart config

//---index
var metricsChart = document.getElementById('metricsChart').getContext('2d');
var metricsChartBar = document.getElementById('metricsChartBar').getContext('2d');

new Chart(metricsChart, {
    type: 'radar',
    data: {
        labels: ['EC', 'OR', 'CA', 'EA'],
        datasets: [
           {
            label: 'Assimilador',
            data: [30, 36, 30, 24],
            backgroundColor:
                'rgba(241, 194, 0, 0.2)',
            borderColor:
                'rgb(241, 194, 0)',
            borderWidth: 2
        }]
    },
    options: config = {
        scale: {
            ticks: {
                //beginAtZero: true,
                min: 0,
                stepSize: 5,
                // max: 100,
            },
        }
    }
});

new Chart(metricsChartBar, {
    type: 'bar',
    data: {
        labels: ['EC', 'OR', 'CA', 'EA'],
        datasets: [
           {
            label: 'Assimilador',
            data: [30, 36, 30, 24],
            backgroundColor:
                ['rgba(98,211,219,0.5)',
                 'rgba(229,75,75,0.5)',
                 'rgba(92, 87, 175, 0.5)',
                 'rgba(255,204,68,0.5)'],

            borderColor:
                ['rgba(98,211,219,1)',
                 'rgba(229,75,75,1)',
                 'rgba(92, 87, 175, 1)',
                 'rgba(255,204,68,1)'],
            borderWidth: 2
        }]
    },
    options: {
        scales: {
            yAxes: [{
                stacked:true,
                gridLines: {
                    display: false
                }
            }]
        }
    }
});