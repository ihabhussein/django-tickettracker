function change_state(object, state) {
    object = object.replace(/^.+-/, '');
    state = state.replace(/^.+-/, '');

    // TODO
    alert('TODO: Change ticket ' + object + ' to ' + state);
    return Promise.resolve(1);
};

document.querySelectorAll('.draggable').forEach(e => {
    e.addEventListener('dragstart',
        ev => ev.dataTransfer.setData("text", ev.target.id)
    );
});

document.querySelectorAll('.drop-target').forEach(e => {
    e.addEventListener('dragover',
        ev => ev.preventDefault()
    );

    e.addEventListener('drop', ev => {
        ev.preventDefault();
        var target = ev.target;
        while (target.className != 'drop-target') {
            target = target.parentNode;
        };
        var data = ev.dataTransfer.getData("text");
        var object = document.getElementById(data);
        change_state(data, target.id).then(
            () => target.appendChild(object)
        );
    });
});
