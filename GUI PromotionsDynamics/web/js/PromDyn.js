document.getElementById("get_CalcProfit").onclick = async function calculateProfit() {
	let actual = document.getElementById("prom_info");
	let user = document.getElementById("userNum").value;
	let quantity = document.getElementById("userQuantity").value;
	let total = (actual.innerHTML - user) * quantity

	document.getElementById("totalProfit").innerHTML = total + " $";
};

document.getElementById("get_Dividends").onclick = async function Dividends() {
	let promotions = document.getElementById("prom_info").innerHTML;
	let quantity = document.getElementById("a_1").value;
	let dividends = document.getElementById("a_2").value;

	let total = (promotions * dividends * quantity) / 100

	document.getElementById("totalDividends").innerHTML = total + " $";
};


let textLoad = ' Loading... '

document.getElementById("get_AMD").onclick = async function display_AMD() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_AMD()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_Intel").onclick = async function display_Intel() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_Intel()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_Apple").onclick = async function display_Apple() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_Apple()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_IBM").onclick = async function display_IBM() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_IBM()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_Microsoft").onclick = async function display_Microsoft() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_Microsoft()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_Google").onclick = async function display_Google() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_Google()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_Facebook").onclick = async function display_Facebook() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_Facebook()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_EA").onclick = async function display_EA() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_EA()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_Yandex").onclick = async function display_Yandex() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_Yandex()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_Huawei").onclick = async function display_Huawei() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_Huawei()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_Tesla").onclick = async function display_Tesla() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_Tesla()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_Nissan").onclick = async function display_Ford() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_Nissan()();
    document.getElementById("prom_info").innerHTML = output;

};

document.getElementById("get_Ford").onclick = async function display_Ford() {

    document.getElementById("prom_info").innerHTML = textLoad;

    let output = await eel.check_Ford()();
    document.getElementById("prom_info").innerHTML = output;

};


// Pandas
document.getElementById("getPandas_IT").onclick = async function display_IT() {

    document.getElementById("pandas-out").innerHTML = textLoad + ' Please, wait' ;

    await eel.start_Pandas_IT()();

    document.getElementById("pandas-out").innerHTML = 'Has done!';



};

document.getElementById("getPandas_Auto").onclick = async function display_Auto() {

    document.getElementById("pandas-out").innerHTML = textLoad + ' Please, wait' ;

    let output = await eel.start_Pandas_Auto()();
    document.getElementById("pandas-out").innerHTML = 'Has done!';

};
