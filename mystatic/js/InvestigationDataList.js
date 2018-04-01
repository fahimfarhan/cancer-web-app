var fakeServerResponse = ['marker', 'CBC', 'RBS', 'LFT','KFT','Serum Electrolytes','Others'];
var datalist = document.getElementById('typeName');

document.getElementById('id_type').addEventListener('keyup', function () {
    if (this.value.length === 0) {
        return;
    }

    // Send Ajax request and loop of its result

    datalist.textContent = '';
    for (var i = 0; i < fakeServerResponse.length; i++) {
        if (fakeServerResponse[i].indexOf(this.value) !== 0) {
            continue;
        }
        var option = document.createElement('option');
        option.value = fakeServerResponse[i];
        datalist.appendChild(option);
    }
});