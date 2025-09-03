function erf(x) {
    var z;
    const ERF_A = 0.147;
    var the_sign_of_x;
    if (0 == x) {
        the_sign_of_x = 0;
        return 0;
    } else if (x > 0) {
        the_sign_of_x = 1;
    } else {
        the_sign_of_x = -1;
    }

    var one_plus_axsqrd = 1 + ERF_A * x * x;
    var four_ovr_pi_etc = 4 / Math.PI + ERF_A * x * x;
    var ratio = four_ovr_pi_etc / one_plus_axsqrd;
    ratio *= x * -x;
    var expofun = Math.exp(ratio);
    var radical = Math.sqrt(1 - expofun);
    z = radical * the_sign_of_x;
    return z;
}

function updateOutput() {
    //get form
    var form = document.getElementById("calc1");
    //get form
    var form = document.getElementById("calc");
    //get output
    var out = form.elements["z"];
    //get two numbers
    var num2 = parseInt(form.elements["y"].value);
    var num3 = parseInt(form.elements["y1"].value);
    //get operator
    var operator = parseInt(form.elements["op"].value);
    //set output depending on operator
    switch (operator) {
        // value="0"   Aluminum 1100 (UNS A91100)
        case 0:
            var a = +23.39172
            var b = -148.5733
            var c = +422.1917
            var d = -653.6664
            var e = +607.0402
            var f = -346.152
            var g = +118.4276
            var h = -22.2781
            var i = +1.770187
            //num1 = 23.39172-148.5733*Math.log10(num2)+422.1917*Math.pow(Math.log10(num2),2)-653.6664*Math.pow(Math.log10(num2),3)+607.0402*Math.pow(Math.log10(num2),4)-346.152*Math.pow(Math.log10(num2),5)+118.4276*Math.pow(Math.log10(num2),6)-22.2781*Math.pow(Math.log10(num2),7)+1.770187*Math.pow(Math.log10(num2),8);
            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="1"   Aluminum 3003-F(UNS A93003) TC
        case 1:
            var a = +0.63736
            var b = -1.1437
            var c = +7.4624
            var d = -12.6905
            var e = +11.9165
            var f = -6.18721
            var g = +1.63939
            var h = -0.172667
            var i = +0
            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="101"   Aluminum 3003-F(UNS A93003) SH
        case 101:
            var a = 46.6467
            var b = -314.292
            var c = 866.662
            var d = -1298.3
            var e = 1162.27
            var f = -637.795
            var g = 210.351
            var h = -38.3094
            var i = 2.96344

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="102"   Aluminum 3003-F(UNS A93003)   - LE (10^-5 m/m) -  Equation Range: 4  to 300 K
        case 102:
            var a = -4.1277 * 100 //Math.exp(2)
            var b = -3.0389 / 10 //Math.exp(-1)
            var c = 8.7696 / 1000 //Math.exp(-3)
            var d = -9.9821 / 1000000 //Math.exp(-6)
            var e = 0

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;


            // value="2"   Aluminum 5083-O (UNS A95083)
        case 2:

            var a = -0.90933
            var b = 5.751
            var c = -11.112
            var d = 13.612
            var e = -9.3977
            var f = 3.6873
            var g = -0.77295
            var h = 0.067336
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="201"   Aluminum 5083-O (UNS A95083)  - SH (J/kg-K) -  Equation Range: 4  to 300 K	
        case 201:

            var a = 46.6467
            var b = -314.292
            var c = 866.662
            var d = -1298.3
            var e = 1162.27
            var f = -637.795
            var g = 210.351
            var h = -38.3094
            var i = 2.96344

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="202"   Aluminum 5083-O (UNS A95083)  - YM (GPa) -   Equation Range: 0  to 300 K	
        case 202:

            var a = 8.083212 * 10 //Math.exp(1)
            var b = 1.061708 / 100 //Math.exp(-2)
            var c = -3.016100 / 10000 //Math.exp(-4)
            var d = 7.561340 / 10000000 ///10000000 //*Math.exp(-7)
            var e = -6.994800 / 10000000000 ///10000000000 //*Math.exp(-10)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="203"   Aluminum 5083-O (UNS A95083)  - LE (10^-5 m/m) - Equation Range: 4  to 300 K
        case 203:

            var a = -4.1277 * 100 //Math.exp(2)
            var b = -3.0389 / 10 ///10 //*Math.exp(-1)
            var c = 8.7696 / 1000 ///1000 //*Math.exp(-3)
            var d = -9.9821 / 1000000 ///1000000 //*Math.exp(-6)
            var e = 0

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;


            // value="3"   Aluminum 6061-T6 (UNS A96061) - TC (W/m-K) - Range 4  to 300 K
        case 3:

            var a = 0.07918
            var b = 1.0957
            var c = -0.07277
            var d = 0.08084
            var e = 0.02803
            var f = -0.09464
            var g = 0.04179
            var h = -0.00571
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);

            break;

            // value="301"   Aluminum 6061-T6 (UNS A96061) - SH (J/kg-K) -  Range 4  to 300 K	
        case 301:

            var a = 46.6467
            var b = -314.292
            var c = 866.662
            var d = -1298.3
            var e = 1162.27
            var f = -637.795
            var g = 210.351
            var h = -38.3094
            var i = 2.96344

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="302"   Aluminum 6061-T6 (UNS A96061) - YM (GPa) -   Range 0  to 299 K
        case 302:

            var a = 7.771221 * 10 //Math.exp(1)
            var b = 1.030646 / 100 ///100 //*Math.exp(-2)
            var c = -2.924100 / 10000 ///10000 //*Math.exp(-4)
            var d = 8.993600 / 10000000 ///10000000 //*Math.exp(-7)
            var e = -1.070900 / 1000000000 ///1000000000 //*Math.exp(-9)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="303"   Aluminum 6061-T6 (UNS A96061) - LE (10^-5 m/m) -  Range 4  to 300 K
        case 303:

            var a = -4.1277 * 100 //Math.exp(2)
            var b = -3.0389 / 10 ///10 //*Math.exp(-1)
            var c = 8.7696 / 1000 ///1000 //*Math.exp(-3)
            var d = -9.9821 / 1000000 ///1000000 //*Math.exp(-6)
            var e = 0

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;


            // value="4"   Aluminum 6063-T5 (UNS A96063) - TC (W/m-K) - Range 4  to 295 K

        case 4:

            var a = 22.401433
            var b = -141.13433
            var c = 394.95461
            var d = -601.15377
            var e = 547.83202
            var f = -305.99691
            var g = 102.38656
            var h = -18.810237
            var i = 1.4576882

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;
            // value="5"   Apiezon N       - SH (J/kg-K) -  Equation Range: 1  to 200 K	

        case 5:

            var a = -1.61975
            var b = 3.10923
            var c = -0.712719
            var d = 4.93675
            var e = -9.37993
            var f = 7.58304
            var g = -3.11048
            var h = 0.628309
            var i = -0.0482634

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;
            // value="6"   Balsa         - TC (W/m-K) - Range 70 to 300 K den(6ft/lb3)

        case 6:

            var a = 4172.447
            var b = -11309.97
            var c = 12745.09
            var d = -7647.584
            var e = 2577.309
            var f = -462.538
            var g = 34.5351
            var h = 0
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;
            // value="601"   Balsa         - TC (W/m-K) - Range 70 to 300 K den(11ft/lb3)

        case 601:

            var a = 4815.4
            var b = -12969.63
            var c = 14520.76
            var d = -8654.164
            var e = 2895.712
            var f = -515.7272
            var g = 38.19218
            var h = 0
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;


            // value="7"   Beechwood-Phenolic

        case 7:

            var a = -1375.11
            var b = 3740.69
            var c = -4238.465
            var d = 2559.333
            var e = -868.6067
            var f = 157.1018
            var g = -11.82957
            var h = 0
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="7"   Beechwood/phenolic      - TC (W/m-K) - Range 92 to 300 K grain direction
        case 7:
            var a = -1375.11
            var b = 3740.69
            var c = -4238.465
            var d = 2559.333
            var e = -868.6067
            var f = 157.1018
            var g = -11.82957
            var h = 0
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="701"   Beechwood/phenolic    - TC (W/m-K) - Range 92 to 300 K flatwise	
        case 701:

            var a = 1035.33
            var b = -2191.85
            var c = 1470.505
            var d = 39.845
            var e = -541.9035
            var f = 289.844
            var g = -65.2253
            var h = 5.59956
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="702"   Beechwood/phenolic    - LE (10^-5 m/m) -   Equation Range: 77 to 293 K unidirectional flatwise
        case 702:
            var a = -683.9
            var b = 2.18264
            var c = 0.001701
            var d = -7.1 / 1000000 ///1000000 //*Math.exp(-6)
            var e = 1.04 / 100000000 ///100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="703"   Beechwood/phenolic    - LE (10^-5 m/m) -   Equation Range: 77 to 293 K unidirectional grain
        case 703:
            var a = -189.138
            var b = 0.646759
            var c = 0.000202
            var d = -1.2 / 1000000 //*Math.exp(-6)
            var e = 1.85 / 1000000000 //*Math.exp(-9)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="704"   Beechwood/phenolic    - LE (10^-5 m/m) -   Equation Range: 77 to 293 K cross laminate grain	
        case 704:
            var a = -944.081
            var b = 2.909782
            var c = 0.002971
            var d = -1e-5
            var e = 1.23e-8

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="8"   Beryllium         - SH (J/kg-K) -  Equation Range: 10  to 284 K	

        case 8:

            var a = -526.84477
            var b = 2755.4105
            var c = -6209.8985
            var d = 7859.2257
            var e = -6106.2095
            var f = 2982.9958
            var g = -894.99967
            var h = 150.85256
            var i = -10.943615

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="801"   Beryllium         - LE (10^-5 m/m) -   Equation Range: 75  to 500 K (//a axis)
        case 801:
            var a = -134.17300
            var b = -4.4051 / 10 //*Math.exp(-1)
            var c = 3.4063 / 1000 //*Math.exp(-3)
            var d = -6.5593 / 10000000 //*Math.exp(-7)
            var e = -1.8112 / 1000000000 //*Math.exp(-9)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="802"   Beryllium         - LE (10^-5 m/m) -   Equation Range: 75  to 500 K (//c axis)	
        case 802:
            var a = -86.08100
            var b = -2.6372 / 10 //*Math.exp(-1)
            var c = 1.3623 / 1000 //*Math.exp(-3)
            var d = 3.2709 / 1000000 //*Math.exp(-6)
            var e = -4.8719 / 1000000000 //*Math.exp(-9)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="803"   Beryllium         - LE (10^-5 m/m) -   Equation Range: 75  to 500 K (Polycrystalline)		
        case 803:
            var a = -120.29800
            var b = -3.4687 / 10 //*Math.exp(-1)
            var c = 2.5691 / 1000 //*Math.exp(-3)
            var d = 8.9848 / 10000000 //*Math.exp(-7)
            var e = -2.9422 / 1000000000 //*Math.exp(-9)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="9"   Beryllium Copper      - TC (W/m-K) - Equation Range: 2 to 80 K 

        case 9:

            var a = -0.50015
            var b = 1.9319
            var c = -1.6954
            var d = 0.71218
            var e = 1.2788
            var f = -1.6145
            var g = 0.68722
            var h = -0.10501
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="901"   Beryllium Copper      - LE (10^-5 m/m) - Equation Range: 24 to 300 K 	
        case 901:
            var a = -3.1150 * 100 //*Math.exp(2)
            var b = -4.4498 / 10 //*Math.exp(-1)
            var c = 1.0133 / 100 //*Math.exp(-2)
            var d = -2.4718 / 100000 //*Math.exp(-5)
            var e = 2.6277 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;


            // value="10"   Brass (UNS C2600)      - TC (W/m-K) - Equation Range: 5 to 116 K 

        case 10:

            var a = 0.021035
            var b = -1.01835
            var c = 4.54083
            var d = -5.03374
            var e = 3.20536
            var f = -1.12933
            var g = 0.174057
            var h = -0.0038151
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="11"   Copper (OFHC) (UNS C10100/ C10200) - TC (W/m-K) - Equation Range: 4 to 300 K (RRR=50)	

        case 11:

            var a = 1.8743
            var b = -0.41538
            var c = -0.6018
            var d = 0.13294
            var e = 0.26426
            var f = -0.0219
            var g = -0.051276
            var h = 0.0014871
            var i = 0.003723

            num1 = (a + c * Math.pow(num2, 0.5) + e * num2 + g * Math.pow(num2, 1.5) + i * Math.pow(num2,
                2)) / (1 + b * Math.pow(num2, 0.5) + d * num2 + f * Math.pow(num2, 1.5) + h * Math.pow(num2,
                2));
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="111"   Copper (OFHC) (UNS C10100/ C10200) - TC (W/m-K) - Equation Range: 4 to 300 K (RRR=100)	

        case 111:

            var a = 2.2154
            var b = -0.47461
            var c = -0.88068
            var d = 0.13871
            var e = 0.29505
            var f = -0.02043
            var g = -0.04831
            var h = 0.001281
            var i = 0.003207

            num1 = (a + c * Math.pow(num2, 0.5) + e * num2 + g * Math.pow(num2, 1.5) + i * Math.pow(num2,
                2)) / (1 + b * Math.pow(num2, 0.5) + d * num2 + f * Math.pow(num2, 1.5) + h * Math.pow(num2,
                2));
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="112"   Copper (OFHC) (UNS C10100/ C10200) - TC (W/m-K) - Equation Range: 4 to 300 K (RRR=150)	

        case 112:

            var a = 2.3797
            var b = -0.4918
            var c = -0.98615
            var d = 0.13942
            var e = 0.30475
            var f = -0.019713
            var g = -0.046897
            var h = 0.0011969
            var i = 0.0029988

            num1 = (a + c * Math.pow(num2, 0.5) + e * num2 + g * Math.pow(num2, 1.5) + i * Math.pow(num2,
                2)) / (1 + b * Math.pow(num2, 0.5) + d * num2 + f * Math.pow(num2, 1.5) + h * Math.pow(num2,
                2));
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="113"   Copper (OFHC) (UNS C10100/ C10200) - TC (W/m-K) - Equation Range: 4 to 300 K (RRR=300)	

        case 113:

            var a = 1.357
            var b = 0.3981
            var c = 2.669
            var d = -0.1346
            var e = -0.6683
            var f = 0.01342
            var g = 0.05773
            var h = 0.0002147
            var i = 0

            num1 = (a + c * Math.pow(num2, 0.5) + e * num2 + g * Math.pow(num2, 1.5) + i * Math.pow(num2,
                2)) / (1 + b * Math.pow(num2, 0.5) + d * num2 + f * Math.pow(num2, 1.5) + h * Math.pow(num2,
                2));
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="114"   Copper (OFHC) (UNS C10100/ C10200) - TC (W/m-K) - Equation Range: 4 to 300 K (RRR=500)	

        case 114:

            var a = 2.8075
            var b = -0.54074
            var c = -1.2777
            var d = 0.15362
            var e = 0.36444
            var f = -0.02105
            var g = -0.051727
            var h = 0.0012226
            var i = 0.0030964

            num1 = (a + c * Math.pow(num2, 0.5) + e * num2 + g * Math.pow(num2, 1.5) + i * Math.pow(num2,
                2)) / (1 + b * Math.pow(num2, 0.5) + d * num2 + f * Math.pow(num2, 1.5) + h * Math.pow(num2,
                2));
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="115"   Copper (OFHC) (UNS C10100/ C10200) - SH (J/kg-K) -   Equation Range: 4 to 300 K

        case 115:

            var a = -1.91844
            var b = -0.15973
            var c = 8.61013
            var d = -18.996
            var e = 21.9661
            var f = -12.7328
            var g = 3.54322
            var h = -0.3797
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="116"   Copper (OFHC) (UNS C10100/ C10200) - EC (10^-6/K) - Equation Range: 4 to 300 K

        case 116:

            var a = -17.9081289
            var b = 67.131914
            var c = -118.809316
            var d = 109.9845997
            var e = -53.8696089
            var f = 13.30247491
            var g = -1.30843441
            var h = 0
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="12"   Fiberglass Epoxy G-10 - TC (W/m-K) - Equation Range: 4 to 300 K (Normal Direction)	

        case 12:

            var a = -4.1236
            var b = 13.788
            var c = -26.068
            var d = 26.272
            var e = -14.663
            var f = 4.4954
            var g = -0.6905
            var h = 0.0397
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="121"   Fiberglass Epoxy G-10 - TC (W/m-K) - Equation Range: 4 to 300 K (Wrap Direction)	

        case 121:

            var a = -2.64827
            var b = 8.80228
            var c = -24.8998
            var d = 41.1625
            var e = -39.8754
            var f = 23.1778
            var g = -7.95635
            var h = 1.48806
            var i = -0.11701

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="122"   Fiberglass Epoxy G-10 - SH (J/kg-K) -  Equation Range: 4 to 300 K 	

        case 122:

            var a = -2.4083
            var b = 7.6006
            var c = -8.2982
            var d = 7.3301
            var e = -4.2386
            var f = 1.4294
            var g = -0.24396
            var h = 0.015236
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="123"   Fiberglass Epoxy G-10 - LE (10^-5 m/m) -  Equation Range: 4 to 300 K (Normal Direction)	
        case 123:
            var a = -7.198 * 100 //*Math.exp(2)
            var b = 4.455 / 10 //*Math.exp(-1)
            var c = 7.505 / 1000 //*Math.exp(-3)
            var d = -2.219 / 1000000 //*Math.exp(-6)
            var e = 0

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="124"   Fiberglass Epoxy G-10 - LE (10^-5 m/m) -  Equation Range: 4 to 300 K (Wrap Direction)		
        case 124:
            var a = -2.469 * 100 //*Math.exp(2)
            var b = 2.064 / 10 //*Math.exp(-1)
            var c = 3.072 / 1000 //*Math.exp(-3)
            var d = -3.226 / 1000000 //*Math.exp(-6)
            var e = 0

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="13"   Glass Fabric-polyester - TC (W/m-K) - Equation Range: 38 to 300 K (He Wrap Direction)

        case 13:

            var a = 689.532
            var b = -2543.63
            var c = 3967.067
            var d = -3400.366
            var e = 1731.725
            var f = -524.309
            var g = 87.4249
            var h = -6.19597
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="131"   Glass Fabric-polyester - TC (W/m-K) - Equation Range: 80 to 300 K (N2 Wrap Direction)

        case 131:

            var a = -2141.58
            var b = 4639.74
            var c = -3249.405
            var d = 51.72425
            var e = 1101.977
            var f = -613.8563
            var g = 141.1432
            var h = -12.3133
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="132"   Glass Fabric-polyester - TC (W/m-K) - Equation Range: 84 to 300 K (N2 Normal Direction)	

        case 132:

            var a = 2909.905
            var b = -8616.64
            var c = 10542.69
            var d = -6832.068
            var e = 2475.328
            var f = -475.7
            var g = 37.9003
            var h = 0
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="133"   Glass Fabric-polyester - LE (10^-5 m/m) - Equation Range: 80 to 293 K (Normal Direction)	
        case 133:
            var a = -7.179 * 100 //*Math.exp(2)
            var b = -3.157 * 1 //*Math.exp(0)
            var c = 5.251 / 100 //*Math.exp(-2)
            var d = 1.947 / 10000 //*Math.exp(-4)
            var e = 2.752 / 10000000 //*Math.exp(-7)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="134"   Glass Fabric-polyester - LE (10^-5 m/m) - Equation Range: 80 to 293 K (Wrap Direction)	
        case 134:
            var a = -3.0897 * 100 //*Math.exp(2)
            var b = 1.0245 * 1 //*Math.exp(0)
            var c = -2.9503 / 1000 //*Math.exp(-3)
            var d = 1.8323 / 100000 //*Math.exp(-5)
            var e = -2.7013 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;
            // value="14"   Glass mat/epoxy - LE (10^-5 m/m) - Equation Range: 77 to 293 K (Chopped Strand mat)	
        case 14:
            var a = -6.5898 * 100 //*Math.exp(2)
            var b = 4.7697 * 1 //*Math.exp(0)
            var c = -2.9638 / 100 //*Math.exp(-2)
            var d = 1.1501 / 10000 //*Math.exp(-4)
            var e = -1.4763 / 10000000 //*Math.exp(-7)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="141"   Glass mat/epoxy - LE (10^-5 m/m) - Equation Range: 77 to 293 K (Continuous Strand)	
        case 141:
            var a = -4.392 * 100 //*Math.exp(2)
            var b = 1.525 * 1 //*Math.exp(0)
            var c = -2.384 / 1000 //*Math.exp(-3)
            var d = 8.665 / 1000000 //*Math.exp(-6)
            var e = -2.857 / 1000000000 //*Math.exp(-9)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="15"   Inconel 718 (UNS N107718) - TC (W/m-K) - Equation Range: 6 to 275 K 	

        case 15:

            var a = -8.28921
            var b = 39.447
            var c = -83.4353
            var d = 98.169
            var e = -67.2088
            var f = 26.7082
            var g = -5.7205
            var h = 0.51115
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;


            // value="151"   Inconel 718 (UNS N107718) - LE (10^-5 m/m) - Equation Range: 4 to 300 K 
        case 151:
            var a = -2.368 * 100 //*Math.exp(2)
            var b = -2.120 / 10 //*Math.exp(-1)
            var c = 5.497 / 1000 //*Math.exp(-3)
            var d = -6.882 / 1000000 //*Math.exp(-6)
            var e = 0

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;
            //************Need to complete below

            // value="16"   Indium - SH (J/kg-K) -  Equation Range: 1 to 300 K	

        case 16:

            var a = -2.4259351
            var b = 12.613611
            var c = -46.472893
            var d = 104.64717
            var e = -127.1863
            var f = 88.805612
            var g = -35.915625
            var h = 7.8307989
            var i = -0.71218931

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="17"   Invar (Fe-36Ni) (UNS K93600)  - TC (W/m-K) - Equation Range: 4  to 300 K	
        case 17:

            var a = -2.7064
            var b = 8.5191
            var c = -15.923
            var d = 18.276
            var e = -11.9116
            var f = 4.40318
            var g = -0.86018
            var h = 0.068508
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="171"   Invar (Fe-36Ni) (UNS K93600)  - SH (J/kg-K) -  Equation Range: 4  to 20 K	
        case 171:

            var a = 28.08
            var b = -228.23
            var c = 777.587
            var d = -1448.423
            var e = 1596.567
            var f = -1040.294
            var g = 371.2125
            var h = -56.004
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="172"   Invar (Fe-36Ni) (UNS K93600)  - YM (GPa) -   Equation Range: 1  to 298 K	
        case 172:

            var a = 1.41565 * 100 //*Math.exp(2)
            var b = 2.54435 / 100 //*Math.exp(-2)
            var c = -1.00842 / 1000 //*Math.exp(-3)
            var d = 6.72797 / 1000000 //*Math.exp(-6)
            var e = -1.08230 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="173"   Invar (Fe-36Ni) (UNS K93600)  - LE (10^-5 m/m) -   Equation Range: 80  to 300 K	
        case 173:

            var a = -5.265 * 10 //*Math.exp(1)
            var b = 1.009 / 10 //*Math.exp(-1)
            var c = 8.395 / 10000 //*Math.exp(-4)
            var d = -1.973 / 1000000 //*Math.exp(-6)
            var e = 9.794 / 100000000000 //*Math.exp(-11)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;



            // value="18"   Kevlar-49 Fiber - TC (W/m-K) - Equation Range: 0 to 350 K Different Equation	

        case 18:

            var a = -2.4219
            var b = 1.986637
            var c = 1.257441
            var d = 0.961209
            var e = -9.6106
            var f = 0.777857

            num1 = (a + b * Math.log10(num2)) * (1 - erf(2 * (Math.log10(num2) - c))) / 2 + (d + e * (Math
                .exp(-1 * Math.log10(num2) / f))) * (1 + erf(2 * (Math.log10(num2) - c))) / 2;
            out.value = Math.pow(10, num1).toFixed(num3);
            //Not  accurate results
            break;

            // value="19"   Kevlar-49 composite - TC (W/m-K) - Equation Range: 0 to 350 K Different Equation	

        case 19:

            var a = -2.65
            var b = 1.986637
            var c = 1.24851
            var d = 0.57
            var e = -8
            var f = 0.777857

            num1 = (a + b * Math.log10(num2)) * (1 - erf(2 * (Math.log10(num2) - c))) / 2 + (d + e * (Math
                .exp(-1 * Math.log10(num2) / f))) * (1 + erf(2 * (Math.log10(num2) - c))) / 2;
            out.value = Math.pow(10, num1).toFixed(num3);
            //Not  accurate results
            break;


            // value="20"   Lead  - TC (W/m-K) -   Equation Range: 4  to 296 K

        case 20:

            var a = 38.963479
            var b = -221.40505
            var c = 597.56622
            var d = -900.93831
            var e = 816.40461
            var f = -455.08342
            var g = 152.94025
            var h = -28.451163
            var i = 2.2516244

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="21"   Molybdenum - TC (W/m-K) - Equation Range: 2 to 373 K 	

        case 21:

            var a = 10.78259
            var b = -72.13065
            var c = 228.57351
            var d = -384.50447
            var e = 381.43825
            var f = -228.83783
            var g = 81.26658
            var h = -15.69097
            var i = 1.26814

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="211"   Molybdenum - LE (10^-5 m/m) - Equation Range: 20 to 500K 
        case 211:

            var a = -90.912613
            var b = -0.127173
            var c = 0.00266801
            var d = -5.0432 / 1000000 //*Math.exp(-6)
            var e = 3.5183 / 1000000000 //*Math.exp(-9)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;


            // value="22"   Nickel Steel Fe 2.25 Ni  - TC (W/m-K) - Equation Range: 4  to 300 K	
        case 22:

            var a = -3.5785
            var b = 20.804
            var c = -55.826
            var d = 87.812
            var e = -83.5016
            var f = 49.08
            var g = -17.4348
            var h = 3.4277
            var i = -0.28622

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="221"   Nickel Steel Fe 2.25 Ni  - SH (J/kg-K) -  Equation Range: 60  to 300 K	
        case 221:

            var a = 15503.108
            var b = -37280.377
            var c = 26788.417
            var d = 7010.0877
            var e = -22731.651
            var f = 15386.526
            var g = -5175.7968
            var h = 896.97274
            var i = -64.055866

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="222"   Nickel Steel Fe 2.25 Ni  - YM (GPa) -   Equation Range: 0  to 297 K	
        case 222:

            var a = 2.17656 * 100 //*Math.exp(2)
            var b = 1.11923 / 100 //*Math.exp(-2)
            var c = -3.54650 / 10000 //*Math.exp(-4)
            var d = 8.31168 / 10000000 //*Math.exp(-7)
            var e = -7.03680 / 10000000000 //*Math.exp(-10)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="223"   Nickel Steel Fe 2.25 Ni  - LE (10^-5 m/m) -   Equation Range: 4  to 300K	
        case 223:

            var a = -2.104 * 100 //*Math.exp(2)
            var b = -5.699 / 100 //*Math.exp(-2)
            var c = 5.072 / 1000 //*Math.exp(-3)
            var d = -1.381 / 100000 //*Math.exp(-5)
            var e = 1.897 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="23"   Nickel Steel Fe 3.25 Ni  - TC (W/m-K) - Equation Range: 4  to 300 K	
        case 23:

            var a = 0.89481
            var b = -8.1998
            var c = 22.096
            var d = -27.645
            var e = 19.7524
            var f = -8.1113
            var g = 1.77866
            var h = -0.16172
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="231"   Nickel Steel Fe 3.25 Ni  - SH (J/kg-K) -  Equation Range: 60  to 300 K	
        case 231:

            var a = 15503.108
            var b = -37280.377
            var c = 26788.417
            var d = 7010.0877
            var e = -22731.651
            var f = 15386.526
            var g = -5175.7968
            var h = 896.97274
            var i = -64.055866

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="232"   Nickel Steel Fe 3.25 Ni  - YM (GPa) -   Equation Range: 0  to 298 K	
        case 232:

            var a = 2.15351 * 100 //*Math.exp(2)
            var b = 1.04624 / 100 //*Math.exp(-2)
            var c = -3.55710 / 10000 //*Math.exp(-4)
            var d = 8.9497 / 10000000 //*Math.exp(-7)
            var e = -8.48640 / 10000000000 //*Math.exp(-10)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="233"   Nickel Steel Fe 3.25 Ni  - LE (10^-5 m/m) -   Equation Range: 4  to 300K	
        case 233:

            var a = -2.104 * 100 //*Math.exp(2)
            var b = -5.699 / 100 //*Math.exp(-2)
            var c = 5.072 / 1000 //*Math.exp(-3)
            var d = -1.381 / 100000 //*Math.exp(-5)
            var e = 1.897 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="24"   Nickel Steel Fe 5.0 Ni  - TC (W/m-K) - Equation Range: 4  to 300 K	
        case 24:

            var a = -0.57245
            var b = -0.33593
            var c = 3.9379
            var d = -5.4589
            var e = 4.2337
            var f = -1.8653
            var g = 0.43223
            var h = -0.041207
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="241"   Nickel Steel Fe 5.0 Ni  - SH (J/kg-K) -  Equation Range: 60  to 300 K	
        case 241:

            var a = 15503.108
            var b = -37280.377
            var c = 26788.417
            var d = 7010.0877
            var e = -22731.651
            var f = 15386.526
            var g = -5175.7968
            var h = 896.97274
            var i = -64.055866

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="242"   Nickel Steel Fe 5.0 Ni  - YM (GPa) -   Equation Range: 0  to 297 K	
        case 242:

            var a = 2.09182 * 100 //*Math.exp(2)
            var b = 1.66974 / 100 //*Math.exp(-2)
            var c = -2.06410 / 10000 //*Math.exp(-4)
            var d = -1.82360 / 10000000 //*Math.exp(-7)
            var e = -9.27168 / 10000000000 //*Math.exp(-10)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="243"   Nickel Steel Fe 5.0 Ni  - LE (10^-5 m/m) -   Equation Range: 4  to 300K	
        case 243:

            var a = -2.104 * 100 //*Math.exp(2)
            var b = -5.699 / 100 //*Math.exp(-2)
            var c = 5.072 / 1000 //*Math.exp(-3)
            var d = -1.381 / 100000 //*Math.exp(-5)
            var e = 1.897 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="25"   Nickel Steel Fe 9.0 Ni  - TC (W/m-K) - Equation Range: 4  to 300 K	
        case 25:

            var a = -0.0712785
            var b = -3.48735
            var c = 10.6547
            var d = -12.9153
            var e = 8.89066
            var f = -3.51482
            var g = 0.743643
            var h = -0.0657884
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="251"   Nickel Steel Fe 9.0 Ni  - SH (J/kg-K) -  Equation Range: 60  to 300 K	
        case 251:

            var a = 15503.108
            var b = -37280.377
            var c = 26788.417
            var d = 7010.0877
            var e = -22731.651
            var f = 15386.526
            var g = -5175.7968
            var h = 896.97274
            var i = -64.055866

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="252"   Nickel Steel Fe 5.0 Ni  - YM (GPa) -   Equation Range: 0  to 297 K	
        case 252:

            var a = 2.05335 * 100 //*Math.exp(2)
            var b = 1.74835 / 100 //*Math.exp(-2)
            var c = -3.65760 / 10000 //*Math.exp(-4)
            var d = 8.71545 / 10000000 //*Math.exp(-7)
            var e = -7.78130 / 10000000000 //*Math.exp(-10)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="253"   Nickel Steel Fe 5.0 Ni  - LE (10^-5 m/m) -   Equation Range: 4  to 300K	
        case 253:

            var a = -2.104 * 100 //*Math.exp(2)
            var b = -5.699 / 100 //*Math.exp(-2)
            var c = 5.072 / 1000 //*Math.exp(-3)
            var d = -1.381 / 100000 //*Math.exp(-5)
            var e = 1.897 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="26"   Platinum  - TC (W/m-K) - Equation Range: 4  to 295 K	
        case 26:

            var a = -7.33450054
            var b = 80.8550484
            var c = -268.441084
            var d = 481.629105
            var e = -503.890454
            var f = 314.812622
            var g = -115.699394
            var h = 23.0957119
            var i = -1.93361717

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="261"   Platinum  - SH (J/kg-K) -  Equation Range: 1  to 295 K	
        case 261:

            var a = -1.6135538
            var b = 0.95823584
            var c = 1.431777
            var d = -3.5963989
            var e = 5.1299735
            var f = -2.4186452
            var g = -0.12560841
            var h = 0.34342394
            var i = -0.06198179

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="27"   Polyamide (Nylon)  - TC (W/m-K) - Equation Range: 4  to 300 K	
        case 27:

            var a = -2.6135
            var b = 2.3239
            var c = -4.7586
            var d = 7.1602
            var e = -4.9155
            var f = 1.6324
            var g = -0.2507
            var h = 0.0131
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="271"   Polyamide (Nylon)  - SH (J/kg-K) -  Equation Range: 4  to 300 K	
        case 271:

            var a = -5.2929
            var b = 25.301
            var c = -54.874
            var d = 71.061
            var e = -52.236
            var f = 21.648
            var g = -4.7317
            var h = 0.42518
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="272"   Polyamide (Nylon) - LE (10^-5 m/m) -   Equation Range: 4  to 300K	
        case 272:

            var a = -1.389e3
            var b = -1.561e-1
            var c = 2.988e-2
            var d = -7.948e-5
            var e = 1.181e-7

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="28"   Polyethylene Terephthalate (Mylar) - TC (W/m-K) - Equation Range: 1  to 83 K	
        case 28:

            var a = -1.37737
            var b = -3.40668
            var c = 20.5842
            var d = -53.1244
            var e = 73.2476
            var f = -57.6546
            var g = 26.1192
            var h = -6.3479
            var i = 0.640331

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="29"   Polyimide (Kapton)  - TC (W/m-K) - Equation Range: 4  to 300 K	
        case 29:

            var a = 5.73101
            var b = -39.5199
            var c = 79.9313
            var d = -83.8572
            var e = 50.9157
            var f = -17.9835
            var g = 3.42413
            var h = -0.27133
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="291"   Polyimide (Kapton)  - SH (J/kg-K) -  Equation Range: 4  to 300 K	
        case 291:

            var a = -1.3684
            var b = 0.65892
            var c = 2.8719
            var d = 0.42651
            var e = -3.0088
            var f = 1.9558
            var g = -0.51998
            var h = 0.051574
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="330"   Polystyrene - TC (W/m-K) - Equation Range: 90 to 300 K (density: 31.88 kg/m^3 = 1.99 lb/ft^3)
        case 330:

            var a = -1557.5
            var b = 3984.7
            var c = -3940.245
            var d = 1649.668
            var e = 12.80097
            var f = -294.2616
            var g = 119.5898
            var h = -20.6301
            var i = 1.36067

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="3301"   Polystyrene - TC (W/m-K) - Equation Range: 33 to 300 K (density: 32.04 kg/m^3 = 2.0 lb/ft^3)
        case 3301:

            var a = -1145.45
            var b = 4086.02
            var c = -6234.293
            var d = 5260.106
            var e = -2649.914
            var f = 797.0372
            var g = -132.5244
            var h = 9.3968
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="3302"   Polystyrene - TC (W/m-K) - Equation Range: 7 to 300 K (density: 49.98 kg/m^3 = 3.12 lb/ft^3)	
        case 3302:

            var a = -1.5194
            var b = -4.6449
            var c = 11.643
            var d = -15.969
            var e = 12.722
            var f = -5.821
            var g = 1.4174
            var h = -0.14128
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="3303"   Polystyrene - TC (W/m-K) - Equation Range: 4 to 300 K (density: 99.96 kg/m^3 = 6.24 lb/ft^3)	
        case 3303:

            var a = 7.39582
            var b = -59.6737
            var c = 160.58
            var d = -240.33
            var e = 218.817
            var f = -124.155
            var g = 42.9088
            var h = -8.26683
            var i = 0.68082

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;


            // value="3304"   Polystyrene - SH (J/kg-K) - Equation Range: 100 to 300 K (density: 99.96 kg/m^3 = 6.24 lb/ft^3)	
        case 3304:

            var a = -5911.474
            var b = 14991.16
            var c = -15513.753
            var d = 8232.5666
            var e = -2237.3586
            var f = 225.423
            var g = 20.33505
            var h = -4.6169
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="3305"   Polystyrene - SH (J/kg-K) - Equation Range: 100 to 300 K density: 9.93 kg/m^3 = .062 lb/ft^3)
        case 3305:

            var a = -734.172
            var b = 1163.613
            var c = -135.157
            var d = -878.514
            var e = 791.787
            var f = -308.6236
            var g = 58.6764
            var h = -4.4494
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="3306"   Polystyrene - SH (J/kg-K) - Equation Range: 100 to 300 K density: (60.07 kg/m^3 = 3.75 lb/ft^3)	
        case 3306:

            var a = 2139.33
            var b = -6518.015
            var c = 9650.919
            var d = -9229.889
            var e = 6104.0571
            var f = -2739.14
            var g = 784.878
            var h = -128.40103
            var i = 9.08405

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="3307"   Polystyrene - LE (10^-5 m/m) - Equation Range: 4  to 105 K (density: 51.42 kg/m^3 = 3.21 lb/ft^3)	
        case 3307:

            var a = -1.6948 * 1000 //*Math.exp(3)
            var b = -9.6845 / 10 //*Math.exp(-1)
            var c = 7.8268 / 100 //*Math.exp(-2)
            var d = -2.4831 / 10000 //*Math.exp(-4)
            var e = 0

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="3308"   Polystyrene - LE (10^-5 m/m) - Equation Range: 105 to 278 K (density: 51.42 kg/m^3 = 3.21 lb/ft^3)	
        case 3308:

            var a = -2.1168 * 1000 //*Math.exp(3)
            var b = 1.0963 * 10 //*Math.exp(1)
            var c = -3.5335 / 100 //*Math.exp(-2)
            var d = 1.3552 / 10000 //*Math.exp(-4)
            var e = -1.9890 / 10000000 //*Math.exp(-7)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="3309"   Polystyrene - LE (10^-5 m/m) - Equation Range: 4  to 102 K (density: 102.2 kg/m^3 = 6.38 lb/ft^3)		
        case 3309:

            var a = -1.7494 * 1000 //*Math.exp(3)
            var b = 2.0607 * 1 //*Math.exp(0)
            var c = -4.7467 / 100 //*Math.exp(-2)
            var d = 1.2156 / 1000 //*Math.exp(-3)
            var e = -5.4405 / 1000000 //*Math.exp(-6)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="3310"   Polystyrene - LE (10^-5 m/m) - Equation Range: 102 to 286 K (density: 102.2 kg/m^3 = 6.38 lb/ft^3)
        case 3310:

            var a = -1.9374 * 1000 //*Math.exp(3)
            var b = 3.6139 * 1 //*Math.exp(0)
            var c = 3.5974 / 100 //*Math.exp(-2)
            var d = -1.5164 / 10000 //*Math.exp(-4)
            var e = 2.1764 / 10000000 //*Math.exp(-7)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="31"   Polyurethane - TC (W/m-K) - Equation Range: 60 to 300 K (density: 31.88 kg/m^3 = 1.99 lb/ft^3) Freon Filled
        case 31:

            var a = -3218.679
            var b = 9201.61
            var c = -10956.66
            var d = 6950.102
            var e = -2476.94
            var f = 470.284
            var g = -37.1669
            var h = 0
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="311"   Polyurethane - TC (W/m-K) - Equation Range: 85 to 300 K (density: 32.04 kg/m^3 = 2.0 lb/ft^3)CO2 Filled	
        case 311:

            var a = 3788.43
            var b = -7642.66
            var c = 4592.448
            var d = 778.8423
            var e = -2214.434
            var f = 1090.293
            var g = -235.6349
            var h = 19.66088
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="312"   Polyurethane - TC (W/m-K) - Equation Range: 20 to 300 K (density: 49.02 kg/m^3 = 3.06 lb/ft^3)He Filled	
        case 312:

            var a = -33.898
            var b = 117.81
            var c = -178.376
            var d = 142.038
            var e = -63.034
            var f = 14.958
            var g = -1.5468
            var h = 0.020625
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="313"   Polyurethane - TC (W/m-K) - Equation Range: 55 to 300 K (density: 64.08 kg/m^3 = 4.00 lb/ft^3) Freon Filled	
        case 313:

            var a = 789.79
            var b = -2347.94
            var c = 3024.61
            var d = -2206.76
            var e = 989.238
            var f = -273.18
            var g = 43.065
            var h = -2.9863
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;


            // value="314"   Polyurethane - SH (J/kg-K) - Equation Range: 90 to 300 K (density: 49.02 kg/m^3 = 3.06 lb/ft^3) He Filled		
        case 314:

            var a = 89.69
            var b = -269.32
            var c = 333.276
            var d = -214.635
            var e = 76.2052
            var f = -14.1137
            var g = 1.061
            var h = 0
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="315"   Polyurethane - SH (J/kg-K) - Equation Range: 90 to 300 K (density: 389.25 kg/m^3 = 24.3 lb/ft^3) Air Filled
        case 315:

            var a = 4894.36
            var b = -11608.63
            var c = 10463.31
            var d = -3895.8
            var e = -40.0053
            var f = 497.4517
            var g = -147.7555
            var h = 14.19365
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="316"   Polyurethane - LE (10^-5 m/m) - Equation Range: 20  to 275 K (density: 32.04 kg/m^3 = 2.0 lb/ft^3)
        case 316:

            var a = -8.064 * 100 //*Math.exp(2)
            var b = -5.049 / 10 //*Math.exp(-1)
            var c = 2.140 / 100 //*Math.exp(-2)
            var d = -5.036 / 100000 //*Math.exp(-5)
            var e = 5.192 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="317"   Polyurethane - LE (10^-5 m/m) - Equation Range: 20  to 293 K (density: 64.07 kg/m^3 = 4.0 lb/ft^3)	
        case 317:

            var a = -1.0647 * 1000 //*Math.exp(3)
            var b = 3.1238 / 10 //*Math.exp(-1)
            var c = 2.2854 / 100 //*Math.exp(-2)
            var d = -5.9123 / 100000 //*Math.exp(-5)
            var e = 6.7482 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="32"   Polyvinyl Chloride (PVC) - TC (W/m-K) - Equation Range: 90 to 300 K (density: 32.04 kg/m^3 = 2.0 lb/ft^3)CO2 Filled	
        case 32:

            var a = 11314.56
            var b = -30824.32
            var c = 34964.24
            var d = -21141.43
            var e = 7187.43
            var f = -1302.708
            var g = 98.35252
            var h = 0
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="321"   Polyvinyl Chloride (PVC) - TC (W/m-K) - Equation Range: 125 to 300 K (density: 56.06 kg/m^3 = 3.5 lb/ft^3) CO2 Filled	
        case 321:

            var a = -4123.51
            var b = 9690.59
            var c = -7920.09
            var d = 1572.897
            var e = 1459.993
            var f = -1028.329
            var g = 255.773
            var h = -23.31925
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="322"   Polyvinyl Chloride (PVC) - SH (J/kg-K) - Equation Range: 10 to 300 K (density: 48.05 kg/m^3 = 3.0 lb/ft^3) CO2 Filled
        case 322:

            var a = 190.776
            var b = -991.521
            var c = 2200.811
            var d = -2726.414
            var e = 2069.971
            var f = -988.4221
            var g = 290.405
            var h = -48.0737
            var i = 3.437928

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="323"   Polyvinyl Chloride (PVC) - LE (10^-5 m/m) - Equation Range: 4 to 280 K; CO2 Filled	
        case 323:

            var a = -1033.8
            var b = 2.1922
            var c = 8.7335 / 1000 //*Math.exp(-3)
            var d = -3.1408 / 100000 //*Math.exp(-5)
            var e = 5.9411 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1;
            break;

            // value="33"   Sapphire - EC (10^-6/K) - Equation Range: 5 to 80 K (3% Uncertainty)	
        case 33:

            var a = 10.97236
            var b = -97.2354
            var c = 240.2436
            var d = -294.9933
            var e = 195.9244
            var f = -66.89247
            var g = 9.19921
            var h = 0
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="331"   Sapphire - LE (10^-5 m/m) - Equation Range: 20 to 293 K (4% Uncertainty)	
        case 331:

            var a = -7.8850 * 10 //*Math.exp(1)
            var b = -2.2346 / 100 //*Math.exp(-2)
            var c = 1.0185 / 10000 //*Math.exp(-4)
            var d = 5.5594 / 1000000 //*Math.exp(-6)
            var e = -8.5422 / 1000000000 //*Math.exp(-9)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="34"   Silicon - EC (10^-8/K) -  Equation Range: 0  to 600 K	
        case 34:

            /*		var a = 1.00500/100000//*Math.pow(10,-5)
                    var b = -5.99688/1000000//*Math.pow(10,-6)
                    var c = 1.25574/1000000//*Math.pow(10,-6)
                    var d = -1.12086/10000000//*Math.pow(10,-7)
                    var e = 3.63225/1000000000//*Math.pow(10,-9)
                    var f = 2.67708/100//*Math.pow(10,-2)
                    var g = -1.22829/10000//*Math.pow(10,-4)
                    var h = 1.62544/1000000000000000000//*Math.pow(10,-18)
                    var i = 472.374//*Math.pow(10,2)
                    var j = -358.796//*Math.pow(10,2)
                    var k = -12419100//*Math.pow(10,7)
                    var l = 1259720000//*Math.pow(10,9) */

            var a = 1.005 * Math.pow(10, -5)
            var b = -5.99688 * Math.pow(10, -6)
            var c = 1.25574 * Math.pow(10, -6)
            var d = -1.12086 * Math.pow(10, -7)
            var e = 3.63225 * Math.pow(10, -9)
            var f = 2.67708 * Math.pow(10, -2)
            var g = -1.22829 * Math.pow(10, -4)
            var h = 1.62544 * Math.pow(10, -18)
            var i = 4.72374 * Math.pow(10, 2)
            var j = -3.58796 * Math.pow(10, 4)
            var k = -1.24191 * Math.pow(10, 7)
            var l = 1.25972 * Math.pow(10, 9)

            //		num1 = (4.8*Math.pow(10,-5)*Math.pow(num2,3)+(a*Math.pow(num2,5)+b*Math.pow(num2,5.5)+c*Math.pow(num2,6)+d*Math.pow(num2,6.5)+e*Math.pow(num2,7))*((1+erf(num2-15))/2))*((1-erf(0.2*(num2-52)))/2)+((-47.6+f*Math.pow((num2-76),2)+g*Math.pow((num2-76),3)+h*Math.pow((num2-76),9))*((1+erf(0.2*(num2-52)))/2))*((1-erf(0.1*(num2-200)))/2)+((i+j/num2+k/(Math.pow(num2,2))+l/(Math.pow(num2,3)))*((1+erf(0.1*(num2-200)))/2));
            num1 = (4.8 * Math.pow(10, -5) * Math.pow(num2, 3) + (a * Math.pow(num2, 5) + b * Math.pow(num2,
                5.5) + c * Math.pow(num2, 6) + d * Math.pow(num2, 6.5) + e * Math.pow(num2, 7)) * ((
                1 + erf(num2 - 15)) / 2)) * ((1 - erf(0.2 * (num2 - 52))) / 2) + ((-47.6 + f * Math.pow((
                num2 - 76), 2) + g * Math.pow((num2 - 76), 3) + h * Math.pow((num2 - 76), 9)) * ((1 +
                erf(0.2 * (num2 - 52))) / 2)) * ((1 - erf(0.1 * (num2 - 200))) / 2) + ((i + j / num2 + k /
                (Math.pow(num2, 2)) + l / (Math.pow(num2, 3))) * ((1 + erf(0.1 * (num2 - 200))) / 2));
            out.value = num1.toFixed(num3);

            break;

            // value="35"   Stainless Steel 304 (UNS S30400)  - TC (W/m-K) - Equation Range: 4  to 300 K	
        case 35:

            var a = -1.4087
            var b = 1.3982
            var c = 0.2543
            var d = -0.626
            var e = 0.2334
            var f = 0.4256
            var g = -0.4658
            var h = 0.165
            var i = -0.0199

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="351"   Stainless Steel 304 (UNS S30400)  - SH (J/kg-K) -  Equation Range: 4  to 300 K	
        case 351:

            var a = 22.0061
            var b = -127.5528
            var c = 303.647
            var d = -381.0098
            var e = 274.0328
            var f = -112.9212
            var g = 24.7593
            var h = -2.239153
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="352"   Stainless Steel 304 (UNS S30400)  - YM1 (GPa) -   Equation Range: 5  to 57 K	
        case 352:

            var a = 2.098145 * 100 //*Math.exp(2)
            var b = 1.217019 / 10 //*Math.exp(-1)
            var c = -1.146999 / 100 //*Math.exp(-2)
            var d = 3.605430 / 10000 //*Math.exp(-4)
            var e = -3.017900 / 1000000 //*Math.exp(-6)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="353"   Stainless Steel 304 (UNS S30400)  - YM2 (GPa) -   Equation Range: 57  to 293 K	
        case 353:

            var a = 2.100593 * 100 //*Math.exp(2)
            var b = 1.534883 / 10 //*Math.exp(-1)
            var c = -1.617390 / 1000 //*Math.exp(-3)
            var d = 5.117060 / 1000000 //*Math.exp(-6)
            var e = -6.154600 / 1000000000 //*Math.exp(-9)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="354"   Stainless Steel 304 (UNS S30400)  - LE (10^-5 m/m) -   Equation Range: 23  to 300 K	
        case 354:

            var a = -2.9554 * 100 //*Math.exp(2)
            var b = -3.9811 / 10 //*Math.exp(-1)
            var c = 9.2683 / 1000 //*Math.exp(-3)
            var d = -2.0261 / 100000 //*Math.exp(-5)
            var e = 1.7127 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="36"   Stainless Steel 304L (UNS S30403)  - TC (W/m-K) - Equation Range: 4  to 300 K	
        case 36:

            var a = -1.4087
            var b = 1.3982
            var c = 0.2543
            var d = -0.626
            var e = 0.2334
            var f = 0.4256
            var g = -0.4658
            var h = 0.165
            var i = -0.0199

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="361"   Stainless Steel 304L (UNS S30403)  - SH (J/kg-K) -  Equation Range: 4  to 20 K	
        case 361:

            var a = -351.51
            var b = 3123.695
            var c = -12017.28
            var d = 26143.99
            var e = -35176.33
            var f = 29981.75
            var g = -15812.78
            var h = 4719.64
            var i = -610.515

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="362"   Stainless Steel 304L (UNS S30403)  - LE (10^-5 m/m) -   Equation Range: 23  to 300 K	
        case 362:

            var a = -2.9554 * 100 //*Math.exp(2)
            var b = -3.9811 / 10 //*Math.exp(-1)
            var c = 9.2683 / 1000 //*Math.exp(-3)
            var d = -2.0261 / 100000 //*Math.exp(-5)
            var e = 1.7127 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="37"   Stainless Steel 310 (UNS S31000)  - TC (W/m-K) - Equation Range: 4  to 300 K	
        case 37:

            var a = -0.81907
            var b = -2.1967
            var c = 9.1059
            var d = -13.078
            var e = 10.853
            var f = -5.1269
            var g = 1.2583
            var h = -0.12395
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="371"   Stainless Steel 310 (UNS S31000)  - SH (J/kg-K) -  Equation Range: 4  to 300 K	
        case 371:

            var a = 20.694
            var b = -171.007
            var c = 600.6256
            var d = -1162.748
            var e = 1361.931
            var f = -986.2934
            var g = 430.093
            var h = -102.85
            var i = 10.275

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="372"   Stainless Steel 310 (UNS S31000)  - SH (J/kg-K) -  Equation Range: 5  to 65 K	
        case 372:

            var a = -2755.63
            var b = 9704.831
            var c = -14618.36
            var d = 12202.74
            var e = -6092.339
            var f = 1818.555
            var g = -300.458
            var h = 21.1942
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);

            break;

            // value="373"   Stainless Steel 310 (UNS S31000)  - YM (GPa) -   Equation Range: 5  to 295 K	
        case 373:

            var a = 2.066588 * 100 //*Math.exp(2)
            var b = 6.375129 / 1000 //*Math.exp(-3)
            var c = -4.34520 / 10000 //*Math.exp(-4)
            var d = 1.129930 / 1000000 //*Math.exp(-6)
            var e = -1.191600 / 1000000000 //*Math.exp(-9)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="374"   Stainless Steel 310 (UNS S31000)  - LE (10^-5 m/m) -   Equation Range: 23  to 300 K	
        case 374:

            var a = -2.9554 * 100 //*Math.exp(2)
            var b = -3.9811 / 10 //*Math.exp(-1)
            var c = 9.2683 / 1000 //*Math.exp(-3)
            var d = -2.0261 / 100000 //*Math.exp(-5)
            var e = 1.7127 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="38"   Stainless Steel 316 (UNS S31600)  - TC (W/m-K) - Equation Range: 4  to 300 K	
        case 38:

            var a = -1.4087
            var b = 1.3982
            var c = 0.2543
            var d = -0.626
            var e = 0.2334
            var f = 0.4256
            var g = -0.4658
            var h = 0.165
            var i = -0.0199

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="381"   Stainless Steel 316 (UNS S31600)  - SH1 (J/kg-K) -  Equation Range: 4  to 300 K	
        case 381:

            var a = 12.2486
            var b = -80.6422
            var c = 218.743
            var d = -308.854
            var e = 239.5296
            var f = -89.9982
            var g = 3.15315
            var h = 8.44996
            var i = -1.91368

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="382"   Stainless Steel 316 (UNS S31600)  - SH2 (J/kg-K) -  Equation Range: 4  to 300 K	
        case 382:

            var a = -1879.464
            var b = 3643.198
            var c = 76.70125
            var d = -6176.028
            var e = 7437.6247
            var f = -4305.7217
            var g = 1382.4627
            var h = -237.22704
            var i = 17.05262

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="383"   Stainless Steel 316 (UNS S31600)  - YM1 (GPa) -   Equation Range: 5  to 60 K	
        case 383:

            var a = 2.084729 * 100 //*Math.exp(2)
            var b = -1.358965 / 10 //*Math.exp(-1)
            var c = 8.368629 / 1000 //*Math.exp(-3)
            var d = -1.381700 / 10000 //*Math.exp(-4)
            var e = 6.831930 / 10000000 //*Math.exp(-7)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="384"   Stainless Steel 316 (UNS S31600)  - YM2 (GPa) -   Equation Range: 48  to 294 K	
        case 384:

            var a = 2.079488 * 100 //*Math.exp(2)
            var b = 7.394241 / 100 //*Math.exp(-2)
            var c = -9.627200 / 10000 //*Math.exp(-4)
            var d = 2.845560 / 1000000 //*Math.exp(-6)
            var e = -3.240800 / 1000000000 //*Math.exp(-9)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="385"   Stainless Steel 316 (UNS S31600)  - LE (10^-5 m/m) - Equation Range: 23  to 300 K	
        case 385:

            var a = -2.9554 * 100 //*Math.exp(2)
            var b = -3.9811 / 10 //*Math.exp(-1)
            var c = 9.2683 / 1000 //*Math.exp(-3)
            var d = -2.0261 / 100000 //*Math.exp(-5)
            var e = 1.7127 / 100000000 //*Math.exp(-8)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);
            break;

            // value="39"   Teflon - TC (W/m-K) - Equation Range: 4  to 300 K	
        case 39:

            var a = 2.738
            var b = -30.677
            var c = 89.43
            var d = -136.99
            var e = 124.69
            var f = -69.556
            var g = 23.32
            var h = -4.3135
            var i = 0.33829

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="391"   Teflon  - SH (J/kg-K) -  Equation Range: 4  to 300 K
        case 391:

            var a = 31.88256
            var b = -166.51949
            var c = 352.01879
            var d = -393.44232
            var e = 259.98072
            var f = -104.61429
            var g = 24.99276
            var h = -3.20792
            var i = 0.16503

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="392"   Teflon  - LE (10^-5 m/m) - Equation Range: 4  to 300 K	
        case 392:

            var a = -2.125 * 1000 //*Math.exp(3)
            var b = -8.201 / 10 //*Math.exp(-1)
            var c = 6.161 / 100 //*Math.exp(-2)
            var d = -3.171 / 10000 //*Math.exp(-4)
            var e = 6.850 / 10000000 //*Math.exp(-7)

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="40"   Ti-6Al-4V (UNS R56400)  - TC (W/m-K) - Equation Range: 23  to 300 K	
        case 40:

            var a = -5107.8774
            var b = 19240.422
            var c = -30789.064
            var d = 27134.756
            var e = -14226.379
            var f = 4438.2154
            var g = -763.07767
            var h = 55.796592
            var i = 0

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

            // value="401"   Ti-6Al-4V (UNS R56400)  - LE (10^-5 m/m) - Equation Range: 24  to 300 K
        case 401:

            var a = -1.711 * 100 //*Math.exp(2)
            var b = -2.140 / 10 //*Math.exp(-1)
            var c = 4.807 / 1000 //*Math.exp(-3)
            var d = -7.111 / 1000000 //*Math.exp(-6)
            var e = 0

            num1 = a + b * num2 + c * Math.pow(num2, 2) + d * Math.pow(num2, 3) + e * Math.pow(num2, 4);
            out.value = num1.toFixed(num3);

            break;

            // value="41"   Titanium 15-3-3-3 - TC (W/m-K) - Equation Range: 1.4  to 300 K	
        case 41:

            var a = -2.398794842
            var b = 8.970743802
            var c = -29.19286973
            var d = 54.87139779
            var e = -59.67137228
            var f = 38.89321714
            var g = -14.94175848
            var h = 3.111616089
            var i = -0.270452768

            num1 = a + b * Math.log10(num2) + c * Math.pow(Math.log10(num2), 2) + d * Math.pow(Math.log10(
                    num2), 3) + e * Math.pow(Math.log10(num2), 4) + f * Math.pow(Math.log10(num2), 5) + g *
                Math.pow(Math.log10(num2), 6) + h * Math.pow(Math.log10(num2), 7) + i * Math.pow(Math.log10(
                    num2), 8);
            out.value = Math.pow(10, num1).toFixed(num3);
            break;

        case 42:
            // value="42"   Silicon - EC (10^-8/K) -  Equation Range: 0  to 600 K	

            /*		var a = 1.00500/100000//*Math.pow(10,-5)
                    var b = -5.99688/1000000//*Math.pow(10,-6)
                    var c = 1.25574/1000000//*Math.pow(10,-6)
                    var d = -1.12086/10000000//*Math.pow(10,-7)
                    var e = 3.63225/1000000000//*Math.pow(10,-9)
                    var f = 2.67708/100//*Math.pow(10,-2)
                    var g = -1.22829/10000//*Math.pow(10,-4)
                    var h = 1.62544/1000000000000000000//*Math.pow(10,-18)
                    var i = 472.374//*Math.pow(10,2)
                    var j = -358.796//*Math.pow(10,2)
                    var k = -12419100//*Math.pow(10,7)
                    var l = 1259720000//*Math.pow(10,9) */

            var a = 1.005 * Math.pow(10, -5)
            var b = -5.99688 * Math.pow(10, -6)
            var c = 1.25574 * Math.pow(10, -6)
            var d = -1.12086 * Math.pow(10, -7)
            var e = 3.63225 * Math.pow(10, -9)
            var f = 2.67708 * Math.pow(10, -2)
            var g = -1.22829 * Math.pow(10, -4)
            var h = 1.62544 * Math.pow(10, -18)
            var i = 4.72374 * Math.pow(10, 2)
            var j = -3.58796 * Math.pow(10, 4)
            var k = -1.24191 * Math.pow(10, 7)
            var l = 1.25972 * Math.pow(10, 9)

            //		num1 = (4.8*Math.pow(10,-5)*Math.pow(num2,3)+(a*Math.pow(num2,5)+b*Math.pow(num2,5.5)+c*Math.pow(num2,6)+d*Math.pow(num2,6.5)+e*Math.pow(num2,7))*((1+erf(num2-15))/2))*((1-erf(0.2*(num2-52)))/2)+((-47.6+f*Math.pow((num2-76),2)+g*Math.pow((num2-76),3)+h*Math.pow((num2-76),9))*((1+erf(0.2*(num2-52)))/2))*((1-erf(0.1*(num2-200)))/2)+((i+j/num2+k/(Math.pow(num2,2))+l/(Math.pow(num2,3)))*((1+erf(0.1*(num2-200)))/2));
            num1 = (4.8 * Math.pow(10, -5) * Math.pow(num2, 3) + (a * Math.pow(num2, 5) + b * Math.pow(num2,
                5.5) + c * Math.pow(num2, 6) + d * Math.pow(num2, 6.5) + e * Math.pow(num2, 7)) * ((
                1 + erf(num2 - 15)) / 2)) * ((1 - erf(0.2 * (num2 - 52))) / 2) + ((-47.6 + f * Math.pow((
                num2 - 76), 2) + g * Math.pow((num2 - 76), 3) + h * Math.pow((num2 - 76), 9)) * ((1 +
                erf(0.2 * (num2 - 52))) / 2)) * ((1 - erf(0.1 * (num2 - 200))) / 2) + ((i + j / num2 + k /
                (Math.pow(num2, 2)) + l / (Math.pow(num2, 3))) * ((1 + erf(0.1 * (num2 - 200))) / 2));
            out.value = num1.toFixed(num3);
            break;


        default:
            break;
    }
}