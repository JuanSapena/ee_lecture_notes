clf;
load('trajectories.mat');

%produce expectation value and ensemble-average comparison
semilogy(x(:,1),exp(0.05*x(:,1)),'lineWidth',6,'color',[.7, .7, 1]);
hold on
semilogy(x1000000(:,1),x1000000(:,2),'lineWidth', 3,'color','k');
legend('Mathematical expectation','N=1,000,000','location','northWest');
axis([0 52 0 20]);
xlabel('t');
ylabel('<x(t)>_N');
set(gca,'LooseInset',get(gca,'TightInset'))
saveas(gca,'./../figs/fig1_4a.pdf');

%long trajectory and time-average growth factor
clf;
semilogy(x1(:,1),exp(.5*log(.9)*x1(:,1)),'lineWidth',6,'color',[.7, .7, 1]);
hold on
semilogy(x1(:,1),x1(:,2),'lineWidth', 3);
legend('Time-average growth','N=1','location','northWest');
axis([0 10000 10^-250 10^50]);
xlabel('t');
ylabel('x(t)');
set(gca,'LooseInset',get(gca,'TightInset'))
saveas(gca,'./../figs/fig1_4b.pdf');
