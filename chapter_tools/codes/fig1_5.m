t=10000;
r=rand(t);
r(r>.5)=1;
r(r<=.5)=-1;
y(1,1)=1;
y(1,2)=1;
for i=2:t
    y(i,1)=i;
    y(i,2)=y(i-1,2)+r(i);
    y(i,3)=mean(y(1:i,2));
end

clf;

%single trajectory does not self-average
plot(y(:,1),y(:,3),'lineWidth',3,'color','b');
hold on
plot(y(:,1),0,'lineStyle',':');
legend('Finite-time average','location','northEast');
axis([0 10000 min(y(:,3))-1 max(y(:,3))+1]);
xlabel('t');
ylabel('\bar{x}_t');
set(gca,'LooseInset',get(gca,'TightInset'))
saveas(gca,'./../figs/fig1_5.pdf');