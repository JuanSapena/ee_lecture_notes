clf;
load('trajectories.mat');
% N=1000000;
% t=52;
% r=rand(t,N);
% r(r>.5)=1.5;
% r(r<=.5)=.6;
% x=ones(t,N+1);
% for i=2:t
%     x(i,1)=i;
%     x(i,2:N+1)=x(i-1,2:N+1).*r(i,:);
% end
% x1=x(:,1:2);
% x100=[x(:,1) mean(x(:,2:101),2)];
% x10000=[x(:,1) mean(x(:,2:10001),2)];
% x1000000=[x(:,1) mean(x(:,2:1000001),2)];
%plot(x(:,1),exp(0.05*x(:,1)),'lineWidth',6,'color',[.7, .7, 1]);
stairs(x(:,1),x(:,2),'lineWidth', 3);
hold on
stairs(x100(:,1),x100(:,2),'lineWidth', 3,'Color','g');
stairs(x10000(:,1),x10000(:,2),'lineWidth', 3,'color','r');
stairs(x1000000(:,1),x1000000(:,2),'lineWidth', 3,'color','k');
legend('N=1','N=100','N=10,000','N=1,000,000','location','northWest');
axis([0 52 0 max(x(:,2))+1 ]);
xlabel('t');
ylabel('<x(t)>_N');
set(gca,'LooseInset',get(gca,'TightInset'))
saveas(gca,'./../figs/fig1_2a.pdf');

%...and on log-y scale
clf;
stairs(x(:,1),x(:,2),'lineWidth', 3);
hold on
stairs(x100(:,1),x100(:,2),'lineWidth', 3,'Color','g');
stairs(x10000(:,1),x10000(:,2),'lineWidth', 3,'color','r');
stairs(x1000000(:,1),x1000000(:,2),'lineWidth', 3,'color','k');
set(gca, 'YScale', 'log')
legend('N=1','N=100','N=10,000','N=1,000,000','location','northWest');
axis([0 52 0.1 max(x(:,2))+10]);
xlabel('t');
ylabel('<x(t)>_N');
set(gca,'LooseInset',get(gca,'TightInset'))
saveas(gca,'./../figs/fig1_2b.pdf');
