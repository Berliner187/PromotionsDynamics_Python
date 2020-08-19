document.getElementById("get_CalcProfit").onclick = async function calculateProfit() {
	let actual = document.getElementById("prom_info");
	let user = document.getElementById("userNum").value;
	let quantity = document.getElementById("userQuantity").value;
	let total = ((actual.innerHTML) - user) * quantity

	document.getElementById("totalProfit").innerHTML = total + " $";
};

document.getElementById("get_Dividends").onclick = async function Dividends() {
	let promotions = document.getElementById("a_0").value;
	let quantity = document.getElementById("a_1").value;
	let dividends = document.getElementById("a_2").value;

	let total = (promotions * dividends) * (dividends / 100)

	document.getElementById("totalDividends").innerHTML = total + " $";
};



document.getElementById("get_AMD").onclick = async function display_AMD() {

    let output = await eel.check_AMD()();
    document.getElementById("prom_info").innerHTML = output;


};

document.getElementById("get_Intel").onclick = async function display_Intel() {

    let output = await eel.check_Intel()();
    document.getElementById("prom_info").innerHTML = output;


};

document.getElementById("get_Apple").onclick = async function display_Apple() {

    let output = await eel.check_Apple()();
    document.getElementById("prom_info").innerHTML = output;


};

document.getElementById("get_IBM").onclick = async function display_IBM() {

    let output = await eel.check_IBM()();
    document.getElementById("prom_info").innerHTML = output;


};

document.getElementById("get_Microsoft").onclick = async function display_Microsoft() {

    let output = await eel.check_Microsoft()();
    document.getElementById("prom_info").innerHTML = output;


};

document.getElementById("get_Google").onclick = async function display_Google() {

    let output = await eel.check_Google()();
    document.getElementById("prom_info").innerHTML = output;


};

document.getElementById("get_Facebook").onclick = async function display_Facebook() {

    let output = await eel.check_Facebook()();
    document.getElementById("prom_info").innerHTML = output;


};

document.getElementById("get_EA").onclick = async function display_EA() {

    let output = await eel.check_EA()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_Yandex").onclick = async function display_Yandex() {

    let output = await eel.check_Yandex()();
    document.getElementById("prom_info").innerHTML = output;


};

document.getElementById("get_Huawei").onclick = async function display_Huawei() {

    let output = await eel.check_Huawei()();
    document.getElementById("prom_info").innerHTML = output;


};