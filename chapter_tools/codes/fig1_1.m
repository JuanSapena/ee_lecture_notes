clf;
%clear all;
% trajectories are generated in simulations.m
% I'm using the same trajectories (including finite-ensemble averages) for
% all figures, to make it easy, e.g. to compare log vs. linear, short time
% vs. long time etc.
load('trajectories.mat')

stairs(x1(:,1),x1(:,2),'lineWidth', 3);
legend('Wealth','location','northWest');
axis([0 52 min(x1(:,2)), max(x1(:,2))+1]);
xlabel('t');
ylabel('x(t)');
set(gca,'LooseInset',get(gca,'TightInset'))
saveas(gca,'./../figs/fig1_1.pdf');