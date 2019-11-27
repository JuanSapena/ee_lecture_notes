% generate N coin-toss trajectories 
% for t tosses
% save finite-ensemble averages in trajectories.mat
N=1000000;
t=53;
r=rand(t,N);
r(r>.5)=1.5;
r(r<=.5)=.6;
x=ones(t,N+1);
x(1,1)=0;
for i=2:t
     x(i,1)=i-1;
     x(i,2:N+1)=x(i-1,2:N+1).*r(i,:);
%     if mod(t,5)==0 
%         t 
%     end
end
% generate trajectories of finite-ensemble averages 
x1=x(:,1:2);
x100=[x(:,1) mean(x(:,2:101),2)];
x10000=[x(:,1) mean(x(:,2:10001),2)];
x1000000=[x(:,1) mean(x(:,2:1000001),2)];

%extend trajectory for single system
r=rand(10000,1);
r(r>.5)=1.5;
r(r<=.5)=.6;

for i=t+1:10001
    x1(i,1)=i;
    x1(i,2)=x1(i-1,2).*r(i-1);
end

save('trajectories.mat','x','x1','x100','x10000','x1000000');
