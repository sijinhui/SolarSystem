// Generated case design for Access/Access.kicad_pcb
// By https://github.com/revk/PCBCase
// Generated 2026-03-06 12:17:54
// title:	Access Control
// rev:	3
// company:	Adrian Kennard Andrews & Arnold Ltd
// comment:	toot.me.uk/@RevK
// comment:	www.me.uk
//

// Globals
margin=0.200000;
lip=3.000000;
lipa=0;
lipt=2;
casewall=3.000000;
casebottom=2.000000;
casetop=6.500000;
bottomthickness=0.000000;
topthickness=0.000000;
fit=0.000000;
snap=0.150000;
edge=2.000000;
pcbthickness=1.200000;
function pcbthickness()=1.200000;
nohull=false;
hullcap=1.000000;
hulledge=1.000000;
useredge=false;
datex=0.000000;
datey=0.000000;
datet=0.500000;
dateh=3.000000;
datea=0;
date="2026-02-22";
datef="OCRB";
logox=0.000000;
logoy=0.000000;
logot=0.500000;
logoh=10.000000;
logoa=0;
logo="A";
logof="AJK";
namex=0.000000;
namey=-10.000000;
namet=0.500000;
nameh=5.000000;
namea=0;
name="Access Control";
namef="OCRB";
spacing=65.300000;
pcbwidth=49.300000;
function pcbwidth()=49.300000;
pcblength=24.400000;
function pcblength()=24.400000;
originx=100.150000;
originy=99.500000;

module outline(h=pcbthickness,r=0){linear_extrude(height=h)offset(r=r)polygon(points=[[-24.650000,-12.200000],[-24.650000,12.200000],[24.650000,12.200000],[24.650000,-12.200000]],paths=[[0,1,2,3]]);}

