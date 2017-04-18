clf;
t=1000;
dt=0.1;
sdt=sqrt(dt);
r=randn(t);
mu=0.05;
sigma=sqrt(.1);
z=ones(t,2);
for i=2:t
    z(i,1)=i*dt;
    z(i,2)=z(i-1,2).*(1+mu*dt+ sigma * sdt*r(i));
end

clf;

%single trajectory does not self-average
plot(z(:,1),z(:,2),'lineWidth',3,'color','b');
legend('GBM trajectory','location','northWest');
axis([0 1000*dt min(z(:,2)) max(z(:,2))+1]);
xlabel('t');
ylabel('x(t)');
set(gca,'LooseInset',get(gca,'TightInset'))
saveas(gca,'./../figs/fig1_6.pdf');