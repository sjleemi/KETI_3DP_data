function createMultiLineChart(canvasId, datasets) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: datasets[0].data.map((_, i) => i),
            datasets: datasets
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: '샘플 순서' } },
                y: { title: { display: true, text: '값' }, beginAtZero: true }
            }
        }
    });
}
