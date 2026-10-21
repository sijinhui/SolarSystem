// gpiotype

#ifndef	i
#define i(g,t)
#endif

#ifndef	fi
#define fi(g,t)
#endif

#ifndef	o
#define o(g,t)
#endif

#ifndef	fo
#define fo(g,t)
#endif

#ifndef g
#define g(g)
#endif

#ifndef gg
#define gg(p) g(p)
#endif

#ifndef n
#define n(g,i)
#endif

#ifndef io
#define io(g,t)
#endif

i(I,输入);
fi(E,出门按钮);
fi(O,门已打开);
fi(L,锁已打开);
fi(D,反锁已解除);
fi(M,手动解锁);

o(P,固定输出);
o(O,输出);
fo(L,开锁输出);
fo(D,解除反锁输出);
fo(B,蜂鸣输出);
fo(E,错误输出);

io(IO,输入/输出);
io(I,输入);
io(O,输出);

g(0);
g(1);
g(2);
g(3);
g(4);
g(5);
g(6);
g(7);
g(8);
g(9);
g(10);
g(11);
g(12);
g(13);
g(14);
g(15);
g(16);
g(17);
g(18);
g(19);
g(20);
g(21);
g(22);
g(23);
g(25);
g(26);
g(27);
g(28);
g(29);
g(30);
g(31);
g(32);
g(33);
g(34);
g(35);
g(36);
g(37);
g(38);
g(39);
g(40);
g(41);
g(42);
g(43);
g(44);
g(45);
g(46);
g(47);
gg(48);

n(30,48);
n(31,49);
n(32,50);
n(33,51);
n(34,52);
n(35,53);
n(71,54);
n(72,55);

#undef i
#undef fi
#undef o
#undef fo
#undef g
#undef gg
#undef n
#undef io