module pcb(h=pcbthickness,r=0){linear_extrude(height=h)offset(r=r)polygon(points=[[-24.650000,-12.200000],[-24.650000,12.200000],[24.650000,12.200000],[24.650000,-12.200000]],paths=[[0,1,2,3]]);}
module J5(){translate([21.300000,5.050000,1.200000])rotate([0,0,180.000000])children();}
module part_J5(part=true,hole=false,block=false,punch=false)
{
translate([21.300000,5.050000,1.200000])rotate([0,0,180.000000])m0(part,hole,block,punch,casetop,2); // J5
};
module J6(){translate([7.500000,5.050000,1.200000])rotate([0,0,180.000000])children();}
module part_J6(part=true,hole=false,block=false,punch=false)
{
translate([7.500000,5.050000,1.200000])rotate([0,0,180.000000])m1(part,hole,block,punch,casetop,2); // J6
};
module J2(){translate([-1.900000,5.057500,1.200000])rotate([0,0,180.000000])children();}
module part_J2(part=true,hole=false,block=false,punch=false)
{
translate([-1.900000,5.057500,1.200000])rotate([0,0,180.000000])m2(part,hole,block,punch,casetop,4); // J2
};
module J3(){translate([-16.300000,5.057500,1.200000])rotate([0,0,180.000000])children();}
module part_J3(part=true,hole=false,block=false,punch=false)
{
translate([-16.300000,5.057500,1.200000])rotate([0,0,180.000000])m2(part,hole,block,punch,casetop,6); // J2
};
module C12(){translate([-13.800000,3.000000,1.200000])rotate([0,0,-90.000000])children();}
module part_C12(part=true,hole=false,block=false,punch=false)
{
translate([-13.800000,3.000000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module R16(){translate([12.850000,-5.400000,1.200000])rotate([0,0,90.000000])children();}
module part_R16(part=true,hole=false,block=false,punch=false)
{
translate([12.850000,-5.400000,1.200000])rotate([0,0,90.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module D16(){translate([-17.549000,3.000000,1.200000])rotate([0,0,45.000000])children();}
module part_D16(part=true,hole=false,block=false,punch=false)
{
translate([-17.549000,3.000000,1.200000])rotate([0,0,45.000000])m5(part,hole,block,punch,casetop); // D16
};
module SW1(){translate([-7.750000,-5.800000,1.200000])rotate([0,0,90.000000])children();}
module part_SW1(part=true,hole=false,block=false,punch=false)
{
translate([-7.750000,-5.800000,1.200000])rotate([0,0,90.000000])translate([2.050000,0.000000,1.150000])rotate([-0.000000,-0.000000,-90.000000])m6(part,hole,block,punch,casetop); // RevK:ESE13 ESE13V01D (back)
};
module V2(){translate([-0.150000,-12.200000,1.200000])rotate([0,0,180.000000])children();}
module part_V2(part=true,hole=false,block=false,punch=false)
{
};
module R10(){translate([-15.550000,0.900000,1.200000])rotate([0,0,-90.000000])children();}
module part_R10(part=true,hole=false,block=false,punch=false)
{
translate([-15.550000,0.900000,1.200000])rotate([0,0,-90.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module C3(){translate([-11.450000,0.900000,1.200000])rotate([0,0,-90.000000])children();}
module part_C3(part=true,hole=false,block=false,punch=false)
{
translate([-11.450000,0.900000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module R25(){translate([23.550000,-1.700000,1.200000])rotate([0,0,180.000000])children();}
module part_R25(part=true,hole=false,block=false,punch=false)
{
translate([23.550000,-1.700000,1.200000])rotate([0,0,180.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module C22(){translate([-23.093750,-8.300000,1.200000])rotate([0,0,-90.000000])children();}
module part_C22(part=true,hole=false,block=false,punch=false)
{
translate([-23.093750,-8.300000,1.200000])rotate([0,0,-90.000000])m7(part,hole,block,punch,casetop); // RevK:C_0603_ C_0603_1608Metric (back)
};
module R26(){translate([-5.550000,-8.800000,1.200000])rotate([0,0,-90.000000])children();}
module part_R26(part=true,hole=false,block=false,punch=false)
{
translate([-5.550000,-8.800000,1.200000])rotate([0,0,-90.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module C5(){translate([-16.450000,0.900000,1.200000])rotate([0,0,-90.000000])children();}
module part_C5(part=true,hole=false,block=false,punch=false)
{
translate([-16.450000,0.900000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module D10(){translate([-6.300000,3.100000,1.200000])rotate([0,0,-90.000000])children();}
module part_D10(part=true,hole=false,block=false,punch=false)
{
translate([-6.300000,3.100000,1.200000])rotate([0,0,-90.000000])m8(part,hole,block,punch,casetop); // D10
};
module D8(){translate([-22.250000,0.950000,1.200000])rotate([0,0,-90.000000])children();}
module part_D8(part=true,hole=false,block=false,punch=false)
{
translate([-22.250000,0.950000,1.200000])rotate([0,0,-90.000000])m8(part,hole,block,punch,casetop); // D10
};
module L4(){translate([-20.593750,-5.000000,1.200000])rotate([0,0,180.000000])children();}
module part_L4(part=true,hole=false,block=false,punch=false)
{
translate([-20.593750,-5.000000,1.200000])rotate([0,0,180.000000])rotate([-0.000000,-0.000000,-90.000000])m9(part,hole,block,punch,casetop); // RevK:L_4x4_ TYA4020 (back)
};
module C17(){translate([-16.950000,-3.900000,1.200000])rotate([0,0,90.000000])children();}
module part_C17(part=true,hole=false,block=false,punch=false)
{
translate([-16.950000,-3.900000,1.200000])rotate([0,0,90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module J1(){translate([19.690000,-6.410000,1.200000])children();}
module part_J1(part=true,hole=false,block=false,punch=false)
{
translate([19.690000,-6.410000,1.200000])translate([0.000000,-2.400000,0.000000])rotate([90.000000,-0.000000,-0.000000])m10(part,hole,block,punch,casetop); // RevK:USB-C-Socket-H CSP-USC16-TR (back)
};
module Q2(){translate([-6.550000,0.600000,1.200000])rotate([0,0,180.000000])children();}
module part_Q2(part=true,hole=false,block=false,punch=false)
{
translate([-6.550000,0.600000,1.200000])rotate([0,0,180.000000])m11(part,hole,block,punch,casetop); // Q2
};
module C7(){translate([-21.450000,0.900000,1.200000])rotate([0,0,-90.000000])children();}
module part_C7(part=true,hole=false,block=false,punch=false)
{
translate([-21.450000,0.900000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module R2(){translate([-11.600000,-3.450000,1.200000])children();}
module part_R2(part=true,hole=false,block=false,punch=false)
{
translate([-11.600000,-3.450000,1.200000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module U1(){translate([-13.400000,-5.350000,1.200000])children();}
module part_U1(part=true,hole=false,block=false,punch=false)
{
translate([-13.400000,-5.350000,1.200000])m12(part,hole,block,punch,casetop); // RevK:SOT-23-6-MD8942 SOT-23-6 (back)
};
module C10(){translate([13.100000,3.000000,1.200000])rotate([0,0,-90.000000])children();}
module part_C10(part=true,hole=false,block=false,punch=false)
{
translate([13.100000,3.000000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module R8(){translate([-10.550000,0.900000,1.200000])rotate([0,0,-90.000000])children();}
module part_R8(part=true,hole=false,block=false,punch=false)
{
translate([-10.550000,0.900000,1.200000])rotate([0,0,-90.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module C26(){translate([20.050000,3.000000,1.200000])rotate([0,0,-90.000000])children();}
module part_C26(part=true,hole=false,block=false,punch=false)
{
translate([20.050000,3.000000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module C25(){translate([-23.800000,2.950000,1.200000])rotate([0,0,-90.000000])children();}
module part_C25(part=true,hole=false,block=false,punch=false)
{
translate([-23.800000,2.950000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module D1(){translate([-9.650000,0.975000,1.200000])rotate([0,0,-90.000000])children();}
module part_D1(part=true,hole=false,block=false,punch=false)
{
translate([-9.650000,0.975000,1.200000])rotate([0,0,-90.000000])m8(part,hole,block,punch,casetop); // D10
};
module D17(){translate([-20.049000,3.000000,1.200000])rotate([0,0,45.000000])children();}
module part_D17(part=true,hole=false,block=false,punch=false)
{
translate([-20.049000,3.000000,1.200000])rotate([0,0,45.000000])m5(part,hole,block,punch,casetop); // D16
};
module D4(){translate([-17.250000,0.975000,1.200000])rotate([0,0,-90.000000])children();}
module part_D4(part=true,hole=false,block=false,punch=false)
{
translate([-17.250000,0.975000,1.200000])rotate([0,0,-90.000000])m8(part,hole,block,punch,casetop); // D10
};
module C15(){translate([-10.900000,-6.650000,1.200000])rotate([0,0,90.000000])children();}
module part_C15(part=true,hole=false,block=false,punch=false)
{
translate([-10.900000,-6.650000,1.200000])rotate([0,0,90.000000])m7(part,hole,block,punch,casetop); // RevK:C_0603_ C_0603_1608Metric (back)
};
module C19(){translate([11.150000,-7.400000,1.200000])rotate([0,0,90.000000])children();}
module part_C19(part=true,hole=false,block=false,punch=false)
{
translate([11.150000,-7.400000,1.200000])rotate([0,0,90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module C16(){translate([-13.400000,-7.350000,1.200000])children();}
module part_C16(part=true,hole=false,block=false,punch=false)
{
translate([-13.400000,-7.350000,1.200000])m7(part,hole,block,punch,casetop); // RevK:C_0603_ C_0603_1608Metric (back)
};
module D6(){translate([-19.750000,1.000000,1.200000])rotate([0,0,-90.000000])children();}
module part_D6(part=true,hole=false,block=false,punch=false)
{
translate([-19.750000,1.000000,1.200000])rotate([0,0,-90.000000])m8(part,hole,block,punch,casetop); // D10
};
module C14(){translate([-18.800000,3.000000,1.200000])rotate([0,0,-90.000000])children();}
module part_C14(part=true,hole=false,block=false,punch=false)
{
translate([-18.800000,3.000000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module C21(){translate([-18.093750,-8.100000,1.200000])rotate([0,0,-90.000000])children();}
module part_C21(part=true,hole=false,block=false,punch=false)
{
translate([-18.093750,-8.100000,1.200000])rotate([0,0,-90.000000])m7(part,hole,block,punch,casetop); // RevK:C_0603_ C_0603_1608Metric (back)
};
module J7(){translate([14.400000,5.057500,1.200000])rotate([0,0,180.000000])children();}
module part_J7(part=true,hole=false,block=false,punch=false)
{
translate([14.400000,5.057500,1.200000])rotate([0,0,180.000000])m1(part,hole,block,punch,casetop,2); // J6
};
module R15(){translate([-22.393750,-11.500000,1.200000])rotate([0,0,180.000000])children();}
module part_R15(part=true,hole=false,block=false,punch=false)
{
translate([-22.393750,-11.500000,1.200000])rotate([0,0,180.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module R9(){translate([-13.050000,0.900000,1.200000])rotate([0,0,-90.000000])children();}
module part_R9(part=true,hole=false,block=false,punch=false)
{
translate([-13.050000,0.900000,1.200000])rotate([0,0,-90.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module C24(){translate([-21.300000,3.000000,1.200000])rotate([0,0,-90.000000])children();}
module part_C24(part=true,hole=false,block=false,punch=false)
{
translate([-21.300000,3.000000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module R27(){translate([-18.793750,-11.500000,1.200000])rotate([0,0,180.000000])children();}
module part_R27(part=true,hole=false,block=false,punch=false)
{
translate([-18.793750,-11.500000,1.200000])rotate([0,0,180.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module D15(){translate([-15.049000,3.000000,1.200000])rotate([0,0,45.000000])children();}
module part_D15(part=true,hole=false,block=false,punch=false)
{
translate([-15.049000,3.000000,1.200000])rotate([0,0,45.000000])m5(part,hole,block,punch,casetop); // D16
};
module C2(){translate([-7.100000,3.000000,1.200000])rotate([0,0,-90.000000])children();}
module part_C2(part=true,hole=false,block=false,punch=false)
{
translate([-7.100000,3.000000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module C11(){translate([-11.300000,3.000000,1.200000])rotate([0,0,-90.000000])children();}
module part_C11(part=true,hole=false,block=false,punch=false)
{
translate([-11.300000,3.000000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module C28(){translate([-8.650000,-10.300000,1.200000])rotate([0,0,180.000000])children();}
module part_C28(part=true,hole=false,block=false,punch=false)
{
translate([-8.650000,-10.300000,1.200000])rotate([0,0,180.000000])m13(part,hole,block,punch,casetop); // RevK:C_1210 C_1210_3225Metric (back)
};
module C27(){translate([12.850000,-8.900000,1.200000])rotate([0,0,90.000000])children();}
module part_C27(part=true,hole=false,block=false,punch=false)
{
translate([12.850000,-8.900000,1.200000])rotate([0,0,90.000000])m14(part,hole,block,punch,casetop); // RevK:C_1206 C_1206_3216Metric (back)
};
module C23(){translate([-20.593750,-7.600000,1.200000])rotate([0,0,180.000000])children();}
module part_C23(part=true,hole=false,block=false,punch=false)
{
translate([-20.593750,-7.600000,1.200000])rotate([0,0,180.000000])m7(part,hole,block,punch,casetop); // RevK:C_0603_ C_0603_1608Metric (back)
};
module R5(){translate([14.350000,-10.100000,1.200000])rotate([0,0,90.000000])children();}
module part_R5(part=true,hole=false,block=false,punch=false)
{
translate([14.350000,-10.100000,1.200000])rotate([0,0,90.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module D9(){translate([-8.700000,2.225000,1.200000])rotate([0,0,90.000000])children();}
module part_D9(part=true,hole=false,block=false,punch=false)
{
translate([-8.700000,2.225000,1.200000])rotate([0,0,90.000000])m8(part,hole,block,punch,casetop); // D10
};
module R12(){translate([-20.550000,0.900000,1.200000])rotate([0,0,-90.000000])children();}
module part_R12(part=true,hole=false,block=false,punch=false)
{
translate([-20.550000,0.900000,1.200000])rotate([0,0,-90.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module R1(){translate([-13.400000,-3.450000,1.200000])children();}
module part_R1(part=true,hole=false,block=false,punch=false)
{
translate([-13.400000,-3.450000,1.200000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module D3(){translate([-14.750000,0.975000,1.200000])rotate([0,0,-90.000000])children();}
module part_D3(part=true,hole=false,block=false,punch=false)
{
translate([-14.750000,0.975000,1.200000])rotate([0,0,-90.000000])m8(part,hole,block,punch,casetop); // D10
};
module C20(){translate([-5.550000,-10.600000,1.200000])rotate([0,0,-90.000000])children();}
module part_C20(part=true,hole=false,block=false,punch=false)
{
translate([-5.550000,-10.600000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module PCB1(){translate([-0.150000,-0.500000,1.200000])children();}
module part_PCB1(part=true,hole=false,block=false,punch=false)
{
};
module D18(){translate([-22.549000,3.000000,1.200000])rotate([0,0,45.000000])children();}
module part_D18(part=true,hole=false,block=false,punch=false)
{
translate([-22.549000,3.000000,1.200000])rotate([0,0,45.000000])m5(part,hole,block,punch,casetop); // D16
};
module D19(){translate([22.150000,1.200000,1.200000])children();}
module part_D19(part=true,hole=false,block=false,punch=false)
{
translate([22.150000,1.200000,1.200000])m15(part,hole,block,punch,casetop); // D19
};
module R4(){translate([14.350000,-6.800000,1.200000])rotate([0,0,90.000000])children();}
module part_R4(part=true,hole=false,block=false,punch=false)
{
translate([14.350000,-6.800000,1.200000])rotate([0,0,90.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module C8(){translate([-23.950000,0.900000,1.200000])rotate([0,0,-90.000000])children();}
module part_C8(part=true,hole=false,block=false,punch=false)
{
translate([-23.950000,0.900000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module R6(){translate([-7.900000,3.000000,1.200000])rotate([0,0,-90.000000])children();}
module part_R6(part=true,hole=false,block=false,punch=false)
{
translate([-7.900000,3.000000,1.200000])rotate([0,0,-90.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module D11(){translate([14.350000,3.000000,1.200000])rotate([0,0,45.000000])children();}
module part_D11(part=true,hole=false,block=false,punch=false)
{
translate([14.350000,3.000000,1.200000])rotate([0,0,45.000000])m5(part,hole,block,punch,casetop); // D16
};
module U3(){translate([12.850000,-2.000000,1.200000])children();}
module part_U3(part=true,hole=false,block=false,punch=false)
{
translate([12.850000,-2.000000,1.200000])m16(part,hole,block,punch,casetop); // U3
};
module D5(){translate([17.750000,1.200000,1.200000])rotate([0,0,180.000000])children();}
module part_D5(part=true,hole=false,block=false,punch=false)
{
translate([17.750000,1.200000,1.200000])rotate([0,0,180.000000])m15(part,hole,block,punch,casetop); // D19
};
module U2(){translate([-20.593750,-9.600000,1.200000])rotate([0,0,180.000000])children();}
module part_U2(part=true,hole=false,block=false,punch=false)
{
translate([-20.593750,-9.600000,1.200000])rotate([0,0,180.000000])m12(part,hole,block,punch,casetop); // RevK:SOT-23-6-MD8942 SOT-23-6 (back)
};
module C6(){translate([-18.950000,0.900000,1.200000])rotate([0,0,-90.000000])children();}
module part_C6(part=true,hole=false,block=false,punch=false)
{
translate([-18.950000,0.900000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module R7(){translate([-5.500000,2.950000,1.200000])rotate([0,0,-90.000000])children();}
module part_R7(part=true,hole=false,block=false,punch=false)
{
translate([-5.500000,2.950000,1.200000])rotate([0,0,-90.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module U10(){translate([2.850000,-4.000000,1.200000])rotate([0,0,180.000000])children();}
module part_U10(part=true,hole=false,block=false,punch=false)
{
translate([2.850000,-4.000000,1.200000])rotate([0,0,180.000000])m17(part,hole,block,punch,casetop); // U10
};
module D14(){translate([-12.549000,3.000000,1.200000])rotate([0,0,45.000000])children();}
module part_D14(part=true,hole=false,block=false,punch=false)
{
translate([-12.549000,3.000000,1.200000])rotate([0,0,45.000000])m5(part,hole,block,punch,casetop); // D16
};
module R11(){translate([-18.050000,0.900000,1.200000])rotate([0,0,-90.000000])children();}
module part_R11(part=true,hole=false,block=false,punch=false)
{
translate([-18.050000,0.900000,1.200000])rotate([0,0,-90.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module C13(){translate([-16.300000,3.000000,1.200000])rotate([0,0,-90.000000])children();}
module part_C13(part=true,hole=false,block=false,punch=false)
{
translate([-16.300000,3.000000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module U8(){translate([20.150000,-2.000000,1.200000])rotate([0,0,90.000000])children();}
module part_U8(part=true,hole=false,block=false,punch=false)
{
translate([20.150000,-2.000000,1.200000])rotate([0,0,90.000000])m16(part,hole,block,punch,casetop); // U3
};
module D7(){translate([21.250000,3.000000,1.200000])rotate([0,0,45.000000])children();}
module part_D7(part=true,hole=false,block=false,punch=false)
{
translate([21.250000,3.000000,1.200000])rotate([0,0,45.000000])m5(part,hole,block,punch,casetop); // D16
};
module D2(){translate([-12.250000,0.975000,1.200000])rotate([0,0,-90.000000])children();}
module part_D2(part=true,hole=false,block=false,punch=false)
{
translate([-12.250000,0.975000,1.200000])rotate([0,0,-90.000000])m8(part,hole,block,punch,casetop); // D10
};
module D13(){translate([-10.049000,3.000000,1.200000])rotate([0,0,45.000000])children();}
module part_D13(part=true,hole=false,block=false,punch=false)
{
translate([-10.049000,3.000000,1.200000])rotate([0,0,45.000000])m5(part,hole,block,punch,casetop); // D16
};
module V1(){translate([-0.150000,12.200000,1.200000])children();}
module part_V1(part=true,hole=false,block=false,punch=false)
{
};
module L3(){translate([-13.400000,-9.950000,1.200000])children();}
module part_L3(part=true,hole=false,block=false,punch=false)
{
translate([-13.400000,-9.950000,1.200000])rotate([-0.000000,-0.000000,-90.000000])m9(part,hole,block,punch,casetop); // RevK:L_4x4_ TYA4020 (back)
};
module C1(){translate([-15.900000,-6.650000,1.200000])rotate([0,0,90.000000])children();}
module part_C1(part=true,hole=false,block=false,punch=false)
{
translate([-15.900000,-6.650000,1.200000])rotate([0,0,90.000000])m7(part,hole,block,punch,casetop); // RevK:C_0603_ C_0603_1608Metric (back)
};
module R13(){translate([-23.050000,0.900000,1.200000])rotate([0,0,-90.000000])children();}
module part_R13(part=true,hole=false,block=false,punch=false)
{
translate([-23.050000,0.900000,1.200000])rotate([0,0,-90.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
module D12(){translate([11.850000,3.000000,1.200000])rotate([0,0,45.000000])children();}
module part_D12(part=true,hole=false,block=false,punch=false)
{
translate([11.850000,3.000000,1.200000])rotate([0,0,45.000000])m5(part,hole,block,punch,casetop); // D16
};
module C18(){translate([11.150000,-9.200000,1.200000])rotate([0,0,-90.000000])children();}
module part_C18(part=true,hole=false,block=false,punch=false)
{
translate([11.150000,-9.200000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module C9(){translate([15.600000,3.000000,1.200000])rotate([0,0,-90.000000])children();}
module part_C9(part=true,hole=false,block=false,punch=false)
{
translate([15.600000,3.000000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module C4(){translate([-13.950000,0.900000,1.200000])rotate([0,0,-90.000000])children();}
module part_C4(part=true,hole=false,block=false,punch=false)
{
translate([-13.950000,0.900000,1.200000])rotate([0,0,-90.000000])m3(part,hole,block,punch,casetop); // RevK:C_0402 C_0402_1005Metric (back)
};
module R14(){translate([-20.593750,-11.500000,1.200000])rotate([0,0,180.000000])children();}
module part_R14(part=true,hole=false,block=false,punch=false)
{
translate([-20.593750,-11.500000,1.200000])rotate([0,0,180.000000])m4(part,hole,block,punch,casetop); // RevK:R_0402 R_0402_1005Metric (back)
};
// Parts to go on PCB (top)
module parts_top(part=false,hole=false,block=false,punch=false){
part_J5(part,hole,block,punch);
part_J6(part,hole,block,punch);
part_J2(part,hole,block,punch);
part_J3(part,hole,block,punch);
part_C12(part,hole,block,punch);
part_R16(part,hole,block,punch);
part_D16(part,hole,block,punch);
part_SW1(part,hole,block,punch);
part_V2(part,hole,block,punch);
part_R10(part,hole,block,punch);
part_C3(part,hole,block,punch);
part_R25(part,hole,block,punch);
part_C22(part,hole,block,punch);
part_R26(part,hole,block,punch);
part_C5(part,hole,block,punch);
part_D10(part,hole,block,punch);
part_D8(part,hole,block,punch);
part_L4(part,hole,block,punch);
part_C17(part,hole,block,punch);
part_J1(part,hole,block,punch);
part_Q2(part,hole,block,punch);
part_C7(part,hole,block,punch);
part_R2(part,hole,block,punch);
part_U1(part,hole,block,punch);
part_C10(part,hole,block,punch);
part_R8(part,hole,block,punch);
part_C26(part,hole,block,punch);
part_C25(part,hole,block,punch);
part_D1(part,hole,block,punch);
part_D17(part,hole,block,punch);
part_D4(part,hole,block,punch);
part_C15(part,hole,block,punch);
part_C19(part,hole,block,punch);
part_C16(part,hole,block,punch);
part_D6(part,hole,block,punch);
part_C14(part,hole,block,punch);
part_C21(part,hole,block,punch);
part_J7(part,hole,block,punch);
part_R15(part,hole,block,punch);
part_R9(part,hole,block,punch);
part_C24(part,hole,block,punch);
part_R27(part,hole,block,punch);
part_D15(part,hole,block,punch);
part_C2(part,hole,block,punch);
part_C11(part,hole,block,punch);
part_C28(part,hole,block,punch);
part_C27(part,hole,block,punch);
part_C23(part,hole,block,punch);
part_R5(part,hole,block,punch);
part_D9(part,hole,block,punch);
part_R12(part,hole,block,punch);
part_R1(part,hole,block,punch);
part_D3(part,hole,block,punch);
part_C20(part,hole,block,punch);
part_PCB1(part,hole,block,punch);
part_D18(part,hole,block,punch);
part_D19(part,hole,block,punch);
part_R4(part,hole,block,punch);
part_C8(part,hole,block,punch);
part_R6(part,hole,block,punch);
part_D11(part,hole,block,punch);
part_U3(part,hole,block,punch);
part_D5(part,hole,block,punch);
part_U2(part,hole,block,punch);
part_C6(part,hole,block,punch);
part_R7(part,hole,block,punch);
part_U10(part,hole,block,punch);
part_D14(part,hole,block,punch);
part_R11(part,hole,block,punch);
part_C13(part,hole,block,punch);
part_U8(part,hole,block,punch);
part_D7(part,hole,block,punch);
part_D2(part,hole,block,punch);
part_D13(part,hole,block,punch);
part_V1(part,hole,block,punch);
part_L3(part,hole,block,punch);
part_C1(part,hole,block,punch);
part_R13(part,hole,block,punch);
part_D12(part,hole,block,punch);
part_C18(part,hole,block,punch);
part_C9(part,hole,block,punch);
part_C4(part,hole,block,punch);
part_R14(part,hole,block,punch);
}

parts_top=80;
module J4(){translate([2.850000,-0.100000,0.000000])rotate([0,0,180.000000])rotate([180,0,0])children();}
module part_J4(part=true,hole=false,block=false,punch=false)
{
};
module J8(){translate([2.850000,-7.550000,0.000000])rotate([180,0,0])children();}
module part_J8(part=true,hole=false,block=false,punch=false)
{
};
// Parts to go on PCB (bottom)
module parts_bottom(part=false,hole=false,block=false,punch=false){
part_J4(part,hole,block,punch);
part_J8(part,hole,block,punch);
}

parts_bottom=0;
module b(cx,cy,z,w,l,h){translate([cx-w/2,cy-l/2,z])cube([w,l,h]);}
module m0(part=false,hole=false,block=false,punch=false,height,N=0)
{ // J5
// PTSM socket
if(part)
{
	hull()
	{
		b(0,-7.5/2+0.3,0,1.7+N*2.5,7.5,4);
		b(0,-7.5/2+0.3,0,1.7+N*2.5-2,7.5,5);
	}
	// Pins
	for(p=[0:N-1])translate([-2.5*(N-1)/2+p*2.5,0,-2.1])cylinder(r1=0.3,r2=1,h=2.1);
}
if(hole)
{
	b(0,-10.5/2-7.5+0.3,0,1.1+N*2.5,10.5,5);
}
}

module m1(part=false,hole=false,block=false,punch=false,height,N=0)
{ // J6
// PTSM socket
if(part)
{
	hull()
	{
		b(0,-7.5/2+0.3,0,1.7+N*2.5,7.5,4);
		b(0,-7.5/2+0.3,0,1.7+N*2.5-2,7.5,5);
	}
	// Pins
	for(p=[0:N-1])translate([-2.5*(N-1)/2+p*2.5,0,-2.1])cylinder(r1=0.3,r2=1,h=2.1);
}
if(hole)
{
	b(0,-10.5/2-7.5+0.3,0,1.1+N*2.5,10.5,5);
}
}

module m2(part=false,hole=false,block=false,punch=false,height,N=0)
{ // J2
// PTSM socket
if(part)
{
	hull()
	{
		b(0,-7.5/2+0.3,0,1.7+N*2.5,7.5,4);
		b(0,-7.5/2+0.3,0,1.7+N*2.5-2,7.5,5);
	}
	// Pins
	for(p=[0:N-1])translate([-2.5*(N-1)/2+p*2.5,0,-2.1])cylinder(r1=0.3,r2=1,h=2.1);
}
if(hole)
{
	b(0,-10.5/2-7.5+0.3,0,1.1+N*2.5,10.5,5);
}
}

module m3(part=false,hole=false,block=false,punch=false,height)
{ // RevK:C_0402 C_0402_1005Metric
// 0402 Capacitor
if(part)
{
	b(0,0,0,1.0,0.5,1); // Chip
	b(0,0,0,1.5,0.65,0.2); // Pad size
}
}

module m4(part=false,hole=false,block=false,punch=false,height)
{ // RevK:R_0402 R_0402_1005Metric
// 0402 Resistor
if(part)
{
	b(0,0,0,1.5,0.65,0.2); // Pad size
	b(0,0,0,1.0,0.5,0.5); // Chip
}
}

module m5(part=false,hole=false,block=false,punch=false,height)
{ // D16
// 1x1mm LED
if(part)
{
        b(0,0,0,1.2,1.2,.8);
}
if(hole)
{
        hull()
        {
                b(0,0,.8,1.2,1.2,1);
                translate([0,0,height])cylinder(d=1.001,h=0.001,$fn=16);
        }
}
if(block)
{
        hull()
        {
                b(0,0,.8,2.8,2.8,1);
                translate([0,0,height])cylinder(d=2,h=1,$fn=16);
        }
}
}

module m6(part=false,hole=false,block=false,punch=false,height)
{ // RevK:ESE13 ESE13V01D
// Tamper switch
rotate([0,0,180])translate([0,2.05,-1.15])
{
	if(part)
	{
		b(0,0,0,3.6,4.2,1.4);
		b(0,-3.08,0,1.2,1.95,0.9);
	}
	if(block)
	{
		b(0,-3.08,1.5,1.2+2,1.95+2,height);
	}
}

}

module m7(part=false,hole=false,block=false,punch=false,height)
{ // RevK:C_0603_ C_0603_1608Metric
// 0603 Capacitor
if(part)
{
	b(0,0,0,1.6,0.8,1); // Chip
	b(0,0,0,1.6,0.95,0.2); // Pad size
}
}

module m8(part=false,hole=false,block=false,punch=false,height)
{ // D10
// DFN1006-2L
if(part)
{
	b(0,0,0,1.0,0.6,0.45); // Chip
}
}

module m9(part=false,hole=false,block=false,punch=false,height)
{ // RevK:L_4x4_ TYA4020
// 4x4 Inductor
if(part)
{
	b(0,0,0,4,4,3);
}
}

module m10(part=false,hole=false,block=false,punch=false,height)
{ // RevK:USB-C-Socket-H CSP-USC16-TR
// USB connector
rotate([-90,0,0])translate([0,1.9,0])
{
	if(part)
	{
        b(0,1.57,0,7,1.14,0.2); // Pads

		translate([0,1.76-7.55,1.63])
		rotate([-90,0,0])
		hull()
		{
			translate([(8.94-3.26)/2,0,0])
			cylinder(d=3.26,h=7.55,$fn=24);
			translate([-(8.94-3.26)/2,0,0])
			cylinder(d=3.26,h=7.55,$fn=24);
		}
		translate([-8.94/2,0.99-1.1/2,0])cube([8.94,1.1,1.6301]);
		translate([-8.94/2,-3.2-1.6/2,0])cube([8.94,1.6,1.6301]);
	}
	if(hole)
		translate([0,-5.79,1.63])
		rotate([-90,0,0])
	{
		// Plug
		hull()
		{
			translate([(8.34-2.5)/2,0,-23+1])
			cylinder(d=2.5,h=23,$fn=24);
			translate([-(8.34-2.5)/2,0,-23+1])
			cylinder(d=2.5,h=23,$fn=24);
		}
		hull()
		{
            translate([(12-7)/2,0,-21-1])
			cylinder(d=7,h=21,$fn=24);
            translate([-(12-7)/2,0,-21-1])
			cylinder(d=7,h=21,$fn=24);
		}
		translate([0,0,-100-10])
			cylinder(d=5,h=100,$fn=24);
	}
}
}

module m11(part=false,hole=false,block=false,punch=false,height)
{ // Q2
// SOT-323_SC-70
if(part)
{
	b(0,0,0,1.26,2.2,1.2);
	b(0,0,0,2.2,2.2,0.6);
}
}

module m12(part=false,hole=false,block=false,punch=false,height)
{ // RevK:SOT-23-6-MD8942 SOT-23-6
// SOT-23-6
if(part)
{
	b(0,0,0,1.726,3.026,1.2); // Part
	b(0,0,0,3.6,2.5,0.5); // Pins
}
}

module m13(part=false,hole=false,block=false,punch=false,height)
{ // RevK:C_1210 C_1210_3225Metric
// 1210 Capacitor
if(part)
{
	b(0,0,0,3.2,2.6,2); // Part
	b(0,0,0,4.1,2.7,0.2); // Pads
}
}

module m14(part=false,hole=false,block=false,punch=false,height)
{ // RevK:C_1206 C_1206_3216Metric
// 1206 Capacitor
if(part)
{
	b(0,0,0,3.2,1.6,1.5); // Part
	b(0,0,0,4.1,1.8,0.2); // Pads
}
}

module m15(part=false,hole=false,block=false,punch=false,height)
{ // D19
// SOD-123 Diode
if(part)
{
	b(0,0,0,2.85,1.8,1.35); // part
	b(0,0,0,4.2,1.2,0.7); // pads
}
}

module m16(part=false,hole=false,block=false,punch=false,height)
{ // U3
// SO-4_4.4x4.3mm_P2.54mm 
if(part)
{
	b(0,0,0,4.5,4.6,2.2); // Part
	b(0,0,0,3.34,6.8,1.5); // Pins
}
}

module m17(part=false,hole=false,block=false,punch=false,height)
{ // U10
// ESP32-S3-MINI-1
translate([-15.4/2,-15.45/2,0])
{
	if(part)
	{
		cube([15.4,20.5,0.8]);
		translate([0.7,0.5,0])cube([14,13.55,2.4]);
		cube([15.4,20.5,0.8]);
	}
}
}

// Generate PCB casework

height=casebottom+pcbthickness+casetop;
$fn=48;

module pyramid()
{ // A pyramid
 polyhedron(points=[[0,0,0],[-height,-height,height],[-height,height,height],[height,height,height],[height,-height,height]],faces=[[0,1,2],[0,2,3],[0,3,4],[0,4,1],[4,3,2,1]]);
}


module pcb_hulled(h=pcbthickness,r=0)
{ // PCB shape for case
	if(useredge)outline(h,r);
	else hull()outline(h,r);
}

module solid_case(d=0)
{ // The case wall
	hull()
        {
                translate([0,0,-casebottom])pcb_hulled(height,casewall-edge);
                translate([0,0,edge-casebottom])pcb_hulled(height-edge*2,casewall);
        }
}

module preview()
{
	pcb();
	color("#0f0")parts_top(part=true);
	color("#0f0")parts_bottom(part=true);
	color("#f00")parts_top(hole=true,punch=true);
	color("#f00")parts_bottom(hole=true,punch=true);
	color("#00f8")parts_top(block=true);
	color("#00f8")parts_bottom(block=true);
}

module top_half(fit=0)
{
	difference()
	{
		translate([-casebottom-100,-casewall-100,pcbthickness+0.01]) cube([pcbwidth+casewall*2+200,pcblength+casewall*2+200,height]);
		translate([0,0,pcbthickness])
        	{
			snape=lip/5;
			snaph=(lip-snape*2)/3;
			if(lipt==1)rotate(lipa)hull()
			{
				translate([0,-pcblength,lip/2])cube([0.001,pcblength*2,0.001]);
				translate([-lip/2,-pcblength,0])cube([lip,pcblength*2,0.001]);
			} else if(lipt==2)for(a=[0,90,180,270])rotate(a+lipa)hull()
			{
				translate([0,-pcblength-pcbwidth,lip/2])cube([0.001,pcblength*2+pcbwidth*2,0.001]);
				translate([-lip/2,-pcblength-pcbwidth,0])cube([lip,pcblength*2+pcbwidth*2,0.001]);
			}
            		difference()
            		{
                		pcb_hulled(lip,casewall);
				if(snap)
                        	{
					hull()
					{
						pcb_hulled(0.1,casewall/2-snap/2+fit);
						translate([0,0,snape])pcb_hulled(snaph,casewall/2+snap/2+fit);
						translate([0,0,lip-snape-snaph])pcb_hulled(0.1,casewall/2-snap/2+fit);
					}
					translate([0,0,lip-snape-snaph])pcb_hulled(snaph,casewall/2-snap/2+fit);
					hull()
					{
						translate([0,0,lip-snape])pcb_hulled(0.1,casewall/2-snap/2+fit);
						translate([0,0,lip])pcb_hulled(0.1,casewall/2+snap/2+fit);
					}
                        	}
				else pcb_hulled(lip,casewall/2+fit);
				if(lipt==0)translate([-pcbwidth,-pcblength,0])cube([pcbwidth*2,pcblength*2,lip]);
				else if(lipt==1) rotate(lipa)translate([0,-pcblength,0])hull()
				{
					translate([lip/2,0,0])cube([pcbwidth,pcblength*2,lip]);
					translate([-lip/2,0,lip])cube([pcbwidth,pcblength*2,lip]);
				}
				else if(lipt==2)for(a=[0,180])rotate(a+lipa)hull()
                		{
                            		translate([lip/2,lip/2,0])cube([pcbwidth+pcblength,pcbwidth+pcblength,lip]);
                            		translate([-lip/2,-lip/2,lip])cube([pcbwidth+pcblength,pcbwidth+pcblength,lip]);
                		}
            		}
            		difference()
            		{
				if(snap)
                        	{
					hull()
					{
						translate([0,0,-0.1])pcb_hulled(0.1,casewall/2+snap/2-fit);
						translate([0,0,snape-0.1])pcb_hulled(0.1,casewall/2-snap/2-fit);
					}
					translate([0,0,snape])pcb_hulled(snaph,casewall/2-snap/2-fit);
					hull()
					{
						translate([0,0,snape+snaph])pcb_hulled(0.1,casewall/2-snap/2-fit);
						translate([0,0,lip-snape-snaph])pcb_hulled(snaph,casewall/2+snap/2-fit);
						translate([0,0,lip-0.1])pcb_hulled(0.1,casewall/2-snap/2-fit);
					}
                        	}
				else pcb_hulled(lip,casewall/2-fit);
				if(lipt==1)rotate(lipa+180)translate([0,-pcblength,0])hull()
				{
					translate([lip/2,0,0])cube([pcbwidth,pcblength*2,lip+0.1]);
					translate([-lip/2,0,lip])cube([pcbwidth,pcblength*2,lip+0.1]);
				}
				else if(lipt==2)for(a=[90,270])rotate(a+lipa)hull()
                		{
                            		translate([lip/2,lip/2,0])cube([pcbwidth+pcblength,pcbwidth+pcblength,lip]);
                            		translate([-lip/2,-lip/2,lip])cube([pcbwidth+pcblength,pcbwidth+pcblength,lip]);
                		}
			}
            	}
		minkowski()
                {
                	union()
                	{
                		parts_top(part=true,hole=true);
                		parts_bottom(part=true,hole=true);
                	}
                	translate([-0.01,-0.01,-height])cube([0.02,0.02,height]);
                }
        }
	minkowski()
        {
        	union()
                {
                	parts_top(part=true,hole=true);
                	parts_bottom(part=true,hole=true);
                }
                translate([-0.01,-0.01,0])cube([0.02,0.02,height]);
        }
}

module case_wall()
{
	difference()
	{
		solid_case();
		translate([0,0,-height])pcb_hulled(height*2,0.02);
	}
}

module top_side_hole()
{
	difference()
	{
		intersection()
		{
			parts_top(hole=true,punch=true);
			case_wall();
		}
		translate([0,0,-casebottom])pcb_hulled(height,casewall);
	}
}

module bottom_side_hole()
{
	difference()
	{
		intersection()
		{
			parts_bottom(hole=true,punch=true);
			case_wall();
		}
		translate([0,0,edge-casebottom])pcb_hulled(height-edge*2,casewall);
	}
}

module parts_space()
{
	minkowski()
	{
		union()
		{
			parts_top(part=true,hole=true,punch=true);
			parts_bottom(part=true,hole=true,punch=true);
		}
		sphere(r=margin,$fn=6);
	}
}

module top_cut(fit=0)
{
	difference()
	{
		top_half(fit);
		if(parts_top)difference()
		{
			minkowski()
			{ // Penetrating side holes
				top_side_hole();
				rotate([180,0,0])
				pyramid();
			}
			minkowski()
			{
				top_side_hole();
				rotate([0,0,45])cylinder(r=margin,h=height,$fn=4);
			}
		}
	}
	if(parts_bottom)difference()
	{
		minkowski()
		{ // Penetrating side holes
			bottom_side_hole();
			pyramid();
		}
			minkowski()
			{
				bottom_side_hole();
				rotate([0,0,45])translate([0,0,-height])cylinder(r=margin,h=height,$fn=4);
			}
	}
}

module bottom_cut()
{
	difference()
	{
		 translate([-casebottom-50,-casewall-50,-height]) cube([pcbwidth+casewall*2+100,pcblength+casewall*2+100,height*2]);
		 top_cut(-fit);
	}
}

module top_body()
{
	difference()
	{
		intersection()
		{
			solid_case();
			pcb_hulled(casetop+pcbthickness,0.03);
		}
		if(parts_top||topthickness)minkowski()
		{
			union()
			{
				if(nohull)parts_top(part=true);
				else hull(){parts_top(part=true);pcb_hulled();}
				if(topthickness)pcb_hulled(casetop+pcbthickness-topthickness,0);
			}
			translate([0,0,margin-height])cylinder(r=margin,h=height,$fn=8);
		}
	}
	intersection()
	{
		pcb_hulled(casetop+pcbthickness,0.03);
		union()
		{
			parts_top(block=true);
			parts_bottom(block=true);
		}
	}
}

module top_edge()
{
	intersection()
	{
		case_wall();
		top_cut();
	}
}

module top_pos()
{ // Position for plotting bottom
	translate([0,0,pcbthickness+casetop])rotate([180,0,0])children();
}

module pcb_pos()
{	// Position PCB relative to base 
		translate([0,0,pcbthickness-height])children();
}

module top()
{
	top_pos()difference()
	{
		union()
		{
			top_body();
			top_edge();
		}
		parts_space();
		pcb_pos()pcb(height,r=margin);
	}
}

module bottom_body()
{ // Position for plotting top
	difference()
	{
		intersection()
		{
			solid_case();
			translate([0,0,-casebottom])pcb_hulled(casebottom+pcbthickness,0.03);
		}
		if(parts_bottom||bottomthickness)minkowski()
		{
			union()
			{
				if(nohull)parts_bottom(part=true);
				else hull()parts_bottom(part=true);
				if(bottomthickness)translate([0,0,bottomthickness-casebottom])pcb_hulled(casebottom+pcbthickness-bottomthickness,0);
			}
			translate([0,0,-margin])cylinder(r=margin,h=height,$fn=8);
		}
	}
	intersection()
	{
		translate([0,0,-casebottom])pcb_hulled(casebottom+pcbthickness,0.03);
		union()
		{
			parts_top(block=true);
			parts_bottom(block=true);
		}
	}
}

module bottom_edge()
{
	intersection()
	{
		case_wall();
		bottom_cut();
	}
}

module bottom_pos()
{
	translate([0,0,casebottom])children();
}

module bottom()
{
	bottom_pos()difference()
	{
		union()
		{
        		bottom_body();
        		bottom_edge();
		}
		parts_space();
		pcb(height,r=margin);
	}
}

module datecode()
{
	minkowski()
	{
		translate([datex,datey,-1])rotate(datea)scale([-1,1])linear_extrude(1)text(date,size=dateh,halign="center",valign="center",font=datef);
		cylinder(d1=datet,d2=0,h=datet,$fn=6);
	}
}

module logocode()
{
	minkowski()
	{
		translate([logox,logoy,-1])rotate(logoa)scale([-1,1])linear_extrude(1)text(logo,size=logoh,halign="center",valign="center",font=logof);
		cylinder(d1=logot,d2=0,h=logot,$fn=6);
	}
}

module namecode()
{
	minkowski()
	{
		translate([namex,namey,-1])rotate(namea)scale([-1,1])linear_extrude(1)text(name,size=nameh,halign="center",valign="center",font=namef);
		cylinder(d1=namet,d2=0,h=namet,$fn=6);
	}
}
difference(){bottom();datecode();}