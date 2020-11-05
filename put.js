
function send_checkin() {
    
    let Date = document.getElementById('Date').value;
    let Squad = document.querySelector('input[name="Squad"]:checked').value;
    let Feeling = document.querySelector('input[name="Feeling"]:checked').value;
    let Why_Feeling = document.getElementById('Why_Feeling').value;
    let Did = document.getElementById('Did').value;
    let Learned = document.getElementById('Learned').value;
    let Todo = document.getElementById('Todo').value;
    let Question = document.getElementById('Question').value;


    let data = {'Date': Date, 'Squad': Squad, 'Feeling': Feeling, 'Why_Feeling': Why_Feeling, 'Did': Did, 'Learned': Learned, 'Todo': Todo, 'Question': Question};
    
    var id = document.getElementById('Checkin_id').value

    fetch(`http://127.0.0.1:5000/api/checkins/${id}`, {
            method: 'PUT',
            headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then((response) => {
            return response.json();
        })
        .then((result) => {
            alert(result['succes']);
        });

}